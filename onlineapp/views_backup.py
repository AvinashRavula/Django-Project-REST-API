import os
import urllib

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.shortcuts import redirect
from onlineapp.models import *
from django.template import loader


def get_html_data(url_or_file):
    html = ""
    if os.path.isfile(url_or_file):
        if not url_or_file.endswith(".html"):
            raise TypeError("Only HTML files can be processed")
        with open(url_or_file) as f:
            html = f.read()
    else:
        f = urllib.request.urlopen(
            url_or_file)
        html = f.read()
    return html


def index(request):
    #return redirect('D:/Avinash%20New/MissionRnD/Apps%20Course/htmllessons_1/html/html_lesson_01_structure.html')
    return HttpResponse(get_html_data("test.html"))



def college(request):
    queryset = College.objects.values('name','acronym')
    html = "<html><head><h1>Colleges</h1><style>td:hover{color:red;font-size:20px}</style></head><body><table border = 2 ><tr><th>College Name</th><th>College Acronym</th></tr>"
    # for data in queryset:
    #     html += "<tr><td>"+data[0]+"</td><td>"+data[1]+"</td></tr>"
    # resp = HttpResponse()
    # resp.write(html)
    # return resp
    context = {
        'college_list': queryset,
    }
    #template = loader.get_template('CollegeList.html')
    return render(request, 'CollegesList.html', queryset)


def students(request):
    queryset = College.objects.values('student__name','student__email','acronym')
    print(queryset)
    return render(request, 'list.html', {'set': queryset})

def single_student(request):
    q = request.GET.get('q',None)
    queryset = Student.objects.values().filter(id=q)
    print(queryset)
    return render(request, 'list.html',{'set':queryset})

def students_with_mock_link(request):
    queryset = College.objects.values('student__name', 'student__email', 'acronym', 'student__mocktest1__total')
    context = {
        'college_list': queryset,
    }
    return render(request, 'student_mock.html', {'student_list': queryset})


def student_details_of_a_college(request):
    req_acronym = request.GET.get('q',None)
    if isinstance(req_acronym,str):
        queryset = Mocktest1.objects.values('student__name', 'student__email', 'total').filter(student__college__acronym=req_acronym).order_by('-total')
        if queryset.count() == 0:
            return render(request, 'Error_page.html', {'error': "Details not found"})
        context = {
            'student_list': queryset,
        }
        return render(request, 'student_acronym.html', {'student_list': queryset})
    else:
        return render(request, 'Error_page.html',{'error' : "Details not found"})



def session_view(request):
    request.session.setdefault('counter',0)
    request.session['counter'] += 1
    #request.session['counter'] = call_count + 1
    return render(request, 'Error_page.html', {'error': "Count = "+str(request.session['counter'])})


def raise_python_error(request):
    raise ValueError("Value error")


def redirect_page(request):
    return redirect("https://www.google.com")