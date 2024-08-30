from django.shortcuts import render
from .models import Course, Category, Tag
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
            courses = (
                Course.objects.filter(category__slug=category_slug)
                .order_by("created_date")
                .values()
            )
            courses_list = list(courses)

            return JsonResponse(courses_list, safe=False)
        except:
            return print("eerr-------------------------")
    else:
        return JsonResponse({"error": "Bad request"}, status=400)


def tags_detail(request, tag_slug):
    courses = Course.objects.all().filter(tags__slug=tag_slug)
    tags = Tag.objects.all()
    context = {
        "course": courses,
        "tags": tags,
    }

    return render(request, "courses_detail.html", context)
