from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import CustomUserViewSet
from .views import CommentViewSet, PostViewSet

app_name = 'api'

router = DefaultRouter()

router.register("users", CustomUserViewSet, basename="users")
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path("", include(router.urls)),
    path("", include("djoser.urls")),
]
