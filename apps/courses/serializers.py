from rest_framework import serializers
from . import models

class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ('id', 'question', 'options', 'answer', 'is_active')

class QuestionSerializers(serializers.ModelSerializer):
    answer = AnswerSerializers(many = True, required = False)

    class Meta:
        model = models.Question
        fields = ('id', 'lesson', 'question', 'type', 'score', 'is_active', 'answer')

class LessonSerializers(serializers.ModelSerializer):
    question = QuestionSerializers(many = True, required = False)

    class Meta:
        model = models.Lesson
        fields = ('id', 'course', 'title', 'description', 'passing_score','previous', 'next', 'is_active', 'question')

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'title', 'previous', 'next', 'is_active')

####################################################################################################

class GetCourseSerializers(serializers.ModelSerializer):
    lesson = LessonSerializers(many=True, required = False)

    class Meta:
        model = models.Course
        fields = ('id', 'title', 'previous', 'next', 'is_active', 'lesson')