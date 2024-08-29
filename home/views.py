from django.shortcuts import render
from .models import Trainer, Review


# Create your views here.
# Create your views here.
def home__page(request):
    trainers = Trainer.objects.all()
    reviews = Review.objects.all()

    context = {
        "categorys": Trainer.CATEGORY_CHOICES,
        "reviews": reviews,
    }
    return render(request, "home.html", context)


def pricing__page(request):
    trainers = Trainer.objects.all()
    context = {
        "trainers": trainers,
    }
    return render(request, "pricing.html", context)


def features__page(request):
    reviews = Review.objects.all()
    context = {
        # "trainers": trainers,
        "reviews": reviews,
    }

    return render(request, "features.html", context)


def download__page(request):
    return render(request, "download.html")


def lifestyle__page(request):
    return render(request, "lifestyle.html")


def singleblog__page(request, id):
    trainer = Trainer.objects.get(id=id)
    context = {"trainer": trainer}
    return render(request, "single_blog.html", context)


def class01__page(request):
    trainers = Trainer.objects.all()
    context = {
        "trainers": trainers,
        "categorys": Trainer.CATEGORY_CHOICES,
        "styles": Trainer.YOGA_STYLE_CHOICES,
        "timeofday": Trainer.TIME_OF_DAY_CHOICES,
        "difficulty": Trainer.DIFFICULTY_CHOICES,
        "intensity": Trainer.INTENSITY_CHOICES,
    }
    return render(request, "class_01.html", context)


def class01detail__page(request, id):
    trainer = Trainer.objects.get(id=id)
    context = {"trainer": trainer}
    return render(request, "class_01_detail.html", context)


def class02__page(request):
    context = {
        "categorys": Trainer.CATEGORY_CHOICES,
    }
    return render(request, "class_02.html", context)


def class02detail__page(request):
    return render(request, "class_02_detail.html")
