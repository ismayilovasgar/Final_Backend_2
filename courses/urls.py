from django.urls import path
from courses import views

# Define the app namespace
app_name = 'courses'  


urlpatterns = [
    # path('',views.course_list,name="courses"),  
    # path("<slug:category_slug>/<int:course_id>/",views.course_detail,name="course_detail"),
    path("categories/<slug:category_slug>/",views.categories_detail,name="courses_by_category"),
    path("tags/<slug:tag_slug>/",views.tags_detail,name="courses_by_tag"),
    path("programs/list/",views.show_by_array,name="show_by_array"),
    path("programs/<str:text>/",views.show_by_text,name="show_by_text"),
    path("programs/unenrolled/",views.user_unenrolled_course,name="User_unenrolled_courses"),
    #! enroll and release course
    path("enroll/<int:course_id>/",views.enroll_course,name="enroll_course"),
    path("release/<int:course_id>/",views.release_course,name="release_course"),
    path("dashboard/",views.dashboard__page,name="dashboard"),
] 