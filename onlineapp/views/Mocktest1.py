from django import forms

from onlineapp.models import Mocktest1


class MocktestForm(forms.ModelForm):
    class Meta:
        model = Mocktest1
        exclude = ['id', 'total', 'student']
        widgets = {
            'problem1' : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the problem1 Marks'}),
            'problem2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the problem2 Marks'}),
            'problem3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the problem3 Marks'}),
            'problem4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the problem4 Marks'})
        }
