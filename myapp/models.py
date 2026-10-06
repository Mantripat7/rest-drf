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


