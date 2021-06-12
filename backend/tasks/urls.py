from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('task_groups', views.TaskGroupViewSet)
router.register('role', views.RoleViewSet)


app_name = 'tasks'


urlpatterns = [
    path('', include(router.urls)),
]
