from django.shortcuts import render

from rest_framework import status, viewsets, permissions
from rest_framework.views import Response, APIView

from django.http import HttpResponse
from django.conf import settings

from common.utils import UserAuth
from apps.user.models import User
from apps.assignCourse.models import StudentCourse, StudentQuestions

from . import serializers, models
from apps.courses.models import Answer

import json

# Create your views here.
class GetAllCoursesView(viewsets.ModelViewSet):
    model = models.Course
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.GetCourseSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):
        
        kwargs = self.request.GET
        id = kwargs.get('id', None)
        title = kwargs.get('title', None)

        queryset = queryset.filter(
            is_active = True,
        )

        if id:
            queryset = queryset.filter(
                id = id
            )

        if title:
            queryset = queryset.filter(
                title = title
            )
        
        return queryset  

class CourseView(viewsets.ModelViewSet):

    model = models.Course
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.CourseSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):
        
        kwargs = self.request.GET
        id = kwargs.get('id', None)
        title = kwargs.get('title', None)

        queryset = queryset.filter(
            is_active = True
        )

        if id:
            queryset = queryset.filter(
                id = id
            )

        if title:
            queryset = queryset.filter(
                title = title
            )
        
        return queryset

class CrudCourseView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        data = self.request.data

        serializer = serializers.CourseSerializers(data=data)

        if serializer.is_valid():
            serializer.save(
                owner = self.request.user,
                is_active = True,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_200_OK)

    def put(self, request, pk):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        course = models.Course.objects.get(pk=pk)
        data = self.request.data

        serializer = serializers.CourseSerializers(course, data=data, partial=True)
        
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

        course = models.Course.objects.get(pk=pk)
        course.is_active = False
        course.save()
        return Response({'message': 'Removed'}, status=status.HTTP_200_OK)

class LessonView(viewsets.ModelViewSet):

    model = models.Lesson
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.LessonSerializers

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

class CrudLessonView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        data = self.request.data

        serializer = serializers.LessonSerializers(data=data)

        if serializer.is_valid():
            serializer.save(
                owner = self.request.user,
                is_active = True,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_200_OK)

    def put(self, request, pk):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        lesson = models.Lesson.objects.get(pk=pk)
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

        lesson = models.Lesson.objects.get(pk=pk)
        lesson.is_active = False
        lesson.save()
        return Response({'message': 'Removed'}, status=status.HTTP_200_OK)

class QuestionView(viewsets.ModelViewSet):

    model = models.Question
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.QuestionSerializers

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

class CrudQuestionView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        data = self.request.data

        serializer = serializers.QuestionSerializers(data=data)

        if serializer.is_valid():
            serializer.save(
                owner = self.request.user,
                is_active = True,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_200_OK)

    def put(self, request, pk):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        question = models.Question.objects.get(pk=pk)
        data = self.request.data

        serializer = serializers.QuestionSerializers(question, data=data, partial=True)
        
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

        question = models.Question.objects.get(pk=pk)
        question.is_active = False
        question.save()
        return Response({'message': 'Removed'}, status=status.HTTP_200_OK)

class AnswerView(viewsets.ModelViewSet):

    model = models.Answer
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.AnswerSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):
        
        kwargs = self.request.GET
        id = kwargs.get('id', None)
        question = kwargs.get('question', None)

        queryset = queryset.filter(
            is_active = True
        )

        if id:
            queryset = queryset.filter(
                id = id
            )

        if question:
            queryset = queryset.filter(
                question = question
            )
        
        return queryset

class CrudAnswerView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        data = self.request.data

        question_id = data['question']

        has_an_answer = models.Answer.objects.filter(question = question_id).exists()

        if has_an_answer:
            return Response({'message': 'This question already has an answer'}, status=status.HTTP_200_OK)

        serializer = serializers.AnswerSerializers(data=data)

        if serializer.is_valid():
            serializer.save(
                owner = self.request.user,
                is_active = True,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_200_OK)

    def put(self, request, pk):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        answer = models.Answer.objects.get(pk=pk)
        data = self.request.data

        serializer = serializers.AnswerSerializers(answer, data=data, partial=True)
        
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

        answer = models.Answer.objects.get(pk=pk)
        answer.is_active = False
        answer.save()
        return Response({'message': 'Removed'}, status=status.HTTP_200_OK)

class GetAvailableCourses(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        data = self.request.data
        user = data['user']

        courses_by_user = StudentCourse.objects.filter(user=user).values_list('course', flat=True)

        courses_ids = models.Course.objects.filter(is_active = True).exclude(id__in = courses_by_user).values_list('id', flat=True)
        
        courses = models.Course.objects.filter(id__in = courses_ids)
        
        serializer = serializers.CourseSerializers(courses, many = True)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetAvailableLesson(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        access = UserAuth(request.user.id)
        if access['access'] == False:
            return Response({'message':access['details']}, status=status.HTTP_200_OK)

        data = self.request.data
        user = data['user']

        lesson_by_user = StudentCourse.objects.filter(user=user).values_list('lesson', flat=True)

        lessons_ids = models.Lesson.objects.filter(is_active = True).exclude(id__in = lesson_by_user).values_list('id', flat=True)
        
        lessons = models.Lesson.objects.filter(id__in = lessons_ids)
        
        serializer = serializers.LessonSerializers(lessons, many = True)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)  