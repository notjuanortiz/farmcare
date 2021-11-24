from django.db import models

# Create your models here.

class Crop(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    
    class Meta:
        verbose_name_plural = 'crops'
    def __str__(self):
        return self.name