from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='students/images')
    roll = models.IntegerField()
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)


class Course(models.Model):
    cname = models.CharField(max_length=100)
    max_marks = models.DecimalField(max_digits=6, decimal_places=2)
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return f"{self.cname}"
