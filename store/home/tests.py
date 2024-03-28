from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus


class HomeViewTestCase(TestCase):

    def test_view(self):
        path = reverse('home')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Roselissa')
