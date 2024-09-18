from django.shortcuts import render, redirect
from courses.models import *
from pages.models import Review
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# sending message
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

#
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect

import json


def index(request):
    # Check for the first_login session variable
    # first_login = request.session.pop("first_login", None)  # Remove after showing once
    login_success = request.session.pop("login_success", None)  # Show the message once
    categories = Category.objects.all()
    reviews = Review.objects.all()
    context = {
        "login_success": login_success,
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


def class01_detail_page(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        "course": course,
    }
    return render(request, "class_01_detail.html", context)


def class02__page(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    context = {
        "courses": courses,
        "categories": categories,
    }
    return render(request, "class_02.html", context)


def blog_detail(request, id):
    course = get_object_or_404(Course, id=id)
    context = {
        "course": course,
    }

    return render(request, "single_blog.html", context)


# @login_required(login_url="accounts:login")
def programs_detail(request, id):
    course = get_object_or_404(Course, id=id)
    courses = Course.objects.all()
    context = {
        "course": course,
        "courses": courses,
    }
    if request.user.is_authenticated:
        return render(request, "class_02_detail.html", context)
    return render(request, "class_01_detail.html", context)


def class02_trainers(request, category_name):
    if request.method == "POST":
        try:
            category = Category.objects.get(name=category_name)
            trainer_ids = set()
            trainers = Trainer.objects.all()
            result = []

            for trainer in trainers:
                trainer_courses = Course.objects.filter(
                    trainer=trainer, category=category
                )
                if trainer_courses.exists():
                    if trainer.id not in trainer_ids:
                        trainer_data = {
                            "fullname": trainer.fullname,
                            "trainer_image": trainer.image.url,
                            "profession": trainer.profession,
                            "facebook": trainer.facebook,
                            "twitter": trainer.twitter,
                            "instagram": trainer.instagram,
                            "linkedin": trainer.linkedin,
                            "courses": [],
                        }
                        for course in trainer_courses:
                            course_data = {
                                "image": course.image.url,
                                "description": course.description,
                                "level": course.level.name,
                                "category": course.category.name,
                            }
                            trainer_data["courses"].append(course_data)

                        result.append(trainer_data)
                        trainer_ids.add(trainer.id)
            return JsonResponse(result, safe=False)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


def custom_404(request, exception):
    return render(request, "error/custom_404.html")


def send_simple_email(request):
    url = request.META.get("HTTP_REFERER")

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            subject = "Subject here 3"
            message = "Here is the message 3."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]

        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
            fail_silently=False,
        )
        return JsonResponse(
            {
                "status": "success",
                "message": "Your message has been sent successfully!",
            }
        )

    else:
        form = ContactForm()
        # Return error if the form is invalid
        return JsonResponse(
            {
                "status": "error",
                "message": "Form validation failed. Please correct the errors.",
            }
        )

    # return HttpResponseRedirect(url)


def send_custom_email(request):
    subject = "Custom Email Subject"
    body = "This is the body of the email."
    from_email = "your_email@gmail.com"
    to_email = ["recipient1@example.com"]

    email = EmailMessage(subject, body, from_email, to_email)
    email.send()
    return redirect("home")


def send_html_email():
    subject = "HTML Email"
    html_content = "<h1>Here is the HTML email</h1><p>This is the body.</p>"
    from_email = "your_email@gmail.com"
    to_email = ["recipient@example.com"]

    email = EmailMessage(subject, html_content, from_email, to_email)
    email.content_subtype = "html"  # Set content to HTML
    email.send()


# ? -------------------------- DATA API --------------------------


def short_format_data(category_name):
    trainers = Trainer.objects.prefetch_related(
        models.Prefetch(
            "courses", queryset=Course.objects.filter(category=category_name)
        )
    ).all()

    result = []

    for trainer in trainers:
        trainer_data = {
            "name": trainer.fullname,
            "image": trainer.image.url,
            "profession": trainer.profession,
            "courses": [],
        }
        for course in trainer.courses.all():
            course_data = {
                "category": course.category.name,
                "level": course.level,
                "image": course.image.url,
                "description": course.description,
            }
            trainer_data["courses"].append(course_data)

        # Only add the trainer to the result if they have courses in the specified category
        if trainer_data["courses"]:
            result.append(trainer_data)
    print(result)
    return JsonResponse(result, safe=False)


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
