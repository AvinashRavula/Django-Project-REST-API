from rest_framework import status, serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *
from todolist.models import ToDoList
from todolist.serializers.todo_serializer import ToDoSerializer


class TodoAPI(ListCreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer
    # permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = self.request.user.id
        todolist_serialized = ToDoSerializer(data=data)
        if todolist_serialized.is_valid():
            todolist_serialized.save()
            return Response(todolist_serialized.data,status.HTTP_200_OK)
        return Response(todolist_serialized.errors,status.HTTP_400_BAD_REQUEST)


# class TodoPutDeleteGetPatchAPI(RetrieveUpdateDestroyAPIView):
#     