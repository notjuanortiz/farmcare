from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import FarmcareUser


class FarmcareUserCreationForm(UserCreationForm):

    class Meta:
        model = FarmcareUser
        fields = ('email',)


class FarmcareUserChangeForm(UserChangeForm):

    class Meta:
        model = FarmcareUser
        fields = ('email',)