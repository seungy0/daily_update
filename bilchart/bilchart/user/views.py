from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User
# Create your views here.


def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'user/register2.html')

    elif request.method == "POST":
        username = request.POST.get('name')
        user_id = request.POST.get('user_id')# 딕셔너리형태
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        res_data = {}
        if not (username and password and re_password and email):
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password:
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(user_name=username, user_id=user_id, email=email, password=make_password(password), phone=phone)
            user.save()
        return render(request, 'user/register2.html', res_data)  # register를 요청받으면 register.html 로 응답.
