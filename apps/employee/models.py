from django.db import models

class Department(models.Model):
    name = models.CharField('name', max_length=150)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField('name', max_length=150)
    email = models.EmailField('email')
    department = models.ForeignKey(
        'Department',
        verbose_name='department',
        related_name='employees',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
