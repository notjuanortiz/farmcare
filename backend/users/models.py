from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext as _
from django.utils import timezone

from .managers import FarmcareUserManager
from crops.models import Crop


class FarmcareUser(AbstractBaseUser, PermissionsMixin):
    '''
    The base user. This class allows us to add extra fields to the user.
    By default, only username, password are defined.
    '''
    email = models.EmailField(_('email address'), unique=True, null=False)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    zipcode = models.IntegerField(default=11367)
    crops = models.ManyToManyField(Crop, through='UserCrop')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Allows logging in by email only
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = FarmcareUserManager()

    def __str__(self):
        return self.email

    class Meta:
        # Django automatically names a database table after the model object name. We're overriding it here.
        db_table = 'users'


class UserCrop(models.Model):
    '''
    An intermediate table that enables a many-to-many relationship between user and crop
    '''
    user = models.ForeignKey(FarmcareUser, on_delete=CASCADE, primary_key=True)
    crop = models.ForeignKey(Crop, on_delete=CASCADE)
    user_submitted_image = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    class Meta:
       # managed = False
        constraints = [
            # composite key constraint
            UniqueConstraint(fields=['user', 'crop'], name='user_crop_id')
        ]
        db_table = 'users_crops'
