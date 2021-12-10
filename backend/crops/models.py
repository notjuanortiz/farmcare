from django.db import models
from django.db.models.constraints import UniqueConstraint 
from django.db.models.deletion import DO_NOTHING

def crop_image_directory(instance, filename: str):
    '''
    Images should be stored into the database but we're storing them locally due to time constraints
    '''
    return 'images/crop_{0}/{1}'.format(instance.name, filename.lower())

class Crop(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.CharField(max_length=255)
    companion = models.ManyToManyField('self', through='CompanionCrop')
    class Meta:
        ordering = ['name']
        db_table = 'crops'

class CompanionCrop(models.Model):
    crop = models.ForeignKey(Crop, related_name='crop', on_delete=DO_NOTHING)
    helper = models.ForeignKey(Crop, related_name='helped_by', on_delete=DO_NOTHING)
    description = models.TextField(max_length=50)
    class Meta:
        db_table = 'companion_crops'
        constraints = [
            UniqueConstraint(fields=['crop', 'crop'], name='unique_companion_crop')
        ]