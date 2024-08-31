from django.urls import path
from courses import views

app_name = 'courses'  # Define the app namespace


urlpatterns = [
    path('',views.course_list,name="courses"),  
    path("<slug:category_slug>/<int:course_id>/",views.course_detail,name="course_detail"),
    path("categories/<slug:category_slug>/",views.categories_detail,name="courses_by_category"),
    path("tags/<slug:tag_slug>/",views.tags_detail,name="courses_by_tag"),
    path("programs/list/",views.show_by_array,name="show_by_array"),
] 