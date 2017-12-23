from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

app_name = 'employee'

router = DefaultRouter()
router.register(r'department', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
