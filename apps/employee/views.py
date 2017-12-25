from rest_framework import viewsets, permissions

from . import models, serializers


class DepartmentViewSet(viewsets.ModelViewSet):
    """Department API End Point"""
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

    permission_classes = (permissions.IsAuthenticated,)


class EmployeeViewSet(viewsets.ModelViewSet):
    """Employee API End Point"""
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

    permission_classes = (permissions.IsAuthenticated,)