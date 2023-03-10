from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.forms import *

from django.contrib.auth import get_user_model

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ['email', 'username']


admin.site.register(get_user_model(), CustomUserAdmin)