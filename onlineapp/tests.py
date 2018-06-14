from urllib import request

from django.test import TestCase,Client

# Create your tests here.
import requests
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.utils import json

from onlineapp.models import College
from onlineapp.serializers import *

class SerializeTestMethods(TestCase):

    def setUp(self):
        self.c = Client()
        self.result = ""
        # self.college = College.objects.create(name="Sree Chaitanya",location="Karimnagar",acronym="scce",contact="website@scce.ac.in")
        # self.serialize = CollegeSerializer(self.college)

    def test_post_create_college_valid(self):
        new_data = {'name':"TestName",'location':"TestPlace",
                               'acronym':"TEST",'contact':"test@test.test"}
        self.result = self.c.post('api/v1/colleges/',data=new_data)
        import ipdb
        ipdb.set_trace()
        json_data = json.loads(self.result.content)
        new_data['id'] = json_data['id']
        print(json_data)
        print(new_data)
        self.assertEqual(json_data, new_data)

    def test_post_create_college_status_code_valid(self):
        self.assertEqual(self.result.status_code, status.HTTP_201_CREATED)

    # def test_get_college_id_invalid(self):
    #     result = requests.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/123")
    #     self.assertEqual(result.status_code,status.HTTP_404_NOT_FOUND)
    #
    # def test_get_college_id_valid(self):
    #     result = requests.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/6")
    #     self.assertEqual(result.status_code, status.HTTP_200_OK)
    #
    # def test_get_all_colleges_valid(self):
    #     result = requests.get("http://127.0.0.1:8000/onlineapp/api/v1/colleges/")
    #     self.assertEqual(result.status_code, status.HTTP_200_OK)
    #
    #
    # def test_post_create_college_invalid(self):
    #     result = requests.post("http://127.0.0.1:8000/onlineapp/api/v1/colleges/",
    #                            data={'name': "TestName", 'location': "TestPlace",
    #                                  'acronym': "TEST", 'contact': "test@test.test"})
    #     self.assertEqual(result.status_code, status.HTTP_201_CREATED)
    #
    # def test_delete_college_id_valid(self):
    #     college_max_id = College.objects.all().order_by("-id")[0]
    #     result = requests.delete("http://127.0.0.1:8000/onlineapp/api/v1/colleges/"+college_max_id)
    #     self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)
    #
    # def test_delete_all_college_invalid(self):
    #     result = requests.delete("http://127.0.0.1:8000/onlineapp/api/v1/colleges/")
    #     self.assertEqual(result.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)