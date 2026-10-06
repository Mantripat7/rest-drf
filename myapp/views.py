from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User

def home(request):
    fruits = ["apple", "cherry"]
    context = {
        
        "fruits":fruits
    }
    return render(request, "index.html", context)

def about(request):

    return render(request, "about.html")





class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

