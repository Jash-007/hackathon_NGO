from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def login(request):
     return render(request, 'login.html')
def register (request):
    return render(request,'register.html')
def feedback(request):
    if request.method=="POST":
        name=request.POST['name'];
        email=request.POST['email'];
        msg=request.POST['message'];
        send_mail(
            "Feedback received",#subject
            msg,
            ['jkngo123@gmail.com'],#from mail
            email #to mail
            );
        return render(request,'feedback.html',{'name':name})
    else:
        return render(request,'feedback.html',{})
def cloth(request):
    return render(request,'cloth.html')
def rupees(request):
    return render(request,'rupees.html')
def plant(request):
    return render(request,'plant.html')
def food(request):
    return render(request,'food.html')
