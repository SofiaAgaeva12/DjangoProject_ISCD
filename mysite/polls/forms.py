from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AuthUser


class SignupForm(UserCreationForm):

    class Meta:
        model = AuthUser
        fields = ('username', 'password1', 'password2', 'avatar')


