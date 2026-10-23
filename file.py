import os 
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproj.settings')
django.setup()



from myapp.models import *

# courses = Course.objects.order_by('-name').all()
# # user = User.objects.filter(email = "abcd@gmail.com").first()
# # user = User.objects.exclude(email = "abcd@gmail.com").first()

# for course in courses:
#     print(course.name)




# user = UserProfile.objects.order_by('-matriculation_marks')[:2]


# for u in user:
#     print(u.user.name, u.dob, u.matriculation_marks)
 
# users= User.objects.first().update(name= 'djkfbj')

# user= User.objects.values_list()
# print(users)
# print(user)


# users = User.objects.filter(projects__isnull=False).prefetch_related('projects').distinct()

# for u in users:
#     print(u.name)
#     for project in  u.projects.all():
#         print(project.name)

# user = User.objects.filter(name__startswith="A")
# print(user)    
        





# courses = Course.objects.prefetch_related('user')
# for course in courses:
#     print(course.name)
#     for u in course.user.all():
#         print(u.name, u.email)
#     print("--------")



from django.db.models import Q, Avg, Count, Max, Min, Sum

# course = Course.objects.aggregate(maxFees=Avg('price'))
# courses = Course.objects.annotate(active=Count('price'))
# for course in courses:
#     print(course.name, course.active)


# courses = Course.objects.filter(Q(price__gte=6000) ,  Q(name__startswith='P'))
# for c in courses:
#     print(c.name)

# users = User.objects.filter(roll__range=(3,5))
# # users = User.objects.filter(name__isnull=False)
# for u in users:
#     print(u.email)
import datetime
start = datetime.date(2005,12,12)
end = datetime.date(2026,12,12)
user = UserProfile.objects.filter(dob__range=(start, end))
print(user)
# for u in user:
#     print(u.dob, u.user.email)




