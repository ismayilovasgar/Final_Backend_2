from django.shortcuts import render
from courses.models import *
from pages.models import Review


def index(request):
    categories = Category.objects.all()
    reviews = Review.objects.all()
    context = {
        "categories": categories,
        "reviews": reviews,
    }

    return render(request, "home.html", context)


def pricing(request):
    trainers = Trainer.objects.all()
    context = {
        "trainers": trainers,
    }
    return render(request, "pricing.html", context)


def features(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "features.html", context)


def download(request):
    return render(request, "download.html")


def lifestyle(request):
    tags = Tag.objects.all()
    context = {
        "tags": tags,
    }
    return render(request, "lifestyle.html", context)


def programs(request):
    trainers = Trainer.objects.all()
    styles = Style.objects.all()
    intensities = Intensity.objects.all()
    timeofdaies = TimeOfDay.objects.all()
    levels = Level.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "styles": styles,
        "intensities": intensities,
        "timeofdaies": timeofdaies,
        "levels": levels,
        "categories": categories,
        "tags": tags,
        "trainers": trainers,
    }
    return render(request, "programs.html", context)


def programs_detail(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course,
    }
    return render(request, "class_01_detail.html", context)
