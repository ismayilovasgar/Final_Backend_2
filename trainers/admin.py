from django.contrib import admin
from .models import Trainer


# Register your models here.
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("fullname",)
    list_filter = ("fullname",)
    search_fields = ("fullname", "profession")

    class Meta:
        model = Trainer
