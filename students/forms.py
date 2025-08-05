from django import forms
from .models import student_details

class StudentForm(forms.ModelForm):
    class Meta:
        model = student_details
        fields = ['name', 'email','branch','bio']