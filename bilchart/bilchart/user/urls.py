# https://velog.io/@trequartista/TIL14-Django-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84


from django.urls import path
from . import views


urlpatterns = [
   path('/register/', views.register),
   # 즉, 최종적인 url은 127~~~~:8000/user/register가 된다.
]
