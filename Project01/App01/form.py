from django import forms
from .models import Student, Course

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'courses': forms.CheckboxSelectMultiple()
        }
        labels = {
            'pincode': "asd",
            'courses': "Select any number of courses:-"
        }
        error_message = {
            'cname': {
                "max_length": "Length of Course name is too long..!!"
            }
        }

    # def __init__(self, *args, **kwargs):
        # super(StudentRegisterForm, self).__init__(*args, **kwargs)
        # #self.fields['courses'].queryset = Course.objects.all()
        # #self.fields['courses'].widget = forms.CheckboxSelectMultiple()
        # self.fields['courses'].label_from_instance = lambda obj: obj.cname


class CourseRegisterForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'



