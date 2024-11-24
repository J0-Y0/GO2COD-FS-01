from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from blog.models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        # fields = [
        #     "title",
        #     "comments",
        # ]
