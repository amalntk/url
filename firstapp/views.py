from json import encoder
from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
import os
from .forms import encorder
from django.contrib.auth.models import User
from .forms import regg
# Create your views here.
SECURE=(('a','$'),('b','!'),('c','5'),('d','*'),('e','`'),('f','|'),('g','}'),('h','{'),('i',']'),('j','['),('k','/'),('l','?'),('m','.'),('n','~'),('o','!'),('p','@'),('q','#'),('r','$'),('s','%'),('t','^'),('u','&'),('v','-'),('w','_'),('x','+'),('y',')'),('z','('))
def index(request):
    return render(request,"index.html")
def welcome(request):
    return render(request,"welcome.html")
# def login(request):
#     return render(request,"login1.html")
def cipher(request):
    return render(request,"cipher.html")
def logout(request):
    return render(request,"welcome.html")
def reg(request):
    form = regg()
    if request.method=='POST':
        form=regg(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            # message.success(request,'Account was created for ' + user)
            return redirect('login')
    context={'form':form}
    return render(request,'reg2.html',context)

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            pass
            # message.info(request,'Ussername or password is incorrect')
    context={}
    return render(request,'login1.html',context)
def encrypt(request):
    if request.method=="POST":
        form=encorder(request.POST)
        if form.is_valid():
            message = form.cleaned_data["text"]
            for a,b in SECURE:
                message=message.replace(a,b)
                form=encorder()
            return render(request,'encrypt.html',{'text':message, 'fm':form})
    else:
        form=encorder()
        return render(request,'encrypt.html',{'fm':form})

def decrypt(request):
    if request.method=="POST":
        form=encorder(request.POST)
        if form.is_valid():
            message =form.cleaned_data["text"]
            for a,b in SECURE:
                message=message.replace(b,a)
                form=encorder()
            return render(request,'decrypt.html',{'text':message, 'fm':form})
    else:
        form=encorder()
        return render(request,'decrypt.html',{'fm':form}) 

def articles(request):
    return render(request,"articles.html")

