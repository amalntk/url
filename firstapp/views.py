from cmd import PROMPT
from http.client import HTTPMessage
from json import encoder
from ssl import AlertDescription
from django.http import HttpResponse
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
from firstapp.feature import generate_data_set 
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
        form = encorder(request.POST)
        if form.is_valid():
            message = form.cleaned_data["text"]
            for a,b in SECURE:
                message = message .replace(b, a)
                form = encorder()
            return render(request,'decrypt.html',{'text':message,'fm':form})
    else:
        form=encorder()
        return render(request,'decrypt.html',{'fm':form}) 

def articles(request):
    return render(request,"articles.html")

def phising(request):
    return render(request,"phising.html")
    # ggjgh
    from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings

warnings.filterwarnings('ignore')

# from feature import generate_data_set
# Gradient Boosting Classifier Model
from sklearn.ensemble import GradientBoostingClassifier

data = pd.read_csv("phishing.csv")
#droping index column
data = data.drop(['Index'],axis = 1)
# Splitting the dataset into dependant and independant fetature

X = data.drop(["class"],axis =1)
y = data["class"]

# instantiate the model
gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)

# fit the model 
gbc.fit(X,y)
def predict(request):
    if request.method == "POST":

        # url = request.form["url"]
        url=request.POST.get('url')
        x = np.array(generate_data_set(url)).reshape(1,30) 
        y_pred =gbc.predict(x)[0]
        print(y_pred)
        #1 is safe    
        #-1 is unsafe   
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        print(y_pro_phishing)
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        print(y_pro_non_phishing)
        if(y_pred ==1 ):
            pred = "It is  safe to go ".format(y_pro_phishing*100)
            return render(request,'safe.html',{'pred':pred})
            
        else:
            pred = "It is unsafe to go ".format(y_pro_non_phishing*100)
            return render(request,"unsafe.html",{'pred':pred})
            # pred = "It is {0:.2f} % unsafe to go ".format(y_pro_non_phishing*100)
            # return render_template('index.html',x =y_pro_non_phishing,url=url )
    return render(request,"safe.html")

def safe(request):
    return render(request,"safe.html")
def unsafe(request):
    return render(request,"unsafe.html")    
