from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from .models import User
from django.contrib.auth import authenticate,login,logout


def regstudent(request):
    if request.method=="POST":
        n=request.POST['name']
        a=request.POST['add']
        p=request.POST['phone']
        age=request.POST['age']
        u=request.POST['uname']
        password=request.POST['pass']
        User.objects.create_user(Name=n,Address=a,Phoneno=p,Age=age,username=u,password=password,Djoin='2022-06-12',usertype="student",Status=0)
        return HttpResponse('saved')
    else:
        return render(request,'regstudent.html')
    
def regteacher(request):
    if request.method=="POST":
        nm=request.POST['name']
        ad=request.POST['add']
        ph=request.POST['phone']
        ag=request.POST['age']
        q=request.POST['qua']
        dj=request.POST['djoin']
        un=request.POST['uname']
        pas=request.POST['pass']
        User.objects.create_user(Name=nm,Address=ad,Phoneno=ph,Age=ag,Qualification=q,Djoin=dj,username=un,password=pas,usertype="teacher",Status=0)
        return HttpResponse('saved')
    else:
        return render(request,'regteacher.html')
    
def studlist(request):
    x=User.objects.filter(Status="0",usertype='student')
    return render(request,'studlist.html',{'data':x})

   
def teacherlist(request):
    x=User.objects.filter(Status="0",usertype='teacher')
    return render(request,'teacherlist.html',{'data':x})

def studapprove(request,id):
    user=User.objects.filter(id=id).update(Status=1)
    # user.save()

    return redirect(studlist)

def studreject(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect(studlist)


def log(request):
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['psw']
        
        user=authenticate(request,username=u,password=p)
        print(user)
        if user is not None and user.is_superuser==1:
            login(request,user)
            return render(request,'adminhome.html')
        elif user is not None and user.usertype=="student" and user.Status==1:
            login(request,user)
            request.session['studid']=user.id
            return render(request,'studenthome.html')
            
        elif user is not None and user.usertype=="teacher":
            login(request,user)
            request.session['teachid']=user.id
            return render(request,'teacherhome.html')
        return HttpResponse("not approved")
    else:
        return render(request,'log.html')


def adminhome(request):
    return render(request,'adminhome.html')

def studenthome(request):
    return render(request,'studenthome.html')

def teacherhome(request):
    return render(request,'teacherhome.html')

def home(request):
    return render(request,'home.html')