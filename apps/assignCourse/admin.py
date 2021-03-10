from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'lesson', 'students_score')
    search_fields = ('id', 'user', 'course', 'lesson')

@admin.register(models.StudentQuestions)
class StudentQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'lesson', 'correct_question')
    search_fields = ('id', 'user', 'lesson')
    