from django.contrib import admin
from .models import User, UserProfile, UserProject, Course
# Register your models here.


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserProject)
admin.site.register(Course)
