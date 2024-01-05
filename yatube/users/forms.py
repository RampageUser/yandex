from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=60, label='Login', required=True, help_text='Введите никнейм')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')


class ProfilForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name')