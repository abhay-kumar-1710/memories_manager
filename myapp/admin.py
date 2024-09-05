from django.contrib import admin
from myapp.models import ImageUploader

# Register your models here.

@admin.register(ImageUploader)
class ImageUploaderAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "date", "image"]