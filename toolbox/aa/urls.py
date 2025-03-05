from django.urls import path, include
from .views import *

urlpatterns = [
    path('course/',CourseListView.as_view(),name='course_list'),
    
]