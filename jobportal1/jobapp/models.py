from django.db import models
from  django.db import  models
from django.contrib.auth.models import User
# Create your views here.
class profile1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class regmodel(models.Model):
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    dob=models.CharField(max_length=20)
    hq=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class reg2model(models.Model):
    cname=models.CharField(max_length=20)
    email=models.EmailField()
    job_title=models.CharField(max_length=20)
    work_type=models.CharField(max_length=20)
    exp=models.CharField(max_length=20)
    job_type=models.CharField(max_length=20)

class jobapplymodel(models.Model):
    company_name=models.CharField(max_length=20)
    designation=models.CharField(max_length=30)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    qualification=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=12)
    experience=models.CharField(max_length=30)
    resume=models.FileField(upload_to="jobapp/static")
