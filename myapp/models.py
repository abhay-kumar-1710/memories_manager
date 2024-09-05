from django.db import models

# Create your models here.
class ImageUploader(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateField()
    image = models.ImageField(upload_to="memories")