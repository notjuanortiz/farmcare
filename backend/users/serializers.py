from rest_framework import serializers
from django.contrib.auth.models import User

from users.models import FarmcareUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = FarmcareUser
        fields = ('id', 'email', 'zipcode', 'crops')