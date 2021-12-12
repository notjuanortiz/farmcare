from django.contrib import admin
from django import forms

# Register your models here.
from .models import Crop, CompanionCrop

class CompanionCropInline(admin.TabularInline):
    model = CompanionCrop

class CropAdmin(admin.ModelAdmin):
    inlines = [
        CompanionCropInline
    ]

admin.site.register(Crop)