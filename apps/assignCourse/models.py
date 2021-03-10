import os
from django.db import models
from common.baseModel import BaseModels
from apps.user.models import User
from apps.courses.models import Course, Lesson, Question


# Create your models here.
class StudentCourse(BaseModels):

    user = models.ForeignKey(User, related_name='student_course', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, related_name='student_course', on_delete=models.CASCADE, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, related_name='student_lesson', on_delete=models.CASCADE, blank=True, null=True)
    students_score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name = 'Studen Course'
        verbose_name_plural = 'Student Courses'

class StudentQuestions(BaseModels):

    user = models.ForeignKey(User, related_name='student_question', on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Question, related_name='question_student', on_delete=models.CASCADE, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, related_name='taking_lesson', on_delete=models.CASCADE, blank=True, null=True)
    correct_question = models.BooleanField(default=False)

    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name = 'Studen Question'
        verbose_name_plural = 'Student Questions'
