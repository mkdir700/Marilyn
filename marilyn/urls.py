"""marilyn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from options.views import OptionViewSet
from contents.views import ContentsViewSet
from users.views import UserViewSet
from groups.views import GroupViewSet
from metas.views import MetaViewSet
from attachments.views import AttachmentViewSet
from links.views import LinkViewSet
from comments.views import CommentViewSet

router = routers.DefaultRouter()
router.register('options', OptionViewSet, basename='options')
router.register('contents', ContentsViewSet, basename='contents')
router.register('groups', GroupViewSet, basename='groups')
router.register('users', UserViewSet, basename='users')
router.register('metas', MetaViewSet, basename='metas')
router.register('attachments', AttachmentViewSet, basename='attachments')
router.register('links', LinkViewSet, basename='links')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title="Marilyn接口调试")),
    # re_path('^api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
