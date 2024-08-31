from django.shortcuts import render
from .models import Course, Category, Tag
from django.shortcuts import get_object_or_404
from trainers.models import Trainer
from django.http import JsonResponse
from django.db.models import Q
import json


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
            return JsonResponse({"cards": result})
        except:
            return print("eerr-------------------------")
    else:
        return JsonResponse({"error": "Bad request"}, status=400)


def show_by_array(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            list = data.get("data")
            result = Course.objects.filter(
                Q(style__name__contains=list[0])
                & Q(time_day__name__iexact=list[1])
                & Q(level__name__iexact=list[2])
                & Q(intensity__name__iexact=list[3])
            ).order_by("-created_date")
            results = format_data(result)

            return JsonResponse({"results": results})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


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
            "trainer_image_url": course.trainer.image.url,
            # ! Course
            "course_name": course.name,
            "course_category": course.category.name.replace(" & ", ""),
            "course_category_long": course.category.name,
            "course_description": course.description,
            "course_date": course.created_date.strftime("%b %d, %Y"),
            "course_image": course.image.url,
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
