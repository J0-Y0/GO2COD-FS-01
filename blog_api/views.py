from blog.models import Post, Comment
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer, CommentSerializer

from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    BasePermission,
    AllowAny,
    SAFE_METHODS,
    IsAuthenticated,
)


class PostAuthorPermission(BasePermission):
    message = "Action restricted to post author only"

    def has_object_permission(self, request, view, obj):
        # only author can see drafted poste
        if obj.status == "draft":
            return obj.author == request.user
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, PostAuthorPermission]

    def get_queryset(self):
        return Post.newManager.all()

    def get_object(self, queryset=None, **kwargs):
        slug = self.kwargs.get("pk")
        instance = get_object_or_404(Post, slug=slug)
        self.check_object_permissions(self.request, instance)
        return instance


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()
