from django.urls import path
from .views import StudentListView, StudentRegisterView, CourseRegisterView


urlpatterns = [
    path('', StudentListView.as_view(), name='showStudent'),
    path('register/', StudentRegisterView.as_view(), name='registerStudent'),
    path('addcourse/', CourseRegisterView.as_view(), name='registerCourse'),
]
