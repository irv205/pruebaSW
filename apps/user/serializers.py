from rest_framework import serializers, validators
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . import models

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'type', 'full_name', 'email', 'photo','is_active')

class UserUpdateSerializers(serializers.ModelSerializer):

    email = serializers.EmailField(required=False)
    full_name = serializers.CharField(required=False)


    class Meta:
        model = models.User
        fields = ('id', 'type','full_name', 'email', 'photo','is_active')

class getauthenticationtokenSerializers(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token
