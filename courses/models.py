from django.db import models
import os

def get_image_upload_path(instance, filename):
    """
    Generate the upload path for the image based on the product's name.
    Spaces in the name are replaced with underscores.
    """
    # Generate folder name by replacing spaces with underscores
    folder_name = instance.name.replace(" ", "_")

    # Construct the full upload path
    return os.path.join("courses", folder_name, filename)

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=200,unique=True, verbose_name="Class Name",help_text="enter class name")
    description=models.TextField(blank=True,null=True,max_length=300)
    image=models.ImageField(upload_to=get_image_upload_path, default="courses/course_avatar.jpg")
    date=models.DateTimeField(auto_now=True)
    created_date=models.DateTimeField(auto_now_add=True)
    available=models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.name}"