from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from onlineapp.models import College, Student
from onlineapp.serializers.StudentDetailSerializer import StudentDetailSerializer
from onlineapp.serializers.StudentSerializer import StudentSerializer
from onlineapp.serializers.CollegeSerializer import CollegeSerializer


@api_view(['GET', 'POST'])
def college_get_post_request_handler(request):
    if request.method == 'GET':
        college = College.objects.all()
        serializer = CollegeSerializer(college, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def college_get_put_delete_request_handler(request, pk):
    """
    Retrieve, update or delete a code college.
    """
    try:
        college = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CollegeSerializer(college)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        college.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StudentGetPostRequestHandlerView(APIView):
    # @api_view(['GET'])
    def get(self, request, *args, **kwargs):
        college = get_object_or_404(College, **kwargs)
        student = Student.objects.all().filter(college=college)
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = dict()
        data.update(request.data)
        data['college'] = kwargs.get('pk')
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentGetPutDeleteRequestHandlerClass(APIView):

    def get(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student =  get_object_or_404(Student, pk=kwargs.get('pk'))
        serializer = StudentDetailSerializer(student)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student = get_object_or_404(Student, pk=kwargs.get('pk'))
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student = get_object_or_404(Student, pk=kwargs.get('pk'))
        serializer = StudentDetailSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def student_get_post_request_handler(request):
#     if request.method == 'GET':
#         college = get_object_or_404(College, pk=request.GET.get('college_id'))
#         student = Student.objects.all().filter(college=college)
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
