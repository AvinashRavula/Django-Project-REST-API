from rest_framework.serializers import ModelSerializer

from todolist.models import ToDoList


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('title', 'task_completed', 'user')

    def create(self, validated_data):
        return ToDoList.objects.create(**validated_data)