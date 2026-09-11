from . models import *
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

#------------------------------------------------------------------------>
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserBaseSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField()


class UserAuthSerializer(UserBaseSerializer):
    pass


class UserCreateSerializer(UserBaseSerializer):

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')