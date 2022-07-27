from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet


app_name = 'api'
version_api = 'v1'

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path(f'{version_api}/', include(router.urls)),
    path(f'{version_api}/api-token-auth/', views.obtain_auth_token),
]
