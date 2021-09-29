from functools import update_wrapper
from django.contrib import admin
from api.models import UserDetail

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ['id','name','date_of_birth','email','phone_number']