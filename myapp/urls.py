from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet



router = DefaultRouter()

router.register('user', UserViewSet, basename="users")



urlpatterns = [

    path('api/', include(router.urls)),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
]