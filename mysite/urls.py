"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rental.views import UserViewSet, PostViewSet, CommentViewSet, TodoViewSet, PhotoViewSet, AlbumsViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet, 'user')
router.register(r'post', PostViewSet, 'post')
router.register(r'comment', CommentViewSet,'comment')
router.register(r'album', AlbumsViewSet,'album')
router.register(r'photo', PhotoViewSet,'photo')
router.register(r'todo', TodoViewSet,'todo')

urlpatterns = [

    path('', include(router.urls)),

]
