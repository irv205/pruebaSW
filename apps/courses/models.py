import os
from django.db import models
from common.baseModel import BaseModels

# Create your models here.
class Course(BaseModels):

    title = models.CharField(max_length=100)
    previous = models.ForeignKey('self', related_name='previous_course', on_delete=models.SET_NULL, blank=True, null=True)
    next = models.ForeignKey('self', related_name='next_course', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class Lesson(BaseModels):

    course = models.ForeignKey(Course, related_name='lesson', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=600, blank=True, null=True)
    passing_score = models.PositiveIntegerField(default=1)
    previous = models.ForeignKey('self', related_name='previous_lesson', on_delete=models.SET_NULL, blank=True, null=True)
    next = models.ForeignKey('self', related_name='next_lesson', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

class Question(BaseModels):

    TYPE_ANSWER = (
        (1, ("Boolean")),
        (2, ("Multiple choice where only one answer is correct")),
        (3, ("Multiple choice where more than one answer is correct")),
        (4, ("Multiple choice where more than one answer is correct and all of them must be answered correctly")),
    )

    lesson = models.ForeignKey(Lesson, related_name='question', on_delete=models.CASCADE, blank=True, null=True)
    question = models.TextField()
    type = models.IntegerField(choices=TYPE_ANSWER, verbose_name='type_question', blank=True, null=True)
    score = models.IntegerField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class Answer(BaseModels):

    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE, blank=True, null=True)
    options = models.JSONField()
    answer = models.JSONField()

    def __str__(self):
        return self.question.title

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
