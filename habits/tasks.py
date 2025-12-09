from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habits
from users.services import send_telegram_message


@shared_task
def task():
    """Периодическая задача отправки уведомлений в телеграмм за 5 минут до начала выполнения привычки"""
    habits = Habits.objects.all()
    for habit in habits:
        if habit.user.chat_id and habit.time <= datetime.now().time() - timedelta(
            minutes=5
        ):
            text = f"Мне нужно {habit.action} в {habit.time} в {habit.place}"
            send_telegram_message(text, habit.user.telegram_chat_id)
