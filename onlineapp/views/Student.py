from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from onlineapp.models import Student, College
from onlineapp.views.Mocktest1 import MocktestForm


class StudentListView(LoginRequiredMixin,DetailView):
    login_url = 'onlineapp:login_html'
    model = Student
    template_name = 'student_list.html'

    def get_context_data(self, **kwargs):
        context = super(StudentListView,self).get_context_data(**kwargs)
        return context


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'dob', 'college', 'college_name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Student Name'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control'}),
            'db_folder' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Student DB Folder'}),
            'dropped_out': forms.CheckboxInput(),
        }


class AddStudentView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = 'onlineapp:login_html'
    permission_required = "onlineapp.add_student"
    permission_denied_message = "You dont have permission to add a student."
    form_class = StudentForm
    template_name = 'add_student.html'
    #success_url = reverse_lazy('onlineapp:colleges_list_html')

    def get_context_data(self, **kwargs):
        context = super(AddStudentView,self).get_context_data(**kwargs)
        test_form = MocktestForm
        context.update({
            'title' : "Add Student",
            'student_form' : context.get('form'),
            'test_form' : test_form
        })
        return context

    def post(self, request, *args, **kwargs):
        college = get_object_or_404(College, pk = kwargs.get('college_id'))
        student_form = StudentForm(request.POST)
        test_form = MocktestForm(request.POST)

        if student_form.is_valid():
            student = student_form.save(commit=False)
            student.college = college
            # student.college_name = ""
            student.save()

            if test_form.is_valid():
                test = test_form.save(commit=False)
                test.total = sum(test_form.cleaned_data.values())
                test.student = student
                test.save()
                return render(
                    request,
                    template_name='college_list.html',
                    context={
                        'college_list': College.objects.values('id', 'name', 'acronym'),
                    }
                )



class UpdateStudentView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = 'onlineapp:login_html'
    permission_denied_message = "You dont have permissoin to change the student details."
    permission_required = "onlineapp.change_student"
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'

    def get_context_data(self, **kwargs):
        # import ipdb
        # ipdb.set_trace()
        student = get_object_or_404(Student, pk = self.kwargs.get('pk'))
        context = super(UpdateStudentView, self).get_context_data(**kwargs)
        try:
            test_form = MocktestForm(instance=student.mocktest1)
        except Exception:
            test_form = MocktestForm

        context.update({
            'student_form': context.get('form'),
            'test_form': test_form
        })
        return context

    def post(self, request, *args, **kwargs):
        # college = get_object_or_404(College, pk=kwargs.get('college_id'))
        college = get_object_or_404(College, pk=kwargs.get('college_id'))
        student = get_object_or_404(Student, pk=kwargs.get('pk'))

        student_form = StudentForm(request.POST, instance=student)
        test_form = MocktestForm(request.POST, instance=student.mocktest1)

        if student_form.is_valid() and test_form.is_valid():
            student = student_form.save(commit=False)
            student.college = college
            student.save()
            # import ipdb
            # ipdb.set_trace()
            test = test_form.save(commit=False)
            test.total = sum(test_form.cleaned_data.values())
            test.student = student
            test.save()
            return render(
                request,
                template_name='college_list.html',
                context={
                    'college_list': College.objects.values('id', 'name', 'acronym'),
                }
            )


class DeleteStudentView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = 'onlineapp:login_html'
    permission_required = "onlineapp.delete_student"
    permission_denied_message = "You dont have permission to delete a student."
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('onlineapp:colleges_list_html')

    def get(self, request, *args, **kwargs):
        if kwargs:
            get_object_or_404(self.model, **kwargs).delete()