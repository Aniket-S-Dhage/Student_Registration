from django.views import View
from .models import Student
from django.shortcuts import render, redirect
from .form import StudentRegisterForm


class StudentListView(View):
    def get(self, request):
        students = Student.objects.prefetch_related('courses')
        context = {"students": students}
        template_name = 'app01/show.html'
        return render(request, template_name, context)


class StudentRegisterView(View):
    def get(self, request):
        form = StudentRegisterForm()
        context = {"form": form}
        template_name = 'app01/register.html'
        return render(request, template_name, context)

    def post(self, request):
        form = StudentRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showStudent')
        return render(request, template_name='app01/register.html', context={"form":form})






