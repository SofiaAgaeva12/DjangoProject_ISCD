from django import forms
from django.contrib.auth.forms import UserCreationForm
from polls.models import AuthUser


class SignupForm(UserCreationForm):

    class Meta:
        model = AuthUser
        fields = ('first_name', 'username', 'password1', 'password2', 'avatar')


