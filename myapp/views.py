from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User
from django.shortcuts import get_object_or_404
 

def home(request):
    try:
        if request.session["user"]:
            user = User.objects.filter(email = request.session["user"]).first()
            username = user.name
    except:
        username = "Guest"
    
    context = {
        "user":user,
        
        "username":username
    }
    return render(request, "index.html", context)

def about(request):

    return render(request, "about.html")


def register(request):

    if request.method == "POST":
        form_email = request.POST.get("email")
        form_password = request.POST.get("password")

        users = User.objects.filter(email = form_email)
        if users:
            return HttpResponse("email already exist")


        max_roll = User.objects.order_by("-roll").first().roll
        max_roll+=1
        print(max_roll)


        User.objects.create(
            email = form_email,
            password = form_password,
            roll = max_roll
        )
        return HttpResponse("User account created successfully")

    return render(request, "register.html")




def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(email = email).first()
        if not user:
            return HttpResponse("User with this email does not exist")

        if not user.password == password:
            return HttpResponse("password is incorrect")

        
        request.session["user"] = user.email
        return redirect('home')

    return render(request, "login.html")



def profile(request):
    if not request.session.get("user"):
        return redirect("login")
    user = User.objects.filter(email = request.session["user"]).first()
    if request.method == "POST":
        user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.address = request.POST.get("address")
        user.save()
        return redirect("profile")

    return render(request, "profile.html", {"user":user})

def delete_profile(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('login')




def logout(request):
    request.session.flush()
    return redirect('login')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

