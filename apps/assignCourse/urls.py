from django.shortcuts import render
from django.urls import path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'get-student-courses', views.GetStudentCoursesView, basename='student-couses')
router.register(r'get-student-questions', views.GetStudentQuestionsView, basename='student-questions')

urlpatterns = [
    path('assignment-course', views.CourseAssignmentStudent.as_view()),
    re_path(r'^assignment-course/(?P<pk>[0-9]+)/$', views.CourseAssignmentStudent.as_view()),
    path('answer-question', views.AnswerQuestionsforStudent),
]

urlpatterns += router.urls