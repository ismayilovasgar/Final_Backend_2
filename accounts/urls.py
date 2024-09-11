from django.urls import path
from . import views

# Define the app namespace
app_name = "accounts"


urlpatterns = [
    # path("login_register/", views.user_login_register, name="login_register"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("dashboard/", views.user_dashboard, name="dashboard"),
    path("enroll_the_course/", views.enroll_the_course, name="enroll_the_course"),
    path("release_the_course/", views.release_the_course, name="release_the_course"),
]
