from rest_framework import generics, permissions
from django.contrib.auth.models import User
from rest_auth.views import LoginView, LogoutView
from . import serializers
from . permissions import IsAccountOwner


class CustomLoginView(LoginView):
    permission_classes = (permissions.AllowAny,)


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsAccountOwner)


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer
    permission_classes = (permissions.AllowAny,)


