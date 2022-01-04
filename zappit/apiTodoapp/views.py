from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from todoapp.models import Todo


class CompletedList(generics.ListAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by(
            '-datecompleted')
