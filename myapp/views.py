from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User, UserProfile, Course
from django.shortcuts import get_object_or_404
import datetime
from django.core.mail import send_mail
import random, string
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    try:
        if request.session["user"]:
            user = User.objects.filter(email = request.session["user"]).first()
            username = user.name
    except:
        username = "Guest"
        user = None
    if request.GET.get("keyword"):
        key =  request.GET.get("keyword")
        courses = Course.objects.filter(name__icontains=key)
    else:
        key = None
        courses = Course.objects.all()
    paginator = Paginator(courses, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "user":user,
        "courses": page_obj,
        "username":username,
        "key":key,
        "courses_count": Course.objects.count()

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
        messages.success(request, "User account created successfully")
        return redirect('login')

    return render(request, "register.html")




def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(email = email).first()
        if not user:
            messages.warning(request, "User with this email does not exist")
            return redirect('login')

        if not user.password == password:
            messages.error(request, "Password is incorrect")
            return redirect('login')

        
        request.session["user"] = user.email
        messages.success(request, "Login successfully")
        return redirect('home')

    return render(request, "login.html")





def profile(request):
    if not request.session.get("user"):
        return redirect("login")
    
    curruser = User.objects.filter(email = request.session["user"]).first()
    curr_profile = UserProfile.objects.filter(user = curruser).first()
    
        
        
    
    if request.method == "POST":

        if not curr_profile:
            curruser.name = request.POST.get("name")
            curruser.address = request.POST.get("address")
            dob =  request.POST.get("dob") 
            matriculation_marks = request.POST.get("marks", "0.00")
            
            new_profile = UserProfile.objects.create(
                dob = dob,
                matriculation_marks=matriculation_marks,
                user = curruser
            )
            if request.FILES.get("pic"):
                pic = request.FILES.get("pic")
                new_profile.pic = pic


       
            if request.FILES.get("docs"):
                docs = request.FILES.get("docs")
                new_profile.docs = docs 
            
            new_profile.save()
            curruser.save()
            messages.success(request, "New profile created.")
            return redirect('profile')

        
        # curruser.email = request.POST.get("email")
        curruser.name = request.POST.get("name")
        curruser.address = request.POST.get("address")
        curr_profile.dob =  request.POST.get("dob") 
        curr_profile.matriculation_marks = request.POST.get("marks")
        if request.FILES.get("pic"):
            curr_profile.pic = request.FILES.get("pic")
        if request.FILES.get("doc"):
            curr_profile.docs = request.FILES.get("docs")
        curruser.save()
        curr_profile.save()
        messages.warning(request, "Profile updated")
        return redirect("profile")

    return render(request, "profile.html", {"user":curruser, "profile":curr_profile })




def delete_profile(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('login')




def logout(request):
    request.session.flush()
    return redirect('login')



def reset_password(request):
    print("reset password")
    if request.method=="POST":
        
        email = request.POST.get("email")
        print(email)
        user = User.objects.filter(email = email).first()
        if not user:
            messages.error(request, "User does not exist with entered email.")
             
        else:
            # resest passsword send new password
            new_password = "".join(random.choices(string.ascii_letters,  k=8))
            send_mail(
                subject="Request for new password",
                message=f"Your new password for the website has been changed and now the current password is {new_password}.",
                from_email="openmaterial2@gmail.com",
                recipient_list=[user.email],
                fail_silently=False,  
            ) 
            user.password = new_password
            user.save()
            messages.success(request, "New password has been sent to your email.")
            
    return redirect('login')


def mycourse(request):
    if not request.session.get("user"):
        return redirect("login")
    
    user = User.objects.filter(email= request.session['user']).first()
    context = {
        "mycourses":user.courses.all()
    }
    return render(request, "mycourse.html", context)


from .forms import UserForm

def add_user(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_user')

    else:
        form = UserForm()

    return render(request, "add_user.html", {"form":form})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





