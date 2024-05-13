from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from jobportal1.settings import EMAIL_HOST_USER
from django.contrib import  messages
from django.core.mail import send_mail
from  django.conf import settings
from  django.contrib.auth import authenticate
import uuid
from  django.contrib.auth.models import User
from django.http import  HttpResponse
from .forms  import *
from  .models import *
# # Create your views here.
def home(request):
    return render(request,'home.html')


def regis(request):
    if request.method=='POST':

        email=request.POST.get('email')
        pas=request.POST.get('password')
        uname=request.POST.get('uname')

        if User.objects.filter(email=email).first():
            messages.success(request,"email already taken")
            return redirect(regis)

        if User.objects.filter(username=uname).first():
            messages.success(request,"username already taken")
            return redirect(regis)

        user_obj=User(username=uname,email=email)
        user_obj.set_password(pas)
        user_obj.save()
        auth_token=str(uuid.uuid4())
        profile_obj=profile1.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)

        return redirect(success)

    return render(request,"cregister.html")


def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f"pass the link to verify your account http:127.0.0.1:8000/verify/{token}"
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)


def success(request):
    return render(request,"success.html")

def login(request):
    global User;
    if request.method=='POST':
        username=request.POST.get('uname')
        pas=request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'company not found')
            return  redirect(login)
        profile_obj=profile1.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile verified cheek your email')
            return  redirect(login)
        User=authenticate(username=username,password=pas)

        if User is None:
            messages.success(request,'wrong password or username')
            return  redirect(login)
        # return  HttpResponse("success")
        obj=profile1.objects.filter(user=user_obj)
        return render(request,'jobs.html',{'obj':obj})

    return render(request,'clogin.html')

def verify(request,auth_token):
    profile_obj=profile1.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account already verified')
            redirect(login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'ur account verified')
        return redirect(login)
    else:
        return redirect(error)

def error(request):
    return  render(request,'error.html')



def regis2(request):
    if request.method=="POST":
        a=regform(request.POST)
        if a.is_valid():
            unm=a.cleaned_data['uname']
            eml=a.cleaned_data['email']
            do=a.cleaned_data['dob']
            hq=a.cleaned_data['hq']
            pas=a.cleaned_data['password']
            cpass=a.cleaned_data['cpassword']
            if pas==cpass:
                b=regmodel(uname=unm,email=eml,password=pas,hq=hq,dob=do)
                b.save()
                # return  HttpResponse("successfully registered")
                return render(request,'jlogin.html')
            else:
                return HttpResponse("password and confirm password not match")
        else:
            return HttpResponse("enter valid data")
    return render(request,'jregister.html')

def login2(request):
    if request.method == "POST":
        form = logform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['pas']
            users = regmodel.objects.all()

            for user in users:
                if email == user.email and password == user.password:
                    return render(request, 'applicant.html', {'user': user})

            return HttpResponse("Email and password incorrect....")

        return HttpResponse("Enter valid data...")

    return render(request, 'jlogin.html')


def addjob(request,id):
    if request.method=="POST":
        a=reg2form(request.POST)
        if a.is_valid():
            cnm=a.cleaned_data['cname']
            eml=a.cleaned_data['email']
            jt=a.cleaned_data['job_title']
            wt=a.cleaned_data['work_type']
            ex=a.cleaned_data['exp']
            jtype=a.cleaned_data['job_type']
            b=reg2model(cname=cnm,email=eml,job_title=jt,work_type=wt,exp=ex,job_type=jtype)
            b.save()
            return  HttpResponse("successfully registered")
        else:
            return HttpResponse("enter valid data")

    a=profile1.objects.get(id=id)
    # obj=profile1.objects.get(id=id)
    return render(request,'addjob.html',{'ee':a})




# def add(request):

def list_company(request):
    a= reg2model.objects.all()
    cn=[]
    eml=[]
    id=[]


    for i in a:
        cnn=i.cname
        cn.append(cnn)

        emm=i.email
        eml.append(emm)

        t=i.id
        id.append(t)


    mylist=zip(cn,eml,id)
    # ,jti,wt,ex,jo)
    return render(request,"showcompany.html",{'list':mylist})

def sendmail(request,id):

    if request.method=='POST':
        sub=contactform(request.POST)
        if sub.is_valid():
            # name=sub.cleaned_data['name']
            email=sub.cleaned_data['email']
            subject=sub.cleaned_data['subject']
            msg=sub.cleaned_data['message']
            send_mail(subject,msg,EMAIL_HOST_USER,[email],fail_silently=False)
            return HttpResponse("success")
        else:
            return HttpResponse("not valid")

    a=reg2model.objects.get(id=id)
    return render(request,"sendmail.html",{'a':a})

