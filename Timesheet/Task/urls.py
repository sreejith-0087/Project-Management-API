from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, EmployeeViewSet



router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'employees', EmployeeViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
]

