from django.contrib import admin

# Register your models here.
from users.models import FarmcareUser

admin.site.register(FarmcareUser)