from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True)
    password = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    pic = models.ImageField(upload_to='user/user_profile/', null=True, blank=True)
    docs = models.FileField(upload_to='user/user_docs/', null=True, blank=True)
    matriculation_marks = models.DecimalField(max_digits=4, decimal_places=2)
    dob = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile of {self.user.name}"
    


class UserProject(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    link = models.URLField(unique=True)
    synopsis = models.FileField(upload_to='user/user_synopsis', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="projects",null=True, blank=True)

    def __str__(self):
        return f"{self.name} made by {self.user.name}" 
   


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField()
    price  = models.FloatField()
    img = models.ImageField(upload_to='course/img/',null=True, blank=True)
    user =  models.ManyToManyField(User, related_name="courses")

    def __str__(self):
        return self.name














