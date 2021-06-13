from rest_framework import viewsets
from rest_framework.exceptions import ParseError

from .serializers import TaskSerializer, TaskGroupSerializer, RoleSerializer
from .models import Task, TaskGroup, Role


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        pk = self.request.GET.get('group')
        if pk is None:
            raise ParseError(detail="Не передан id списка задач")
        queryset = Task.objects.filter(task_group__pk=pk)
        return queryset


class TaskGroupViewSet(viewsets.ModelViewSet):
    queryset = TaskGroup.objects.all()
    serializer_class = TaskGroupSerializer
