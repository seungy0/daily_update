from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
# 작성한 모델을 사용하는것에 주의
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user_id', 'user_name', 'password', 'email', 'phone', 'is_active', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Personal info', {'fields': ('user_name', 'email', 'phone',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'user_name', 'password1', 'password2', 'email', 'phone')}
         ),
    )
    search_fields = ('user_id', 'user_name')
    ordering = ('user_id',)
    filter_horizontal = ()


# User, UserAdmin 을 등록
admin.site.register(User, UserAdmin)
# Group 을 등록해제
admin.site.unregister(Group)
