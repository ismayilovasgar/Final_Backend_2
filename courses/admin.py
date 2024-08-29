from django.contrib import admin

from .models import Course,Category,Tag
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=("name","created_date","category")
    list_filter=("available",)
    search_fields=("name",)

    class Meta:
        model=Course


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}

    class Meta:
        model=Category

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}

    class Meta:
        model=Tag