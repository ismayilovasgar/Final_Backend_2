from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "",
                "placeholder": "Username",
            }
        )
    )
    password = forms.PasswordInput(
        widget=forms.PasswordInput(
            attrs={
                "class": "",
                "placeholder": "Password",
            }
        )
    )


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "",
                "placeholder": "First Name",
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "",
                "placeholder": "Last Name",
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "",
                "placeholder": "Username",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "",
                "placeholder": "Email",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "",
                "placeholder": "Password",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "",
                "placeholder": "Re-Type Password",
            }
        )
    )

    class Meta:
        model = User
        # fields = "__all__"
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
