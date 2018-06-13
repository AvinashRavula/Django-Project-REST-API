import os, django
from onlineapp.models import *
import click
from openpyxl import load_workbook


os.environ.setdefault('DJANGO_SETTINGS_MODULE', "onlineproject.settings")
django.setup()



@click.group()
@click.pass_context
def cli(ctx):
    pass


def isHTML(filename):
    return filename.endswith(".html")


def isExcelFile(filename):
    return filename.endswith(".xlsx") or filename.endswith('xls')
