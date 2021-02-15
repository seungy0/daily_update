from django.contrib import admin

# Register your models here.


from .models import User   # 같은 경로의 models.py에서 User라는 클래스를 임포트한다.

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'password', 'email', 'phone')


admin.site.register(User, UserAdmin)  # site에 등록
