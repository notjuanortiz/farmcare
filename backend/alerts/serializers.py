from rest_framework import serializers

class AlertSerializer(serializers.Serializer):
    recipient = serializers.EmailField()
    message = serializers.CharField(allow_blank=True)