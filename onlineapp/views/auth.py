from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'})
    )
    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the password'})
    )


class SignUpForm(forms.Form):
    first_name= forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the first name'})
    )
    last_name = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the last name'})
    )
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the username'})
    )
    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter the password'})
    )


class SignUpFormView(View):

    def get(self, request):
        form = SignUpForm()
        return render(
            request,
            template_name= 'signup_form.html',
            context= {'form' : form,'title' : "Signup"}
        )

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('onlineapp:colleges_list_html')
            else:
                messages.error(request,"Invalid Credentials")



class LoginFormView(View):

    def get(self, request):

        if request.user.is_authenticated:
            return redirect('onlineapp:colleges_list_html')

        form = LoginForm()
        return render(
            request,
            template_name= 'login_form.html',
            context= {'form' : form,'title' : "login",'link': "onlineapp:signup_html",'link_name' : "SignUp"}
        )

    def post(self, request):
        form = LoginForm(request.POST)
        # import ipdb
        # ipdb.set_trace()
        if form.is_valid():

            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('onlineapp:colleges_list_html')
            else:
                messages.error(request, "Invalid Credentials")

        return HttpResponse("Error")



def logout_user(request):
    logout(request)
    import ipdb
    return redirect('onlineapp:login_html')