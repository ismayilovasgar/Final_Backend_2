from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "created_date", "category")
    list_filter = ("available",)
    search_fields = ("name",)
    filter_horizontal = ("tags",)

    class Meta:
        model = Course


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Category


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = Tag


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        model = Level


@admin.register(TimeOfDay)
class TimeOfDayAdmin(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        model = TimeOfDay


@admin.register(Intensity)
class IntensityAdmin(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        model = Intensity


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        model = Style
