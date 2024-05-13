from  django import forms
from  .models import *

class regform(forms.Form):
    uname=forms.CharField(max_length=20)
    email=forms.EmailField()
    dob=forms.CharField(max_length=20)
    hq=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)


class logform(forms.Form):
    email=forms.EmailField()
    pas=forms.CharField(max_length=20)


class reg2form(forms.Form):
    cname=forms.CharField(max_length=20)
    email=forms.EmailField()
    job_title=forms.CharField(max_length=20)
    work_type=forms.CharField(max_length=20)
    exp=forms.CharField(max_length=20)
    job_type=forms.CharField(max_length=20)

class contactform(forms.Form):
    # cname=forms.CharField(max_length=20)
    email=forms.EmailField()
    subject=forms.CharField(max_length=40)
    message=forms.CharField(max_length=500,widget=forms.Textarea(attrs={'row':3,'col':30}))


class jobapplyform(forms.Form):
    company_name=forms.CharField(max_length=20)
    designation=forms.CharField(max_length=30)
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    qualification=forms.CharField(max_length=20)
    phone_no=forms.CharField(max_length=12)
    experience=forms.CharField(max_length=30)
    resume=forms.FileField()
