from django.shortcuts import render, redirect
from django.urls.base import reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.models import Course
from django.contrib.auth.models import User


# def user_login_register(request):
#     if request.method == "POST":
#         if "register" in request.POST:
#             register_form = RegisterForm(request.POST)
#             login_form = LoginForm()
#             if register_form.is_valid():
#                 user = register_form.save()
#                 login(request, user)
#                 messages.success(request, "Register successful!")
#                 return redirect("accounts:login_register")
#             messages.error(request, "Invalid username or password.")

#         elif "login" in request.POST:
#             login_form = LoginForm(request, data=request.POST)
#             register_form = RegisterForm()
#             if login_form.is_valid():
#                 user = login_form.get_user()
#                 login(request, user)
#                 messages.success(request, "Login successful!")
#                 return redirect("home")
#             messages.error(request, "Invalid username or password")

#     else:
#         register_form = RegisterForm()
#         login_form = LoginForm()


#     return render(
#         request,
#         "accounts/login_register.html",
#         {"register_form": register_form, "login_form": login_form},
#     )


def user_login(request):
    context = {"name": "mname"}
    return render(request, "accounts/login.html", context)
    # pass


def user_register(request):
    pass


def user_logout(request):
    logout(request)
    return redirect("home")


@login_required(login_url="login")
def user_dashboard(request):
    current_user = request.user
    courses = current_user.courses_joined.all()
    context = {
        "courses": courses,
    }
    return render(request, "accounts/dashboard.html", context)
    pass


def enroll_the_course(request):
    user_id = request.POST["user_id"]
    course_id = request.POST["course_id"]
    course = Course.objects.get(id=course_id)
    user = User.objects.get(id=user_id)

    course.students.add(user)
    return redirect("dashboard")
    pass


def release_the_course(request):
    user_id = request.POST["user_id"]
    course_id = request.POST["course_id"]
    course = Course.objects.get(id=course_id)
    user = User.objects.get(id=user_id)

    course.students.remove(user)
    return redirect("dashboard")
    pass
    pass
