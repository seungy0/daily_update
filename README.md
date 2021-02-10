# daily_update
말그대로 매일 조금씩 간단한 코딩하려함.

현재 목표: 빌보드 차트 크롤링해서 표시하고 클릭하면 가사, 한글 해석본 띄우는 웹페이지 제작.

## 기술 스택
* **WEB**

|Django|
|:---:|
|<a href="https://www.djangoproject.com/"><img src="https://static.djangoproject.com/img/logos/django-logo-negative.png" height="50px"></a>|

## 프로젝트 실행 방법

```sh
> service mysql restart
> cd bilchart/bilchart
> python manage.py makemigration
> python manage.py migrate
> python manage.py runserver 0.0.0.0:8000

```
야채가게 웹사이트 테스트 레포지토리로 어느새 변모함. 여기서 연습해서 vegeweb에서 업데이트 중