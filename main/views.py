from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
import pyttsx3

# Create your views here.
def main(request):
    
    if request.method == 'POST':
        username =  request.POST['name']
        email = request.POST['email']
        password = request.POST['pwd']
        
        if User.objects.filter(email=email).exists():
            return render(request,'signup.html',{'error':"Email already taken"}) 
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();
            print("user created")
            return render(request,'login.html')
    else:
        return render(request,'signup.html') 


def login_user(request):

    if 'username' in request.session:
        return render(request,'dumb.html')

    if request.method == 'POST': 
        username = request.POST.get('username')
        password = request.POST.get('password') 

        check_user = User.objects.filter(username=username, password=password)
        if check_user:
            return redirect("/login_user")
        else:
            request.session['username'] = username
            return redirect('dumb')

    else:
        return render(request,'login.html')


def logout_user(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('/')


def dumb(request):
    if 'username' in request.session:
        return render(request,'dumb.html')
    return redirect('/') 


def txt_sp(request):
    value=request.GET['text']
    obj=pyttsx3.init()
    obj.say(value)
    obj.runAndWait()
    return redirect('/')
