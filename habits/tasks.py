from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habits
from users.services import send_telegram_message


@shared_task
def send_habit_reminders():
    """Отправка уведомлений для ВСЕХ пользователей"""
    from datetime import datetime, timedelta

    now = datetime.now()
    current_time = now.time()

    # Время через 5 минут
    reminder_datetime = datetime.combine(datetime.today(), current_time) + timedelta(minutes=5)
    reminder_time = reminder_datetime.time()

    # Фильтруем по времени и наличию telegram_chat_id
    habits = Habits.objects.filter(
        time__hour=reminder_time.hour,
        time__minute=reminder_time.minute,
        user__telegram_chat_id__isnull=False  # Только у кого есть Telegram
    ).select_related('user')

    for habit in habits:
        message = f"Мне нужно {habit.action} в {habit.time.strftime('%H:%M')} в {habit.place}"
        send_telegram_message(habit.user.telegram_chat_id, message)
