import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase


class BaseEndPointTest(APITestCase):
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
        user = User.objects.create_user(
            'ronaldtheodoro',
            'ronald@theodoro.com',
            'asdf1234'
        )
        self.client.force_authenticate(user=user)
        self.create_data()

    def create_data(self):
        self.create_data_department()
        self.create_data_employee()

    def create_data_department(self):
        for department in self.departments:
            self.client.post(reverse('department-list'), department)

    def create_data_employee(self):
        for employee in self.employees:
            self.client.post(reverse('employee-list'), employee)

    def create_json(self, response):
        return json.loads(response.rendered_content)

    def url(self, url, pk=None):
        if pk is not None:
            return reverse(url, kwargs={'pk': pk})
        return reverse(url)
