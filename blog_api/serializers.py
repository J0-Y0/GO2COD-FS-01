from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from blog.models import *


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

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


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

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
            "status",
            "category",
            "author",
            "favorite",
            "liked",
            "disliked",
            "comments",
        ]
