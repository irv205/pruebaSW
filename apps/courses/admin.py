from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'previous', 'next', 'is_active')
    search_fields = ('id', 'title')

@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'description', 'previous', 'next', 'is_active')
    search_fields = ('id', 'course')

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'question', 'type', 'score', 'is_active')
    search_fields = ('id', 'lesson')

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'options', 'answer', 'is_active')
    search_fields = ('id', 'question')