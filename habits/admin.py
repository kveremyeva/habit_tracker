from django.contrib import admin
from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    """Класс описания административной панели"""

    list_display = ("id", "action", "is_pleasant", "user", "is_published")
    list_filter = ("action", "is_pleasant", "user")
    search_fields = ("action", "is_pleasant", "user")
