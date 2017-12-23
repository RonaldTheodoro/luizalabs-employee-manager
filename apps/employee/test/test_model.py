from django.test import TestCase

from .. import models


class DepartmentModelTest(TestCase):

    def setUp(self):
        self.obj = models.Department.objects.create(name='Architecture')

    def test_create(self):
        self.assertTrue(models.Department.objects.exists())

    def test_str(self):
        self.assertEqual('Architecture', str(self.obj))


class EmployeeModelTest(TestCase):

    def setUp(self):
        department = models.Department.objects.create(name='Architecture')
        self.obj = models.Employee.objects.create(
            name='Arnaldo Pereira',
            email='arnaldo@luizalabs.com',
            department=department
        )

    def test_create(self):
        self.assertTrue(models.Employee.objects.exists())

    def test_str(self):
        self.assertEqual('Arnaldo Pereira', str(self.obj))
