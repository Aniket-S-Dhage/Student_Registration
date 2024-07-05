from django.contrib import admin
from .models import Student, Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'address', 'pincode']


admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['cname']

admin.site.register(Course, CourseAdmin)