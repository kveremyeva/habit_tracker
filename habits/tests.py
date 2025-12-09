from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            password="testpass123"
        )
        self.habits = Habits.objects.create(
            user=self.user,
            place="Тест",
            time="09:00:00",
            action="Тестируем создание привычки",
            execution_time=10,
            period=1,
            is_published=False
        )
        self.client.force_authenticate(user=self.user)

    def test_habits_retrieve(self):
        url = reverse("habits:habits-retrieve", args=(self.habits.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habits.place)

    def test_habits_create(self):
        """Тест создания привычки"""
        url = reverse("habits:habits-create")
        data = {
            "place": "Новое место",
            "time": "10:00:00",
            "action": "Новая тестовая привычка",
            "execution_time": 15,
            "period": 2,
            "is_published": True
        }
        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)

        self.assertEqual(
            response.json(),
            {'id': 2, 'place': 'Новое место', 'time': '10:00:00',
             'action': 'Новая тестовая привычка',
             'is_pleasant': False, 'period': 2, 'reward': None, 'execution_time': 15,
             'is_published': True, 'user': None, 'related_habit': None}
        )

        self.assertTrue(
            Habits.objects.all().exists()
        )
        response_data = response.json()
        self.assertIn('id', response_data)
        self.assertEqual(response_data['place'], "Новое место")
        self.assertEqual(response_data['action'], "Новая тестовая привычка")

    def test_list_habits(self):
        """Тест вывода списка привычек"""
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Habits.objects.filter(user=self.user).exists())

    def test_habits_update(self):
        """Тест обновления привычки"""
        url = reverse("habits:habits-update", args=(self.habits.pk,))
        data = {"place": "Парк"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Парк")

    def test_habits_delete(self):
        """Тест удаления привычки"""
        url = reverse("habits:habits-delete", args=(self.habits.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)
