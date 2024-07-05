from django.views import View
from .models import Student, Course
from django.shortcuts import render, redirect
from .form import StudentRegisterForm, CourseRegisterForm


class StudentListView(View):
    def get(self, request):
        students = Student.objects.prefetch_related('courses')      ##Prefetch_related will reduce db queries by fetching related object data rather than lazy_loading
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



class CourseRegisterView(View):
    def get(self, request):
        form = CourseRegisterForm()
        template_name= 'app01/add_courses.html'
        context = {"form": form}
        return render(request, template_name, context)

    def post(self, request):
        form = CourseRegisterForm()
        if request.method == 'POST':
            form = CourseRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("showStudent")
        template_name = 'app01/add_courses.html'
        context= {"form": form}
        return render(request, template_name, context)





