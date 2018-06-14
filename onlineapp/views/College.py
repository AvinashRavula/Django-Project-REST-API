from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import ModelForm
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy, resolve
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from onlineapp.models import College, Student, Mocktest1
from django.shortcuts import render, get_object_or_404, redirect

from onlineapp.serializer import OnlineappSerializer


class CollegeView(View):

    def get(self, request, *args, **kwargs):
        colleges = College.objects.values('id', 'name', 'acronym')
        import ipdb
        ipdb.set_trace()
        return render(
            request,
            template_name='college_list.html',
            context={
                'college_list': colleges,
            }
        )


class CollegeListView(LoginRequiredMixin, ListView):
    login_url = 'onlineapp:login_html'
    model = College
    template_name = 'college_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CollegeListView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Participating Colleges',
            'user_permissions': self.request.user.get_all_permissions(),
        })
        return context


class CollegeDetailsView(LoginRequiredMixin, DetailView):
    login_url = 'onlineapp:login_html'
    model = College
    template_name = 'college_details_list.html'

    def get_object(self, queryset=None):
        return get_object_or_404(College, **self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(CollegeDetailsView, self).get_context_data(**kwargs)
        # import ipdb
        college = context.get('college')
        students = list(
            college.student_set.values('id', 'name', 'email', 'mocktest1__total').order_by('-mocktest1__total'))
        # ipdb.set_trace()
        context.update({
            'title': 'Students of ' + college.name,
            'college_id': college.id,
            'college_name': college.name,
            'student_list': students,
            'user_permissions': self.request.user.get_all_permissions(),
        })
        return context


class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['id', 'student']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the College Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Location'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Acronym'}),
            'contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Location'})
        }


class AddCollegeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = 'onlineapp:login_html'
    permission_required = "onlineapp.add_college"
    permission_denied_message = "You dont have permission to add a college."
    form_class = CollegeForm
    template_name = 'add_college.html'
    success_url = reverse_lazy('onlineapp:colleges_list_html')

    def get_context_data(self, **kwargs):
        context = super(AddCollegeView, self).get_context_data(**kwargs)
        context.update({
            'title': "Add Student",
        })
        return context


class UpdateCollegeView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'onlineapp:login_html'
    permission_required = "onlineapp.change_college"
    permission_denied_message = "You dont have permission to edit the college details."
    model = College
    form_class = CollegeForm
    template_name = 'add_college.html'
    success_url = reverse_lazy('onlineapp:colleges_list_html')


class DeleteCollegeView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = 'onlineapp:login_html'
    permission_required = "onlineapp.delete_college"
    permission_denied_message = "You dont have permission to delete the college."
    model = College
    form_class = CollegeForm
    success_url = reverse_lazy('onlineapp:colleges_list_html')

    def get(self, request, *args, **kwargs):
        if kwargs:
            get_object_or_404(College, **kwargs).delete()


def CollegeDetails_Serializer(request, college_id):
    college = get_object_or_404(College,pk = college_id)
    serializer = OnlineappSerializer(college)
    # print(serializer.data)
    return JsonResponse(serializer.data)


@csrf_exempt
@api_view(['GET', 'POST'])
def college_serializer(request):
    if request.method == 'GET':
        college = College.objects.all()
        serializer = OnlineappSerializer(college, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OnlineappSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def college_detail_serializer(request, pk):
    """
    Retrieve, update or delete a code college.
    """
    try:
        college = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OnlineappSerializer(college)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OnlineappSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        college.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)