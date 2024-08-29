from django.shortcuts import render
from .models import Course,Category

# Create your views here.
def course_list(request):
    return render(request,"home.html")

def course_detail(request,category_slug,course_id):
    course=Course.objects.get(category__slug=category_slug,id=course_id)
    context={"course":course}

    return render(request,"course_detail.html",context)