from django.urls import path # type: ignore
from .import views



urlpatterns = [
    path('', views.students, name='students_list'),  # This will point to the 'students' view
]