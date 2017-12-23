from rest_framework import serializers

from . import models


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    employee = serializers.HyperlinkedIdentityField(
        view_name='employee-detail'
    )

    class Meta:
        model = models.Department
        fields = ('id', 'name', 'employee', 'url', )


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.name')
    department_url = serializers.HyperlinkedIdentityField(
        view_name='department-detail'
    )

    class Meta:
        model = models.Employee
        fields = (
            'id', 'name', 'email', 'department', 'department_url', 'url',
        )
