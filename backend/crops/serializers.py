from rest_framework import serializers
from .models import Crop


class CropSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    image = serializers.CharField()

    class Meta:
        model = Crop
        fields = ('id', 'name', 'image')
