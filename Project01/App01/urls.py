from django.urls import path
from .views import StudentListView, StudentRegisterView


urlpatterns = [
    path('', StudentListView.as_view(), name='showStudent'),
    path('register/', StudentRegisterView.as_view(), name='registerStudent'),
]