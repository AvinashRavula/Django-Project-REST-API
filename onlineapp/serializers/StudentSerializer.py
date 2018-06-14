from rest_framework import generics
from rest_framework.serializers import ModelSerializer

from onlineapp.models import Student


class StudentSerializer(ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'name', 'dob', 'email', 'dropped_out', 'db_folder', 'college')

    def create(self, validated_data, **kwargs):
        return Student.objects.create(**validated_data)

