from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from blog.models import *

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "first_name",
            "last_name",
        ]


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "parent",
            "author",
            "content",
            "published_date",
            "liked",
            "time_difference",
            "children",
        ]

    def get_children(self, obj):
        """
        Fetch child comments for the current comment object.
        """
        children = obj.get_children()
        return CommentSerializer(children, many=True).data


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "image",
            "excerpt",
            "content",
            "published_date",
            "time_difference",
            "status",
            "category",
            "author",
            "favorite",
            "liked",
            "disliked",
            "comments",
        ]
