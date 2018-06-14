from rest_framework.serializers import ModelSerializer

from onlineapp.models import Student, Mocktest1
from onlineapp.serializers.Mocktest1Serializer import Mocktest1Serializer


class StudentDetailSerializer(ModelSerializer):
    mocktest1 = Mocktest1Serializer()
    class Meta:
        model = Student
        fields = ('id', 'name', 'dob', 'email', 'dropped_out', 'db_folder', 'college', 'mocktest1')

    def create(self, validated_data, **kwargs):
        mocktest1_data = validated_data.pop('mocktest1')
        student = Student.objects.create(**validated_data)
        if hasattr(validated_data, 'mocktest1'):
            mocktest1_temp = Mocktest1Serializer(**mocktest1_data,student=student)
        return student

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.db_folder = validated_data.get('db_folder',instance.db_folder)
        instance.dropped_out = validated_data.get('dropped_out', instance.dropped_out)
        # instance.college_id = validated_data.get('college_id', instance.college_id)
        mocktest_data = validated_data.pop('mocktest1')
        if mocktest_data:
           instance.mocktest1.problem1 = mocktest_data.get('problem1', instance.mocktest1.problem1)
           instance.mocktest1.problem2 = mocktest_data.get('problem2', instance.mocktest1.problem2)
           instance.mocktest1.problem3 = mocktest_data.get('problem3', instance.mocktest1.problem3)
           instance.mocktest1.problem4 = mocktest_data.get('problem4', instance.mocktest1.problem4)
        instance.save()
        return instance