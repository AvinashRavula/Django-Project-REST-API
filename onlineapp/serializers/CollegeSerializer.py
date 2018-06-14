from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from onlineapp.models import College, Mocktest1, Student
from onlineproject import settings


class CollegeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    location = serializers.CharField(required=True,style={'base_template': 'textarea.html'})
    acronym = serializers.CharField(required=True)
    contact = serializers.EmailField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return College.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.acronym = validated_data.get('acronym', instance.acronym)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.save()
        return instance


