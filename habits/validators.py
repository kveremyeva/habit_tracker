from django.core.exceptions import ValidationError


def validate_execution_time(value):
    """Проверка времени выполнения (не более 120 секунд)"""
    if value > 120:
        raise ValidationError('Время выполнения не должно превышать 120 секунд.')


def validate_related_habit(value):
    """Проверка связанной привычки"""
    if value and not value.is_pleasant:
        raise ValidationError(
            'В связанные привычки могут попадать только привычки '
            'с признаком приятной привычки.'
        )


def validate_pleasant_habit(instance):
    """Проверка приятной привычки"""
    if instance.is_pleasant:
        if instance.reward:
            raise ValidationError(
                'У приятной привычки не может быть вознаграждения.'
            )
        if instance.related_habit:
            raise ValidationError(
                'У приятной привычки не может быть связанной привычки.'
            )


def validate_period(value):
    """Проверка периодичности (не реже 1 раза в 7 дней)"""
    if value > 7:
        raise ValidationError(
            'Нельзя выполнять привычку реже, чем 1 раз в 7 дней.'
        )


def validate_habit_fields(instance):
    """Проверка взаимного исключения связанной привычки и вознаграждения"""
    if instance.related_habit and instance.reward:
        raise ValidationError(
            'Нельзя одновременно указывать и связанную привычку, и вознаграждение.'
        )
