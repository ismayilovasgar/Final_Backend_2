from django.urls import path, include
from pages import views

# app_name="pages"

urlpatterns = [
    path("", views.index, name="home"),  # http://127.0.0.1:8000/
    path("pricing/", views.pricing, name="pricing"),  # http://127.0.0.1:8000/pricing
    path(
        "features/", views.features, name="features"
    ),  # http://127.0.0.1:8000/features
    path(
        "download/", views.download, name="download"
    ),  # http://127.0.0.1:8000/download
    path(
        "lifestyle/", views.lifestyle, name="lifestyle"
    ),  # http://127.0.0.1:8000/download
    path(
        "programs/", views.programs, name="programs"
    ),  # http://127.0.0.1:8000/programs
    path(
        "class_01/detail/<int:id>/", views.class01_detail_page, name="class01_detail"
    ),  # http://127.0.0.1:8000/programs
    path(
        "class_02/", views.class02__page, name="class02"
    ),  # http://127.0.0.1:8000/class_02
    path(
        "class_02/category/<str:category_name>/",views.class02_trainers,name="class02_trainers",
    ),  # http://127.0.0.1:8000/programs
    path(
        "singleblog/<int:id>/", views.blog_detail, name="blog_detail"
    ),  # http://127.0.0.1:8000/single_blog/id
    path(
        "programs/detail/<int:id>/", views.programs_detail, name="programs_detail"
    ),  # http://127.0.0.1:8000/programs/detail/id/
    path("error/", views.custom_404, name="custom_404"),
    path("joinmebymail/", views.join_simple_email, name="send_mail"),
    path("sendmail/", views.send_simple_email, name="send_simple_mail"),
]
