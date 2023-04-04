from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="Login",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control"}
                               ))
    password = forms.CharField(label="Parol",
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control"}
                               ))


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Parol",
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control"}
                                ))
    password2 = forms.CharField(label="Parolni qayta kiriting",
                                widget=forms.PasswordInput(
                                    attrs={"class": "form-control"}
                                ))

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "birthday",
        ]
        form_control = {"class": "form-control"}
        widgets = {
            "username": forms.TextInput(attrs=form_control),
            "first_name": forms.TextInput(attrs=form_control),
            "last_name": forms.TextInput(attrs=form_control),
            "email": forms.EmailInput(attrs=form_control),
            "phone": forms.TextInput(attrs=form_control),
            "birthday": forms.DateTimeInput(
                attrs={"class": "form-control",
                       "type": "date"})
        }
