import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class BaseEndPointTest(APITestCase):
    url = reverse('employee-list')
    departments = [
        {'name': 'Architecture'},
        {'name': 'E-commerce'},
        {'name': 'Mobile'}
    ]
    employees = [
        {
            'name': 'Arnaldo Pereira',
            'email': 'arnaldo@luizalabs.com',
            'department': 'Architecture',
        },
        {
            'name': 'Renato Pedigoni',
            'email': 'renato@luizalabs.com',
            'department': 'E-commerce',
        },
        {
            'name': 'Thiago Catoto',
            'email': 'catoto@luizalabs.com',
            'department': 'Mobile',
        }
    ]

    def setUp(self):
        self.create_data()
        self.response = self.client.get(self.url)

    def create_data(self):
        for department in self.departments:
            self.client.post(reverse('department-list'), department)
        for employee in self.employees:
            self.client.post(reverse('employee-list'), employee)

    def create_json(self, response=None):
        if response is not None:
            return json.loads(response.rendered_content)
        return json.loads(self.response.rendered_content)

    def detail_url(self, pk):
        return reverse('employee-detail', kwargs={'pk': pk})


class EmployeeEndPointTest(BaseEndPointTest):

    def test_get_list_employee(self):
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_get_number_of_registers(self):
        itens = self.create_json()
        self.assertEqual(3, itens['count'])

    def test_get_detail_employee(self):
        response = self.client.get(self.detail_url(1))
        employee = self.create_json(response)
        self.assertEqual(employee['name'], 'Arnaldo Pereira')

    def test_put_employee(self):
        response = self.client.put(
            self.detail_url(1),
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
        response = self.client.patch(
            self.detail_url(2),
            data=json.dumps(
                {
                    'name': 'Ryoga Kamishiro',
                    'email': 'ryoga@kamishiro.com'
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        employee = self.create_json(response)
        self.assertEqual(employee['name'], 'Ryoga Kamishiro')
        self.assertEqual(employee['email'], 'ryoga@kamishiro.com')
