
import MySQLdb
import django , os, os.path
import click, requests
from bs4 import BeautifulSoup
import urllib.request
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "onlineproject.settings")
django.setup()
from openpyxl import load_workbook
from onlineapp.models import *
from django.db.models import *


def print_college_names():
    manager = College.objects
    querysets = College.objects.all()
    print(querysets)
    for queryset in querysets:
        print(queryset)


if __name__ == "__main__":
    print_college_names()