import os
from django.db import models


def get_review_upload_path(instance, filename):
    folder_name = instance.author.replace(" ", "_")
    return os.path.join("review", folder_name, filename)


class Review(models.Model):
    author = models.CharField(max_length=40, default="Dorthy Runolfsdottir")
    logo = models.ImageField(upload_to=get_review_upload_path, default="review.png")
    content = models.TextField(
        max_length=250,
        default="The greatest fitness app. It's clear the makers behind this thing use it every week, because it is so perfect.",
    )
    desginer = models.CharField(max_length=40, default="Lead Visual Designer at UI8")

    def __str__(self) -> str:
        return f"{self.author} "


class Contact(models.Model):
    email = models.EmailField(max_length=250)

    def __str__(self) -> str:
        return f"${self.email}"
