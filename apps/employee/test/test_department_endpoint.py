import json
from unittest import skip

from django.urls import reverse

from rest_framework.test import APITestCase


class BaseEndPointTest(APITestCase):
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

    def create_json(self, response=None):
        if response is not None:
            return json.loads(response.rendered_content)
        return json.loads(self.response.rendered_content)

    def detail_url(self, pk):
        return reverse('department-detail', kwargs={'pk': pk})


class DepartmentEndPointTest(BaseEndPointTest):

    def test_get_list_department(self):
        self.assertEqual(200, self.response.status_code)

    def test_get_number_of_registers(self):
        itens = self.create_json()
        self.assertEqual(3, itens['count'])

    def test_get_detail_department(self):
        response = self.client.get(self.detail_url(1))
        department = self.create_json(response)
        self.assertEqual(department['name'], 'Architecture')

    def test_put_department(self):
        response = self.client.put(
            self.detail_url(1),
            data=json.dumps({'name': 'Help Desk'}),
            content_type='application/json'
        )
        self.assertEqual(200, response.status_code)
        department = self.create_json(response)
        self.assertEqual(department['name'], 'Help Desk')