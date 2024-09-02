from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm


def user_login(request):
    if request.method == "POST":
        if "register" in request.POST:
            register_form = RegisterForm(request.POST)
            login_form = LoginForm()
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                return redirect("home")
        elif "login" in request.POST:
            login_form = LoginForm(request, data=request.POST)
            register_form = RegisterForm()
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect("home")
    else:
        register_form = RegisterForm()
        login_form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"register_form": register_form, "login_form": login_form},
    )


def user_logout(request):
    logout(request)
    return redirect("home")


# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect("home")
#     else:
#         form = LoginForm()
#     return render(request, "accounts/login.html", {"form": form})


# def user_register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("home")
#     else:
#         form = RegisterForm()
#         return render(request, "accounts/login.html", {"form": form})


# def user_dashboard(request):
#     pass


# Django Youtube

# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect("home")
#                 else:
#                     messages.info(request, "Disable Account !")

#             messages.info(request, "Check Your Username or Password !")

#     form = LoginForm()
#     context = {
#         "form": form,
#     }
#     return render(request, "accounts/login.html", context)
