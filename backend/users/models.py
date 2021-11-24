from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import FarmcareUserManager
from crops.models import Crop

class FarmcareUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    zipcode = models.IntegerField(default=11367)
    crops = models.ManyToManyField(Crop)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = FarmcareUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'