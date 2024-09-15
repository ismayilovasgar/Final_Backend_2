from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm as AuthForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    # Customizing the username field
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",  # Adding a custom CSS class
                "placeholder": "Username",
                "autocomplete": "username",
            }
        )
    )

    # Customizing the email field
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",  # Adding a custom CSS class
                "placeholder": "Email",  # Placeholder text
                "autocomplete": "email",  # HTML5 autocomplete attribute
            }
        )
    )
    # Customizing the firstname field
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",  # Adding a custom CSS class
                "placeholder": "Firstname",  # Placeholder text
                "autocomplete": "firstname",  # HTML5 autocomplete attribute
                "id": "id_register_firstname",
            }
        )
    )
    # Customizing the lastname field
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",  # Adding a custom CSS class
                "placeholder": "Lastname",  # Placeholder text
                "autocomplete": "lastname",  # HTML5 autocomplete attribute
                "id": "id_register_lastname",
            }
        )
    )

    # Customizing the password1 field
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",  # Adding a custom CSS class
                "placeholder": "Password",
                "autocomplete": "new-password",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",  # Adding a custom CSS class
                "placeholder": "Confirm Password",
                "autocomplete": "new-password",
            }
        )
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


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
                "autocomplete": "username",  # Autocomplete attribute for better UX
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
                "autocomplete": "current-password",
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
