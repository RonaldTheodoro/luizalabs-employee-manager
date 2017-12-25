import json

from rest_framework import status

from .base_test import BaseEndPointTest


class EmployeeEndPointTest(BaseEndPointTest):

    def test_get_list_employee(self):
        """GET /employee/ must return status code 200"""
        response = self.client.get(self.url('employee-list'))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_number_of_registers(self):
        """GET /employee/ must return 3 itens"""
        response = self.client.get(self.url('employee-list'))
        itens = self.create_json(response)
        self.assertEqual(3, itens['count'])

    def test_get_detail_employee(self):
        """GET /employee/1/ must return Arnaldo Pereira employee"""
        response = self.client.get(self.url('employee-detail', 1))
        employee = self.create_json(response)
        self.assertEqual(employee['name'], 'Arnaldo Pereira')

    def test_put_employee(self):
        """PUT /employee/1/ must return status code 200"""
        response = self.client.put(
            self.url('employee-detail', 1),
            data=json.dumps(
                {
                    'name': 'Shimira Cheng',
                    'email': 'shimira@cheng.com', 
                    'department': 'Mobile',
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        employee = self.create_json(response)
        self.assertEqual(employee['name'], 'Shimira Cheng')
        self.assertEqual(employee['email'], 'shimira@cheng.com')
        self.assertEqual(employee['department'], 'Mobile')

    def test_patch_employee(self):
        """PATCH /employee/1/ must return status code 200"""
        response = self.client.patch(
            self.url('employee-detail', 2),
            data=json.dumps(
                {'name': 'Ryoga Kamishiro', 'email': 'ryoga@kamishiro.com'}
            ),
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        employee = self.create_json(response)
        self.assertEqual(employee['name'], 'Ryoga Kamishiro')
        self.assertEqual(employee['email'], 'ryoga@kamishiro.com')

    def test_delete_employee(self):
        """DELETE /employee/1/ must return status code 204"""
        response = self.client.delete(self.url('employee-detail', 3))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
