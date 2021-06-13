from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='task')
router.register('task_groups', views.TaskGroupViewSet, basename='task_group')
router.register('role', views.RoleViewSet, basename='role')


app_name = 'tasks'


urlpatterns = [
    path('', include(router.urls)),
]
