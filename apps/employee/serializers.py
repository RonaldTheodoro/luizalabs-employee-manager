from rest_framework import serializers

from . import models


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Department
        fields = ('id', 'name', )


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')

    class Meta:
        model = models.Employee
        fields = ('id', 'name', 'email', 'department', )
