from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from users.models import CustomUser as User
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']