from django.core.validators import MaxValueValidator
from django.db import models
from config import settings
from habits.validators import (validate_period, validate_execution_time,
                               validate_pleasant_habit, validate_habit_fields,
                               validate_related_habit)


class Habits(models.Model):
    """ Модель привычек"""
    PERIODICITY_CHOICES = [
        (1, 'Ежедневно'),
        (2, 'Раз в два дня'),
        (3, 'Раз в три дня'),
        (4, 'Раз в четыре дня'),
        (5, 'Раз в пять дней'),
        (6, 'Раз в шесть дней'),
        (7, 'Еженедельно'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             null=True, blank=True, verbose_name='Пользователь')
    place = models.CharField(max_length=255, verbose_name="Место")
    time = models.TimeField(verbose_name="Время")
    action = models.CharField(max_length=500, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=False, verbose_name="Признак полезной привычки")
    related_habit = models.ForeignKey("self", on_delete=models.SET_NULL, null=True,
                                      blank=True, verbose_name="Связанная привычка",)
    period = models.PositiveIntegerField(choices=PERIODICITY_CHOICES, default=1,
                                         validators=[validate_period], verbose_name="Периодичность")
    reward = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вознаграждение")
    execution_time = models.PositiveSmallIntegerField(validators=[MaxValueValidator(120),
                                                      validate_execution_time], verbose_name="Время на выполнение")
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['time']

    def __str__(self):
        return f"{self.action} в {self.time} в {self.place}"

    def clean(self):
        """Валидация модели"""
        validate_pleasant_habit(self)
        validate_habit_fields(self)
        if self.related_habit:
            validate_related_habit(self.related_habit)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
