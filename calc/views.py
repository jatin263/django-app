from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from calc.form import StudentForm
from calc.function import handle_uploaded_file
from calc.models import users

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'Jatin'})

def fetchUser(request):
    data = serializers.serialize("json", users.objects.all())
    u = list(users.objects.filter(username="d").values())
    print(u)
    return JsonResponse(u,safe=False)

def Api(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            t=handle_uploaded_file(request.FILES['file'])  
            return HttpResponse(t)  
    else:  
        student = StudentForm()  
        return render(request,"Api.html",{'form':student})


def add(request):
    u1 = users()
    u1.id=7062039927
    u1.name="Jatin Kumawat"
    u1.password="123456"
    name=request.POST['name']
    password=request.POST['password']
    if name== u1.name and password==u1.password:
        return render(request,'result.html',{'result':u1})
    else:
        return render(request,'home.html',{'result':"Wrong Password"})