# def sendmail2(request):


# userdetails
def update(request,id):
    ak=regmodel.objects.get(id=id)
    if request.method=='POST':
        ak.uname=request.POST.get('uname')
        ak.email=request.POST.get('email')
        ak.dob=request.POST.get('dob')
        ak.hq=request.POST.get('hq')
        ak.save()
        return redirect(login2)
    return render(request,'updateuser.html',{'ak':ak})


# def openings(request,id):
#     s = regmodel.objects.get(id=id)
#     k = reg2model.objects.all()
#     cn = []
#     jt=[]
#     ids = []
#
#     for i in k:
#         cnn = i.cname
#         cn.append(cnn)
#
#         # emm = i.email
#         # eml.append(emm)
#
#         m = i. job_title
#         jt.append(m)
#
#         t = i.id
#         ids.append(t)
#
#     j = zip(cn, jt, ids)
#     return render(request, 'opening.html', { 'j': j},{'s':s})


def openings(request, id):
    s = regmodel.objects.get(id=id)
    k = reg2model.objects.all()
    cn = []
    jt = []
    ids = []

    for i in k:
        cnn = i.cname
        cn.append(cnn)

        m = i.job_title
        jt.append(m)

        t = i.id
        ids.append(t)

    j = zip(cn, jt, ids)
    return render(request, 'opening.html', {'j': j, 's': s})

def viewmore(request, id):
    s = regmodel.objects.get(id=id)
    x = reg2model.objects.all()
    cn = []
    eml = []
    jt = []
    jo = []
    wo = []
    ex = []
    ids = []

    for i in x:
        cnn = i.cname
        cn.append(cnn)

        emm = i.email
        eml.append(emm)

        m = i.job_title
        jt.append(m)

        joo = i.job_type
        jo.append(joo)

        w = i.work_type
        wo.append(w)

        e = i.exp
        ex.append(e)

        t = i.id
        ids.append(t)

    x = zip(cn, eml, jt, jo, wo, ex, ids)
    return render(request, 'viewjobs.html', {'x': x, 's': s})


def apply(request, id, ids):
    a = reg2model.objects.get(id=ids)
    s = regmodel.objects.get(id=id)
    if request.method=="POST":
        a=jobapplyform(request.POST,request.FILES)
        if a.is_valid():
            cn=a.cleaned_data['company_name']
            des=a.cleaned_data['designation']
            nm=a.cleaned_data['name']
            eml=a.cleaned_data['email']
            qul=a.cleaned_data['qualification']
            pn=a.cleaned_data['phone_no']
            ex=a.cleaned_data['experience']
            res=a.cleaned_data['resume']
            b=jobapplymodel(company_name=cn,designation=des,name=nm,email=eml,qualification=qul,phone_no=pn,experience=ex,resume=res)
            b.save()
            # return messages("success")
            return render(request,'success2.html')
        else:
            return HttpResponse("enter valid data")

    return render(request, 'aplyform.html', {'a': a, 's': s})




def view_applicant(request,id):
    a=profile1.objects.get(id=id)
    a_name=a.user.username
    data=jobapplymodel.objects.all()
    job=[]
    nam=[]
    eml=[]
    qul=[]
    ph=[]
    exp=[]
    cv=[]
    for i in data:
        if i.company_name==a_name:
            jt=i.designation
            job.append(jt)

            name=i.name
            nam.append(name)

            email1=i.email
            eml.append(email1)

            qual=i.qualification
            qul.append(qual)

            phno=i. phone_no
            ph.append(phno)

            ex=i.experience
            exp.append(ex)

            cvv=i.resume
            cv.append(str(cvv).split('/')[-1])
    applicant=zip(job,nam,eml,qul,ph,exp,cv)
    return render(request,'view_applicant.html',{'applicant':applicant})


def applied_jobs(request,id):
    b=regmodel.objects.get(id=id)
    name1=b.uname
    data=jobapplymodel.objects.all()
    job=[]
    cnam=[]

    for i in data:
        if i.name==name1:
            jt=i.designation
            job.append(jt)

            name=i.company_name
            cnam.append(name)
    jobs=zip(job,cnam)
    return  render(request,'applied_jobs.html',{'jobs':jobs})
# recipe/views.py


