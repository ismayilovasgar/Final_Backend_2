import os
from django.db import models

# Create your models here.


def get_image_upload_path(instance, filename):
    folder_name = instance.fullname.replace(" ", "_")
    return os.path.join("trainers", folder_name, filename)


# ---------------------------------------------------------------------------------
class Trainer(models.Model):
    fullname = models.CharField(max_length=40)
    profession = models.CharField(max_length=40)
    image = models.ImageField(upload_to=get_image_upload_path, default="profile.jpg")
    facebook = models.URLField(
        max_length=100, blank=True, null=True, default="https://www.facebook.com/"
    )
    twitter = models.URLField(
        max_length=100, blank=True, null=True, default="https://twitter.com/"
    )
    instagram = models.URLField(
        max_length=100, blank=True, null=True, default="https://www.instagram.com/"
    )
    linkedin = models.URLField(
        max_length=100, blank=True, null=True, default="https://www.linkedin.com"
    )

    def __str__(self) -> str:
        return f"{self.fullname}"
