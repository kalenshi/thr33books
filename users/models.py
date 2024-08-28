from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """The Objects class of the user model"""

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        """
        Creates and saves a new user
        Args:
            email(str): The unique email of the user
            first_name(str): The first name of the user
            last_name(str): The last name of the user
            password(str): The password of the user to be saved as a hashed password
            **extra_fields(dict): Extra fields to be passed to the user creation

        Returns:
            User: The created user
        Raises:
            ValueError: If the email is not passed in or is not unique to the system
        """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        """
          Creates and saves a new superuser
          Args:
              email(str): The unique email of the user
              first_name(str): The first name of the user
              last_name(str): The last name of the user
              password(str): The password of the user to be saved as a hashed password
              **extra_fields(dict): Extra fields to be passed to the user creation

          Returns:
              User: The created superuser
          Raises:
              ValueError: If the email is not passed in or is not unique to the system
          """
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    The user model for the system
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        """String representation of the user model"""
        return f"{self.pk}:{self.email}"

    def __repr__(self):
        """Developer friendly String representation of the user model"""
        return f"User({self.email}, {self.first_name}, {self.last_name})"
