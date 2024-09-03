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


def class02__page(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    context = {
        "courses": courses,
        "categories": categories,
    }
    return render(request, "class_02.html", context)
    pass


def blog_detail(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course,
    }

    return render(request, "single_blog.html", context)


def programs_detail(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course,
    }
    return render(request, "class_01_detail.html", context)


def format_data(data):
    trainer_data = [
        {
            # key : value
            #! Trainer
            "trainer_id": course.trainer.id,
            "profession": course.trainer.profession,
            "trainer_fullname": course.trainer.fullname,
            "trainer_image": course.trainer.image.url,
            "facebook": course.trainer.facebook,
            "twitter": course.trainer.twitter,
            "instagram": course.trainer.instagram,
            "linkedin": course.trainer.linkedin,
            # ! Course
            "course_id": course.pk,
            "course_name": course.name,
            "course_image": course.image.url,
            "course_category": course.category.name,
            "course_description": course.description,
            "course_date": course.created_date,
            "course_level": course.level.name,
            "course_timeofday": course.time_day.name,
            "course_intensity": course.intensity.name,
            "course_style": course.style.name,
        }
        for course in data
    ]
    return trainer_data
