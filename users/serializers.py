from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer class for the Systems user model"""
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password1 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "password",
            "password1"
        )
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
            "password1": {"write_only": True, "style": {"input_type": "password"}},
        }

    def validate(self, attrs):
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError(_("Email already registered."), code="unique")
        if attrs["password"] != attrs["password1"]:
            raise serializers.ValidationError(
                _("Passwords do not match."), code="password_mismatch"
            )
        return attrs

    def create(self, validated_data):
        _ = validated_data.pop("password1")
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return instance"""

        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password is not None:
            user.set_password(password)
            user.save()
        return user


class TokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password
        )

        if not user:
            msg = _("Unable to Authenticate with provided credentials")
            raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs
