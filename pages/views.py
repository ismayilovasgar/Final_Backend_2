from django.shortcuts import render
from courses.models import Category, Tag, Course, Trainer
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
    tags = Tag.objects.all()
    context = {
        "tags": tags,
    }
    return render(request, "programs.html", context)
