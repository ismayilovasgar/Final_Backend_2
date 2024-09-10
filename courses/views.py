from .models import Course, Category, Tag
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from trainers.models import Trainer
from django.http import JsonResponse
from django.db.models import Q
import json


# ----------------------- Start Functions -----------------------
def categories_detail(request, category_slug):
    if request.method == "POST":
        try:
            # Retrieve the category
            category = Category.objects.get(slug=category_slug)
            # Filter courses by this category
            courses = Course.objects.filter(category=category).select_related("trainer")

            # Extract trainers from these courses
            trainers = {course.trainer for course in courses}

            results = format_data_simple(trainers)

            return JsonResponse(results, safe=False)
        except:
            return print("eerr-------------------------")
    else:
        return JsonResponse({"error": "Bad request"}, status=400)


def tags_detail(request, tag_slug):
    if request.method == "POST":
        try:
            courses = Course.objects.filter(tags__slug=tag_slug)
            results = format_data_bytags(courses)
            return JsonResponse(results, safe=False)
        except:
            return print("eerr-------------------------")
    else:
        return JsonResponse({"error": "Bad request"}, status=400)


def show_by_array(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            list = data.get("data")
            print(list)
            result = Course.objects.filter(
                Q(style__name__contains=list[0])
                & Q(time_day__name__iexact=list[1])
                & Q(level__name__iexact=list[2])
                & Q(intensity__name__iexact=list[3])
            ).order_by("-created_date")

            if request.user.is_authenticated:
                # for exclude courses that user enrolled
                result = result.exclude(students=request.user)

            #
            results = format_data(result)

            return JsonResponse(results, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


def show_by_text(request, text):
    if request.method == "POST":
        try:
            pre_text = text.split("_")[0]
            text = text.split("_")[1]
            if pre_text.startswith("category"):
                results = Course.objects.filter(category__name=text).order_by(
                    "-created_date"
                )
            else:
                results = Course.objects.filter(name__contains=text).order_by(
                    "-created_date"
                )
            if request.user.is_authenticated:
                # for exclude courses that user enrolled
                results = results.exclude(students=request.user)

            results = format_data(results)
            return JsonResponse(results, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


@login_required(login_url="login")
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        # Enroll user in course
        course.students.add(request.user) 

        # Redirect to the dashboard or course detail page
        return redirect("courses:dashboard")  
    return redirect("programs_detail", id=course.id)


@login_required(login_url="login")
def release_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.students.remove(request.user)  # Unenroll user from course
        return redirect(
            "courses:dashboard"
        )  # Redirect to the dashboard or course detail page

    return redirect("programs_detail", id=course.id)


@login_required(login_url="login")
def dashboard__page(request):
    # Get all courses the user is enrolled in
    courses = (
        request.user.courses_joined.all()
    )  # Assuming `courses_joined` is a ManyToManyField
    return render(request, "accounts/dashboard.html", {"courses": courses})


def user_unenrolled_course(request):
    pass


# ? --------------------------------------------- Return Data Functions ---------------------------------------------
def format_data_simple(trainers):
    trainer_data = [
        {
            # key : value
            #! Trainer
            "profession": trainer.profession,
            "name": trainer.fullname,
            "image_url": trainer.image.url,
        }
        for trainer in trainers
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
            "course_id": course.id,
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
