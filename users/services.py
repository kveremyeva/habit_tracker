import requests

from config import settings


def send_telegram_message(telegram_chat_id, message):
    """Функция отправки уведомления в телеграмм"""
    params = {
        "text": message,
        "telegram_chat_id": telegram_chat_id,
    }
    requests.get(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params
    )
