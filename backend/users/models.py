from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import FarmcareUserManager
from crops.models import Crop

class FarmcareUser(AbstractUser):

    zipcode = models.IntegerField(default=11367)
    crops = models.ManyToManyField(Crop)

    class Meta:
        db_table = 'users'