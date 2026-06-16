from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UserCreateView,
    MeView,
    UserUpdateView,
    ChangePasswordView,
    UserListView,
    LastTwoUsersView,
)

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
    path("me/", MeView.as_view(), name="me"),
    path("me/update/", UserUpdateView.as_view(), name="me-update"),
    path("me/change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("last-two/", LastTwoUsersView.as_view(), name="last-two-users"),
]


#router = DefaultRouter()
#router.register(r"", UserViewSet, basename="users")
#
#urlpatterns = router.urls