from urllib import request

from django.test import TestCase

# Create your tests here.
import requests
from rest_framework import status

from onlineapp.models import College
from onlineapp.serializer import *

class SerializeTestMethods(TestCase):

    def setUp(self):
        self.college = College.objects.create(name="Sree Chaitanya",location="Karimnagar",acronym="scce",contact="website@scce.ac.in")
        self.serialize = OnlineappSerializer(self.college)

    def test_serializer_valid_one(self):
        self.assertEqual(self.serialize.data, {'name':'Sree Chaitanya', 'location':'Karimnagar'
                                               ,'acronym':'scce','contact':'website@scce.ac.in'})

    def test_serializer_invalid_one(self):
        self.assertNotEqual(self.serialize.data, {'name':'SreeChaitanya', 'location':'Karimnagar'
                                               ,'acronym':'scce','contact':'website@scce.ac.in'})

    def test_api(self):

        result = requests.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/123")
        self.assertEqual(result.status_code,status.HTTP_404_NOT_FOUND)

        result = requests.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/6")
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        result = requests.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/")
        self.assertEqual(result.status_code, status.HTTP_200_OK)

        result = requests.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/123")
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)

        result = requests.post("http://127.0.0.1:8000/onlineapp/api/v1/colleges/",data={'name':"TestName",'location':"TestPlace",
                               'acronym':"TEST",'contact':"test@test.test"})
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        college_max_id = College.objects.all().order_by("-id")[0]
        result = requests.delete("http://127.0.0.1:8000/onlineapp/api/v1/colleges/"+college_max_id)
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

        result = requests.delete("http://127.0.0.1:8000/onlineapp/api/v1/colleges/")
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)