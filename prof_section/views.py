from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse
import hashlib
from . import models

no = 0
qrCodeStayTime = 10000
reloadTime = 10 * 60 * 1000 

def welcome(request):
    #return HttpResponse("Welcome to the Autoattendence system.")
    text_template_dict = {'insert_here' : "This is the AA system!" }
    return render(request, 'index.html', context=text_template_dict)

def records(request):
    records = models.AttendanceRecord.objects.order_by('dateTime')
    record_template_dict = {'records':records}
    return render(request, 'records.html', context=record_template_dict)


# Create your views here.
def loginView(request):
    message = ""
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            prof_obj = models.Prof.objects.filter(user__username = username)

            if prof_obj.exists():

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index/')
                else:
                    message="Invalid username or password."
                    return render(request = request,
                        template_name = "prof_section/login.html",
                        context={"form":form,
                                "message":message})
            else:
                message="Please enter a correct username and password. Note that both fields may be case-sensitive."
            
        else:
            return render(request = request,
                    template_name = "prof_section/login.html",
                    context={"form":form,
                            "message":message})

                            
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "prof_section/login.html",
                    context={"form":form,"message":message})

@login_required(login_url='/login')
def index(request):

    username = request.user
    prof_obj = models.Prof.objects.filter(user__username = username)
    if(prof_obj.exists()):
        courses = prof_obj[0].courses.split(",")
    else:
        courses = ["no courses added"] 
    
    context ={
            "time" : qrCodeStayTime, 
            "courses" : courses,
            "reloadTime": reloadTime
    }

    return render(request,"prof_section/index.html",context)


def getqr(request):
    
    course = request.GET["course"]
    no = random.randint(0,299)

    
    
    data={
        "no" : course+str(no),
    }
    
    return JsonResponse(data)



