from django.shortcuts import render
import json

from django.views import View
from django.http import JsonResponse

from .models import User
# Create your views here.


class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            user_id=data['user_id'],
            email=data['email'],
            password=data['password'],
        )

        if User.objects.filter(user_id=data['user_id']).exists() == True:
            return JsonResponse({"message": "이미 존재하는 아이디입니다."}, status=401)

        else:
            User.objects.create(user_id=data['user_id'], email=data['email'], password=data['password'])
            return JsonResponse({"message": "회원으로 가입되셨습니다."}, status=200)

    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data": list(users)}, status=200)
