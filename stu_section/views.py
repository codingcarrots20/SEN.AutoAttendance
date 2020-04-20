from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from prof_section.models import AttendanceRecord
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
from . import models

def loginView(request):

    message=""
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            Stu_obj = models.Student.objects.filter(user__username = username)

            if Stu_obj.exists():

                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/stu_section/scan')
                else:
                    message="Invalid username or password."
                    return render(request = request,
                        template_name = "stu_section/login.html",
                        context={"form":form,
                                "message":message})
            else:
                message="Please enter a correct username and password. Note that both fields may be case-sensitive."
        else:
            message= "Invalid username or password."
            return render(request = request,
                    template_name = "stu_section/login.html",
                    context={"form":form,
                            "message":message})


    form = AuthenticationForm()
    return render(request = request,
                    template_name = "stu_section/login.html",
                    context={"form":form,"message":message})



@login_required(login_url='/login')
def scan(request):
    return render(request,"stu_section/scan.html")


def test(request):
    
    qr = request.POST['qr']
    usernm = request.user
    course = ""
    tokenNo = ""
    print(qr)
    if len(qr) > 9:
        data={
            "message":"qr invalid"
        }
        return JsonResponse(data)


    for i in range(5):
        course = course + qr[i]
    for i in range(5,len(qr)):
        tokenNo = tokenNo + qr[i]

    print(qr)
    print(tokenNo)

    if AttendanceToken.objects.filter(tokenNo = tokenNo).exists():
        AttRecs = AttendanceRecord.objects.filter(studentID=usernm)
        flag =False
        for attRec in AttRecs:
            if (  (attRec.dateTime - datetime.now(timezone.utc)).total_seconds()  )/60 < 50  :
                flag = True
        if not flag:


            attRec = AttendanceRecord()
            attRec.studentID = usernm
            attRec.courseID = qr
            attRec.dateTime = datetime.now()

            
            attRec.save()
            
            data={
                "message":"done"
            }
            return JsonResponse(data)

        else:
            data={
                "message":"Already Marked"
            }
            return JsonResponse(data)
    else:
        data={
            "message":"token invalid"
        }
        return JsonResponse(data)