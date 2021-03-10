from django.shortcuts import render

from rest_framework import status, viewsets, exceptions, permissions
from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view, action
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from common.pagination import PageNumberPagination
from django.http import HttpResponse
from . import serializers, models
from django.conf import settings

from apps.user.models import User
import json

class UserView(viewsets.ModelViewSet):

    model = models.User
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.UserSerializers

    def get_queryset(self):
        queryset = self.model.objects.all()
        return self.filter(queryset)

    def filter(self, queryset):
        
        kwargs = self.request.GET
        id = kwargs.get('id', None)
        type = kwargs.get('type', None)
        email = kwargs.get('email', None)
        is_active = kwargs.get('is_active', None)

        if id:
            queryset = queryset.filter(
                id = id
            )
        if email:
            queryset = queryset.filter(
                email = email
            )
        if is_active:
            queryset = queryset.filter(
                is_active = is_active
            )
        if type:
            queryset = queryset.filter(
                type = type
            )

        return queryset        

class GetMe(APIView):
    
    def get(self, request):
        user = request.user
        serializer = serializers.UserSerializers(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterUserView(CreateAPIView):

    permission_classes = ( )
    serializer_class = serializers.UserSerializers

    def get_token_auth(self, user):

        refresh_token = RefreshToken.for_user(user)
        tkn = {
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token)
        }
        return tkn

    def post(self, request):

        data = self.request.data

        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        full_name = data['full_name']
        type = self.request.data.get('type', None)
        
        if type == None:
            type = 3

        verify_email = User.objects.filter(email = email).exists()

        if verify_email:
            return Response({'Error': 'This email is already registered'}, status=status.HTTP_401_UNAUTHORIZED)

        if password != confirm_password:
            return Response({'Password': "Password fields didn't match."}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.create(
            username = email,
            email = email,
            full_name = full_name,
            type = type
        )

        user.set_password(password)
        user.save()

        return Response(self.get_token_auth(user), status=status.HTTP_201_CREATED)

class UpdateUserView(APIView):

    permission_classes = (permissions.IsAuthenticated, )

    def put(self, request, pk):

        password = request.data.get('password', None)
        confirm_password = request.data.get('confirm_password', None)
        email = request.data.get('email', None)

        if email:

            verify_email = User.objects.filter(email = email).exists()

            if verify_email:
                return Response({'Error': 'This email is already registered'}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.get(pk = pk)
        user.username = email
        serializer = serializers.UserUpdateSerializers(
            user, data=request.data
        )

        if serializer.is_valid():
            serializer.save()

        if password:

            if password != confirm_password:
                return Response({'Password': "Password fields didn't match."}, status=status.HTTP_401_UNAUTHORIZED)
            
            user.set_password(password)
            user.save()
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class getauthenticationtokenView(TokenObtainPairView):
    serializer_class = serializers.getauthenticationtokenSerializers
