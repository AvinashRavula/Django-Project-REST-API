from django.urls import path

from todolist.rest_api.todo_api import TodoAPI

urlpatterns = [
    path('api/v1/todolist/', TodoAPI.as_view(), name="todolist_rest_api"),
]