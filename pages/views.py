from django.shortcuts import render
from courses.models import Category, Tag, Course


# Create your views here.
def index(request):
    categories = Category.objects.all()
    # courses = Course.objects.all()
    context = {
        "categories": categories,
        # "courses": courses,
    }

    return render(request, "home.html", context)


def pricing(request):
    return render(request, "pricing.html")


def features(request):
    return render(request, "features.html")


def download(request):
    return render(request, "download.html")


def lifestyle(request):
    return render(request, "lifestyle.html")
