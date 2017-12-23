from django.urls import include, path

from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from . import views


# app_name = 'employee'

router = DefaultRouter()
router.register(r'', views.EmployeeViewSet)
router.register(r'department', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', get_schema_view(title='Luizalabs Employee Manager')),
    path('docs/', include_docs_urls(title='API Docs')),
]
