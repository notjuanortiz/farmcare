from django.db import models
# Create your models here.

def crop_image_directory(instance, filename):
    return 'images/crop_{0}/{1}'.format(instance.crop.name, filename)

class Crop(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=crop_image_directory)

    class Meta:
        verbose_name_plural = 'crops'
        ordering = ['name']

    def __str__(self):
        return self.name