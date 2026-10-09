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
    path('signin/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout, name="logout"),
    path('delete/<int:id>', views.delete_profile, name="delete_profile"),
]