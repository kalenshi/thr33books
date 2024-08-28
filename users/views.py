from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import User
from .serializers import TokenSerializer, UserSerializer


class UserListView(APIView):
    """View for interacting with the user models without id"""
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    @swagger_auto_schema(
        operation_description="Endpoint for Listing users based on different filters",
        manual_parameters=[
            openapi.Parameter(
                name="email",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Email address of the user (Unique)",
            )
        ]
    )
    def get(self, request):
        """Retrieve all users of the System"""
        paginator = self.pagination_class()
        page = request.GET.get("page", 1)
        results = paginator.paginate_queryset(User.objects.all().order_by("id"), request)
        serializer = self.serializer_class(results, many=True)
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_description="Endpoint for Creating a new user",
        request_body=UserSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Schema(type=openapi.TYPE_OBJECT),
        }
    )
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateTokenView(ObtainAuthToken):
    """ The auth-token view"""
    serializer_class = TokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
