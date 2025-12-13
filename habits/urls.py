from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitsCreateApiView, HabitsListApiView, HabitsRetrieveApiView, HabitsUpdateApiView, \
    HabitsDestroyApiView, PublishedHabitsListView

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/create/", HabitsCreateApiView.as_view(), name="habits-create"),
    path("habits/", HabitsListApiView.as_view(), name="habits-list"),
    path("habits/<int:pk>/", HabitsRetrieveApiView.as_view(), name="habits-retrieve"),
    path("habits/<int:pk>/update/", HabitsUpdateApiView.as_view(), name="habits-update"),
    path("habits/<int:pk>/delete/", HabitsDestroyApiView.as_view(), name="habits-delete"),
    path("published-habits/", PublishedHabitsListView.as_view(), name="published-habits-list"),
]
