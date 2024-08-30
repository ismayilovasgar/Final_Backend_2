from django.urls import path
from trainers.views import TrainerListView, TrainerDetailView

app_name = "trainers"  # Define the app namespace


urlpatterns = [
    path("", TrainerListView.as_view(), name="trainers"),
    path("trainer/<int:pk>", TrainerDetailView.as_view(), name="trainer_detail"),
]
