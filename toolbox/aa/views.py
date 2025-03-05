from django.shortcuts import render
from .models import *
from django.views.generic import *

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = 'list_course.html'
    context_object_name = 'course'
