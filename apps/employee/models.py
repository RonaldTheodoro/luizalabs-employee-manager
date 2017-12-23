from django.db import models

class Department(models.Model):
    name = models.CharField('name', max_length=150)

    class Meta:
        ordering = ('name', )
        verbose_name = 'departamento'
        verbose_name_plural = 'departamentos'

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

    class Meta:
        ordering = ('name', )
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'

    def __str__(self):
        return self.name
