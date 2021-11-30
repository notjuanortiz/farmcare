from django.db import models
# Create your models here.

# Images should be stored into the database but we're storing them locally due to time constraints
def crop_image_directory(instance, filename: str):
    return 'images/crop_{0}/{1}'.format(instance.name, filename.lower())

class Crop(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=crop_image_directory)

    class Meta:
        verbose_name_plural = 'crops'
        ordering = ['name']

    def __str__(self):
        return self.name