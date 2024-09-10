from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm as AuthForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthForm):
    # !No widget
    # username = forms.CharField(max_length=254)
    # password = forms.CharField(widget=forms.PasswordInput)
    # ? use widget
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "name": "username",
                "type": "text",
                "class": "form-control",
                "placeholder": "Username",
                "id": "id_login_username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "name": "password",
                "type": "password",
                "class": "form-control",
                "placeholder": "Password",
                "id": "id_login_password",
            }
        )
    )


# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ["username", "password"]

#     def clean(self):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")
#         user = authenticate(username=username, password=password)

#         if not user:
#             raise forms.ValidationError("Invalid username or password !")

#         return self.cleaned_data
