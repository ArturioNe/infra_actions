from http import HTTPStatus
from django.urls import reverse

from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.guest_client = Client()

    def test_about_url_exists_at_desired_location(self):
        """Проверка доступности страниц."""
        response = StaticPagesURLTests.guest_client.get(reverse('index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        response = self.guest_client.get('second_page')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_page_shows_correct_context(self):
        """Проверка контекста страниц."""
        response = self.guest_client.get(reverse('index'))
        self.assertContains(response, 'У меня получилось!')
        response = self.guest_client.get(reverse('second_page'))
        self.assertContains(response, 'А это вторая страница!')
