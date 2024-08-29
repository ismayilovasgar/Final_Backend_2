from django.db import models
import os

def get_image_upload_path(instance, filename):
    folder_name = instance.name.replace(" ", "_")
    return os.path.join("courses", folder_name, filename)


CATEGORY_CHOICES = [
        ("Yoga", "Yoga"),
        ("Fitness & Gym", "Fitness & Gym"),
        ("Gymnastics", "Gymnastics"),
        ("Running", "Running"),
    ]


TAG_CHOICES = [
        ("Lifestyle", "Lifestyle"),
        ("Fitness", "Fitness"),
        ("Mindfulness", "Mindfulness"),
    ]

class Category(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,choices=CATEGORY_CHOICES,default='Yoga')
    slug = models.SlugField(max_length=50,null=True,blank=True,unique=True)

    def __str__(self) -> str:
        return f"{self.name}"
    

class Tag(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,choices=TAG_CHOICES,default='Lifestyle')
    slug = models.SlugField(max_length=50,null=True,blank=True,unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Course(models.Model):
    name=models.CharField(max_length=200,unique=True, verbose_name="Class Name",help_text="enter class name")
    description=models.TextField(blank=True,null=True,max_length=300)
    image=models.ImageField(upload_to=get_image_upload_path, default="courses/course_avatar.jpg")
    date=models.DateTimeField(auto_now=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    available=models.BooleanField(default=True)

    #? ORM Relationship
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    tag=models.ManyToManyField(Tag,on_delete=models.CASCADE,)
    def __str__(self) -> str:
        return f"{self.name}"