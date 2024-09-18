from django.contrib import admin
from .models import Review, Contact


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author",)

    class Meta:
        model = Review


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email",)

    class Meta:
        model = Contact
