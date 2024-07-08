from django.urls import path
from .views import StudentListView, StudentRegisterView


urlpatterns = [
    path('/2', StudentListView.as_view(), name='showStudent2'),
    path('register2/', StudentRegisterView.as_view(), name='registerStudent2')
]
