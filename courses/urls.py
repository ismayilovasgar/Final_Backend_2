from django.urls import path
from courses import views

urlpatterns = [
    path('',views.course_list,name="courses"),   # http://127.0.0.1:8000/courses
    path("<slug:category_slug>/<int:course_id>/",views.course_detail,name="course_detail"),
    path("categories/<slug:category_slug>/",views.categories_detail,name="courses_by_category"),
    path("tags/<slug:tag_slug>/",views.tags_detail,name="courses_by_tag"),
] 