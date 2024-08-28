from django.urls import path

from users.views import UserListView, CreateTokenView

app_name = "users"

urlpatterns = [
    path("", UserListView.as_view(), name="users-list"),
    path("token/", CreateTokenView.as_view(), name="create-token"),
]
