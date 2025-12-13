from rest_framework import serializers

from habits.models import Habits


class HabitsSerializer(serializers.ModelSerializer):
    """Сериализатор для отображения привычек"""
    class Meta:
        model = Habits
        fields = "__all__"
        read_only_fields = ["id", "user"]

    def validate(self, attrs):
        """Функция валидации полей модели привычки"""
        habit = Habits(**attrs)
        habit.clean()
        return attrs
