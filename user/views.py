from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return HttpResponse("사용자 존재")
        else:
            return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if password == password2:
            User.objects.create_user(username=username, password=password, phone=phone, address=address)
            return redirect('/login')
        else:
            return HttpResponse("비밀번호가 틀렸습니다.")
        
    else:
        return HttpResponse("허용되지 않은 메소드 입니다")
    
    
def login(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if not user:
            return render(request, 'login.html') 
        else:
            auth.login(request, user)
            return HttpResponse("로그인 성공")

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return HttpResponse("메인페이지")
        else:
            return render(request, 'login.html')