from django.urls import path, include
from .views import *

from rest_framework_nested import routers
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

# from rest_framework import routers

router = routers.DefaultRouter()
router.register("posts", PostViewSet, basename="posts")


post_router = routers.NestedDefaultRouter(router, "posts", lookup="post")
post_router.register("comments", CommentViewSet, basename="post-comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(post_router.urls)),
]

documentation = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
urlpatterns += documentation
