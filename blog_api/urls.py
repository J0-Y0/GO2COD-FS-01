from django.urls import path, include
from .views import *

# from rest_framework_nested import routers
from rest_framework import routers

router = routers.DefaultRouter()

router.register("posts", PostViewSet, basename="posts")
router.register("comments", CommentViewSet, basename="comments")
urlpatterns = router.urls
