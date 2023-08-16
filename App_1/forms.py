from .models import Forum_Publications
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class forum_publications_form(ModelForm):
    class Meta:
        model = Forum_Publications
        fields = ['title', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва Запису'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст Запису'
            }),
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(label='Ім\'я користувача')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
