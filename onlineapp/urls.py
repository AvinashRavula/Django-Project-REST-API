from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from onlineapp import views

from django.conf import settings
from django.conf.urls import include, url

from onlineapp.views import CollegeView, CollegeListView, CollegeDetailsView, AddCollegeView, AddStudentView, \
    UpdateCollegeView, DeleteCollegeView, UpdateStudentView, DeleteStudentView, SignUpForm, SignUpFormView, \
    LoginFormView, logout_user
from onlineapp.views.rest_api import college_get_put_delete_request_handler, college_get_post_request_handler, \
    StudentGetPostRequestHandlerView, StudentGetPutDeleteRequestHandlerClass

app_name = 'onlineapp'

urlpatterns = [
    # path('hello/', views.index),
    # path('college/',views.college),
    # path('studentssss/',views.students),
    # path('getstudent/',views.single_student),
    # path('student_mock/',views.students_with_mock_link),
    # path('student_acronym/',views.student_details_of_a_college),

    path('test_session/',views.session_view),
    path('test_python_error/',views.raise_python_error),
    path('test_python_error2/',views.raise_python_error),
    path('redirect/',views.redirect_page),

    path('colleges/',CollegeView.as_view(),name='colleges_html'),
    path('colleges_list/',CollegeListView.as_view(),name='colleges_list_html'),
    path('colleges_list/<int:pk>/',CollegeDetailsView.as_view(),name='colleges_details_list_html'),
    path('colleges_list/<str:acronym>/',CollegeDetailsView.as_view(),name='colleges_details_list_html2'),
    path('add_college/',AddCollegeView.as_view(), name = "add_college_html"),
    path('college/<int:pk>/delete', DeleteCollegeView.as_view(),name="delete_college_html"),
    path('college/<int:pk>/edit', UpdateCollegeView.as_view(),name="edit_college_html"),
    path('student/<int:college_id>/add',AddStudentView.as_view(),name="add_student_html"),
    path('colleges/<int:college_id>/student/<int:pk>/edit',UpdateStudentView.as_view(),name="edit_student_html"),
    path('student/<int:pk>/delete',DeleteStudentView.as_view(),name="delete_student_html"),
    path('signup/', SignUpFormView.as_view(), name="signup_html"),
    path('login/', LoginFormView.as_view(), name="login_html"),
    path('logout/', logout_user, name="logout_html"),

    path('api/v1/colleges/<int:pk>',college_get_put_delete_request_handler,name="college_get_put_delete_rest_api"),
    path('api/v1/colleges/',college_get_post_request_handler,name="college_get_post_rest_api"),

    path('api/v1/colleges/<int:pk>/students/', StudentGetPostRequestHandlerView.as_view(), name="student_get_post_rest_api"),
    path('api/v1/colleges/<int:college_id>/students/<int:pk>', StudentGetPutDeleteRequestHandlerClass.as_view(), name="student_get_put_delete_rest_api"),


]