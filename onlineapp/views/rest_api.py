from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView



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
