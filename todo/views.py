from .models import TodoItem
from .serializers import TodoItemSerializer, TodoItemCreateSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class TodoItemViewSet(ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.action == "create":
            return TodoItemCreateSerializer
        return self.serializer_class
