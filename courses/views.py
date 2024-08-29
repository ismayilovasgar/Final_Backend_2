from django.shortcuts import render
from .models import Course, Category, Tag


# Create your views here.
def course_list(request):
    return render(request, "home.html")


def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    context = {"course": course}
    return render(request, "course_detail.html", context)


def course_detail(request, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    context = {"course": course}
    return render(request, "course_detail.html", context)


def categories_detail(request, category_slug):
    courses = Course.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    context = {
        "course": courses,
        "categories": categories,
    }

    return render(request, "course_detail.html", context)


def tags_detail(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug)
    tags = Tag.objects.all()
    context = {
        "course": courses,
        "tags": tags,
    }

    return render(request, "courses_detail.html", context)
