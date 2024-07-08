from django import forms
from .models import Student, Course

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'courses': forms.CheckboxSelectMultiple()
        }


class CourseRegisterForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

