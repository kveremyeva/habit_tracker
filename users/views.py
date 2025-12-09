from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.models import User
from users.serializers import UserRegisterSerializer, UserSerializer, TelegramConnectSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер создания профиля"""
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(
            user.password
        )
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер просмотра деталей пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(ListAPIView):
    """Контроллер вывода списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class TelegramConnectAPIView(generics.UpdateAPIView):
    """Привязка Telegram к пользователю"""
    serializer_class = TelegramConnectSerializer
    permission_classes = [IsAuthenticated]
