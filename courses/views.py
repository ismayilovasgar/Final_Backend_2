from django.shortcuts import render
from .models import Course, Category, Tag
from django.shortcuts import get_object_or_404
from trainers.models import Trainer
from django.http import JsonResponse, HttpResponse


# Create your views here.
def course_list(request):
    return render(request, "home.html")


def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    context = {"course": course}
    return render(request, "home.html", context)


def categories_detail(request, category_slug):
    if request.method == "POST":
        try:
            courses = Course.objects.filter(category__slug=category_slug)
            trainers = format_data_simple(courses)
            return JsonResponse({"trainer_data": trainers})
        except:
            return print("eerr-------------------------")
    else:
        return JsonResponse({"error": "Bad request"}, status=400)


def tags_detail(request, tag_slug):
    if request.method == "POST":
        try:
            courses = Course.objects.filter(tags__slug=tag_slug)
            result = format_data_bytags(courses)
            return JsonResponse({"all_data": result})
        except:
            return print("eerr-------------------------")
    else:
        return JsonResponse({"error": "Bad request"}, status=400)


def search(request):
    courses = Course.objects.filter(name__contains=request.GET.get["search"])
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "categories": categories,
        "tags": tags,
        "courses": courses,
    }
    return render(request, "courses.html", context)


# ? -------------------- Return Data --------------------
def format_data_simple(data):
    trainer_data = [
        {
            # key : value
            #! Trainer
            "profession": course.trainer.profession,
            "name": course.trainer.fullname,
            "image_url": course.trainer.image.url,
        }
        for course in data
    ]
    return trainer_data


def format_data_bytags(data):
    result = [
        {
            # key : value
            #! Trainer
            "name": course.trainer.fullname,
            "image_url": course.trainer.image.url,
            # ! Course
            "course_name": course.name,
            "course_category": course.category.name,
            "course_description": course.description,
            "course_date": course.created_date,
        }
        for course in data
    ]
    return result


def format_data(data):
    trainer_data = [
        {
            # key : value
            #! Trainer
            "id": course.trainer.id,
            "profession": course.trainer.profession,
            "name": course.trainer.fullname,
            "image_url": course.trainer.image.url,
            "facebook": course.trainer.facebook,
            "twitter": course.trainer.twitter,
            "instagram": course.trainer.instagram,
            "linkedin": course.trainer.linkedin,
            # ! Course
            "course_name": course.name,
            "course_category": course.category,
            "course_description": course.description,
            "course_date": course.created_date,
        }
        for course in data
    ]
    return trainer_data
