import json
from unittest import skip

from django.urls import reverse

from rest_framework.test import APITestCase


class DepartmentGetEndPointTest(APITestCase):
    url = reverse('department-list')

    def setUp(self):
        self.response = self.client.get(self.url)

    def test_get_department(self):
        self.assertEqual(200, self.response.status_code)


class DepartmentPostEndPointTest(APITestCase):
    url = reverse('department-list')
    data = [
        {'name': 'Architecture'},
        {'name': 'E-commerce'},
        {'name': 'Mobile'}
    ]

    def setUp(self):
        self.create_data()
        self.response = self.client.get(self.url)

    def create_data(self):
        for register in self.data:
            self.client.post(self.url, register)

    def create_json(self):
        return json.loads(self.response.rendered_content)

    def test_get_number_of_registers(self):
        itens = self.create_json()
        self.assertEqual(3, itens['count'])