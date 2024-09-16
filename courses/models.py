from django.db import models
from trainers.models import Trainer
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# ? Common Uses ----------------------------------------------------
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


DIFFICULTY_CHOICES = [
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced"),
]

TIME_OF_DAY_CHOICES = [
    ("Morning", "Morning"),
    ("Afternoon", "Afternoon"),
    ("Evening", "Evening"),
]
INTENSITY_CHOICES = [
    ("Level 1", "Level 1"),
    ("Level 2", "Level 2"),
    ("Level 3", "Level 3"),
]
STYLE_CHOICES = [
    ("Morning Yoga", "Morning Yoga"),
    ("Vinyasa Yoga", "Vinyasa Yoga"),
    ("Acro Yoga", "Acro Yoga"),
]


#!-------------------------------------------------------------------
class Level(models.Model):
    name = models.CharField(
        max_length=25,
        choices=DIFFICULTY_CHOICES,
        default="Intermediate",
        help_text="Select the difficulty level of the course",
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class TimeOfDay(models.Model):
    name = models.CharField(
        max_length=25,
        choices=TIME_OF_DAY_CHOICES,
        default="Morning",
        help_text="Select the time of day for this course.",
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Intensity(models.Model):
    name = models.CharField(
        max_length=25,
        choices=INTENSITY_CHOICES,
        default="Level 2",
        help_text="Select the intensity level of the exercise.",
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Style(models.Model):
    name = models.CharField(
        max_length=25,
        choices=STYLE_CHOICES,
        default="Morning Yoga",
        help_text="Select the style of this course",
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=CATEGORY_CHOICES,
        default="Yoga",
        unique=True,
    )
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=TAG_CHOICES,
        default="Lifestyle",
        unique=True,
    )
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Class Name",
        help_text="enter class name",
    )
    title = models.TextField(
        blank=True, null=True, max_length=300, default="Sweet and tone"
    )
    description = models.TextField(blank=True, null=True, max_length=300)
    image = models.ImageField(upload_to=get_image_upload_path, default="course.jpg")
    duration = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),  # Minimum value of 1
            MaxValueValidator(59),  # Maximum value of 59
        ],
    )
    classes = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),  # Minimum value of 1
            MaxValueValidator(10),  # Maximum value of 10
        ],
    )
    date = models.DateTimeField(auto_now=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    available = models.BooleanField(default=True)

    # ? ORM Relationship
    #
    trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="coursess"
    )
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name="courses"
    )
    tags = models.ManyToManyField(Tag)
    #
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING, null=True)
    time_day = models.ForeignKey(TimeOfDay, on_delete=models.DO_NOTHING, null=True)
    intensity = models.ForeignKey(Intensity, on_delete=models.DO_NOTHING, null=True)
    style = models.ForeignKey(Style, on_delete=models.DO_NOTHING, null=True)
    #
    students = models.ManyToManyField(User, blank=True, related_name="courses_joined")

    def __str__(self) -> str:
        return f"{self.name}"
