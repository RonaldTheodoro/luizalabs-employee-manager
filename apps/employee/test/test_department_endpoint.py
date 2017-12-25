import json

from rest_framework import status

from .base_test import BaseEndPointTest


class DepartmentEndPointTest(BaseEndPointTest):

    def test_get_list_department(self):
        response = self.client.get(self.url('department-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_number_of_registers(self):
        response = self.client.get(self.url('department-list'))
        itens = self.create_json(response)
        self.assertEqual(3, itens['count'])

    def test_get_detail_department(self):
        response = self.client.get(self.url('department-detail', 1))
        department = self.create_json(response)
        self.assertEqual(department['name'], 'Architecture')

    def test_put_department(self):
        response = self.client.put(
            self.url('department-detail', 1),
            data=json.dumps({'name': 'Help Desk'}),
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        department = self.create_json(response)
        self.assertEqual(department['name'], 'Help Desk')

    def test_delete_department(self):
        response = self.client.delete(self.url('department-detail', 1))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
