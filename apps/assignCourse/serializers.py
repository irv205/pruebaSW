from rest_framework import serializers
from apps.courses.serializers import CourseSerializers, LessonSerializers
from . import models

class StudentCourseSerializers(serializers.ModelSerializer):
    course = CourseSerializers(many = False, required=False)
    lesson = LessonSerializers(many = False, required=False)

    class Meta:
        model = models.StudentCourse
        fields = ('id', 'user', 'course', 'lesson', 'students_score')

class StudentQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.StudentQuestions
        fields = ('id', 'user', 'question', 'lesson', 'correct_question')
