from rest_framework.serializers import ModelSerializer

from onlineapp.models import Mocktest1


class Mocktest1Serializer(ModelSerializer):
    class Meta:
        model = Mocktest1
        fields = ('problem1', 'problem2', 'problem3', 'problem4')
