# from django.shortcuts import render
# from .models import Course, Category, Tag
# from django.shortcuts import get_object_or_404
# from trainers.models import Trainer
# from django.http import JsonResponse
# from django.db.models import Q
# import json


# # ----------------------- Start Functions -----------------------
# def categories_detail(request, category_slug):
#     if request.method == "POST":
#         try:
#             # Retrieve the category
#             category = Category.objects.get(slug=category_slug)
#             # Filter courses by this category
#             courses = Course.objects.filter(category=category).select_related("trainer")

#             # Extract trainers from these courses
#             trainers = {course.trainer for course in courses}

#             results = format_data_simple(trainers)

#             return JsonResponse(results, safe=False)
#         except:
#             return print("eerr-------------------------")
#     else:
#         return JsonResponse({"error": "Bad request"}, status=400)


# def tags_detail(request, tag_slug):
#     if request.method == "POST":
#         try:
#             courses = Course.objects.filter(tags__slug=tag_slug)
#             results = format_data_bytags(courses)
#             return JsonResponse(results, safe=False)
#         except:
#             return print("eerr-------------------------")
#     else:
#         return JsonResponse({"error": "Bad request"}, status=400)


# def show_by_array(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             list = data.get("data")
#             result = Course.objects.filter(
#                 Q(style__name__contains=list[0])
#                 & Q(time_day__name__iexact=list[1])
#                 & Q(level__name__iexact=list[2])
#                 & Q(intensity__name__iexact=list[3])
#             ).order_by("-created_date")
#             results = format_data(result)

#             return JsonResponse({"results": results})
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)
#     return JsonResponse({"error": "Invalid request method"}, status=405)


# def show_by_text(request, text):
#     if request.method == "POST":
#         try:
#             pre_text = text.split("_")[0]
#             text = text.split("_")[1]
#             if pre_text.startswith("category"):
#                 results = Course.objects.filter(category__name=text).order_by(
#                     "-created_date"
#                 )
#             else:
#                 results = Course.objects.filter(name__contains=text).order_by(
#                     "-created_date"
#                 )

#             results = format_data(results)
#             return JsonResponse({"results": results})
#         except json.JSONDecodeError:
#             return JsonResponse({"error": "Invalid JSON"}, status=400)
#     return JsonResponse({"error": "Invalid request method"}, status=405)


# def courses_list(request):
#     # 1
#     # current_user = request.user
#     # if current_user.is_authenticated:
#     #     enrolled_courses = current_user.courses_joined.all()
#     #     courses = Course.objects.all().order_by("created_date")
#     #     for course in enrolled_courses:
#     #         courses = courses.exclude(id=course.id)
#     # else:
#     #     courses = Course.objects.all()

#     # 2
#     # current_user = request.user

#     # if current_user.is_authenticated:
#     #     courses = Course.objects.exclude(students=current_user)
#     #     # courses = Course.objects.exclude(students__username=current_user)
#     # else:
#     #     courses = Course.objects.all().order_by("-created_date")

#     # ortaq hisse
#     # contenxt = {
#     # "courses": courses,
#     # "tags": tags,
#     # "categories": categories,
#     # }
#     pass


# # ? -------------------- Return Data --------------------
# def format_data_simple(trainers):
#     trainer_data = [
#         {
#             # key : value
#             #! Trainer
#             "profession": trainer.profession,
#             "name": trainer.fullname,
#             "image_url": trainer.image.url,
#         }
#         for trainer in trainers
#     ]
#     return trainer_data


# def format_data_bytags(data):
#     result = [
#         {
#             # key : value
#             #! Trainer
#             "name": course.trainer.fullname,
#             "trainer_image_url": course.trainer.image.url,
#             # ! Course
#             "course_id": course.id,
#             "course_name": course.name,
#             "course_category": course.category.name.replace(" & ", ""),
#             "course_category_long": course.category.name,
#             "course_description": course.description,
#             "course_date": course.created_date.strftime("%b %d, %Y"),
#             "course_image": course.image.url,
#         }
#         for course in data
#     ]
#     return result


# def format_data(data):
#     trainer_data = [
#         {
#             # key : value
#             #! Trainer
#             "trainer_id": course.trainer.id,
#             "profession": course.trainer.profession,
#             "trainer_fullname": course.trainer.fullname,
#             "trainer_image": course.trainer.image.url,
#             "facebook": course.trainer.facebook,
#             "twitter": course.trainer.twitter,
#             "instagram": course.trainer.instagram,
#             "linkedin": course.trainer.linkedin,
#             # ! Course
#             "course_id": course.pk,
#             "course_name": course.name,
#             "course_image": course.image.url,
#             "course_category": course.category.name,
#             "course_description": course.description,
#             "course_date": course.created_date,
#             "course_level": course.level.name,
#             "course_timeofday": course.time_day.name,
#             "course_intensity": course.intensity.name,
#             "course_style": course.style.name,
#         }
#         for course in data
#     ]
#     return trainer_data
