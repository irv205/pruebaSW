from django.shortcuts import render

from rest_framework import status, viewsets, permissions
from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.conf import settings

from common import utils
# from common.utils import UserAuth, VerificationStudent, CheckCourseForStudent
from apps.user.models import User
from apps.courses.models import Course, Lesson, Question, Answer

from . import serializers, models
from . import utils as tls

import json

# Create your views here.
class GetStudentCoursesView(viewsets.ModelViewSet):

    model = models.StudentCourse
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.StudentCourseSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):
        
        kwargs = self.request.GET
        id = kwargs.get('id', None)
        course = kwargs.get('course', None)

        queryset = queryset.filter(
            is_active = True
        )

        if id:
            queryset = queryset.filter(
                id = id
            )

        if course:
            queryset = queryset.filter(
                course = course
            )
        
        return queryset

class CourseAssignmentStudent(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        data = self.request.data
        course_id = data['course']
        user_id = data['user']
        lesson_id = data['lesson']

        validation = utils.VerificationStudent(user_id)
        if validation['access'] == False:
            return Response({'message':validation['details']}, status=status.HTTP_200_OK)

        validation = utils.CheckCourseForStudent(course_id, user_id)
        if validation['access'] == False:
            return Response({'message':validation['details']}, status=status.HTTP_200_OK)

        validation = utils.CheckLessonsForCuourses(lesson_id, course_id)
        if validation['access'] == False:
            return Response({'message':validation['details']}, status=status.HTTP_200_OK)

        serializer = serializers.StudentCourseSerializers(data=data)

        if serializer.is_valid():
            course = serializer.save(
                owner = self.request.user,
                is_active = True,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_200_OK)

    def put(self, request, pk):

        lesson = models.lesson.objects.get(pk=pk)
        data = self.request.data

        serializer = serializers.LessonSerializers(lesson, data=data, partial=True)

        if serializer.is_valid():
            serializer.save(
                owner = self.request.user,
                is_active = True,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request, pk):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        assigned_course = models.StudentCourse.objects.get(pk=pk)
        assigned_course.is_active = False
        assigned_course.save()
        return Response({'message': 'Removed'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def AnswerQuestionsforStudent(request):

    permission_classes = (permissions.IsAuthenticated,)

    data = request.data
    user_id = data['user']
    questions = data['question']
    answers = data['answer']
    lesson_id = data['lesson']
    lesson = Lesson.objects.filter(id = lesson_id).first()
    course = Course.objects.filter(id = lesson.course).first()

    validation = utils.CheckLessonForStudent(lesson_id, user_id)
    if validation['access'] == False:
        return Response({'message':validation['details']}, status=status.HTTP_200_OK)

    validation = tls.AnswersAndQuestions(user_id, lesson_id, questions, answers)

    if validation['pass'] == False:

        return Response({'message': 'It seems that you failed in some question'})

    if validation['pass'] == True:

        if lesson.next == None:
            return Response({'message': 'Congratulations, you have finished all the lessons of the course'})

        else:  
            return Response({'message': 'You can go to the next lesson'})


class GetStudentQuestionsView(viewsets.ModelViewSet):

    model = models.StudentQuestions
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.StudentQuestionsSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):
        
        kwargs = self.request.GET
        id = kwargs.get('id', None)
        lesson = kwargs.get('lesson', None)

        queryset = queryset.filter(
            is_active = True
        )

        if id:
            queryset = queryset.filter(
                id = id
            )

        if lesson:
            queryset = queryset.filter(
                lesson = lesson
            )
        
        return queryset
