from rest_framework import status, permissions
from rest_framework.response import Response

from onlineapp.models import College, Student
from onlineapp.serializers.StudentDetailSerializer import StudentDetailSerializer
from onlineapp.serializers.StudentSerializer import StudentSerializer
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class StudentGetPostRequestHandlerView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
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
        serializer = StudentDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentGetPutDeleteRequestHandlerClass(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student =  get_object_or_404(Student, pk=kwargs.get('pk'), college=college)
        serializer = StudentDetailSerializer(student)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student = get_object_or_404(Student, pk=kwargs.get('pk'),college=college)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student = get_object_or_404(Student, pk=kwargs.get('pk'), college=college)
        serializer = StudentDetailSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
