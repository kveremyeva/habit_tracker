from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from habits.models import Habits
from habits.paginators import HabitsPagination
from habits.serializers import HabitsSerializer
from users.permissions import IsOwner


class HabitsCreateApiView(CreateAPIView):
    """Класс контроллера для создания привычки"""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer


    def perform_create(self, serialazer):
        """метод автоматического сохранения пользователя в поле владельца"""
        habits = serialazer.save()
        habits.user = self.request.user
        habits.save()


class HabitsListApiView(ListAPIView):
    """Класс контроллера для вывода списка привычек"""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        """метод отображения привычек заданного пользователя"""
        return Habits.objects.filter(user=self.request.user)


class HabitsRetrieveApiView(RetrieveAPIView):
    """Класс контроллера для вывода экземпляра привычки"""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsOwner,)


class HabitsUpdateApiView(UpdateAPIView):
    """Класс контроллера для изменения экземпляра привычки"""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsOwner,)


class HabitsDestroyApiView(DestroyAPIView):
    """Класс контроллера для удаления экземпляра привычки"""

    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = (IsOwner,)


class PublishedHabitsListView(ListAPIView):
    """Класс контроллера для списка публичных привычек"""

    queryset = Habits.objects.filter(is_published=True)
    serializer_class = HabitsSerializer
    permission_classes = [AllowAny]
