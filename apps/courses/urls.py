from django.shortcuts import render
from django.urls import path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'get-all-courses', views.GetAllCoursesView, basename='get-all-courses')
router.register(r'get-courses', views.CourseView, basename='Courses')
router.register(r'get-lessons', views.LessonView, basename='lessons')
router.register(r'get-questions', views.QuestionView, basename='questions')
router.register(r'get-answers', views.AnswerView, basename='answers')

urlpatterns = [
    path('courses', views.CrudCourseView.as_view()),
    re_path(r'^courses/(?P<pk>[0-9]+)/$', views.CrudCourseView.as_view()),
    path('lessons', views.CrudLessonView.as_view()),
    re_path(r'^lessons/(?P<pk>[0-9]+)/$', views.CrudLessonView.as_view()),
    path('questions', views.CrudQuestionView.as_view()),
    re_path(r'questions/(?P<pk>[0-9]+)/$', views.CrudQuestionView.as_view()),
    path('answers', views.CrudAnswerView.as_view()),
    re_path(r'answers/(?P<pk>[0-9]+)/$', views.CrudAnswerView.as_view()),
    path('available-courses', views.GetAvailableCourses.as_view()),
    path('available-lessons', views.GetAvailableLesson.as_view()),
]

urlpatterns += router.urls