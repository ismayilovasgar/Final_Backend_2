from django.shortcuts import render


# Create your views here.
def user_login(request):
    return render(request, "accounts/login.html")


def user_register(request):
    pass


def user_dashboard(request):
    pass


def user_logout(request):
    pass
