from rest_framework import viewsets

from users.serializers import UserSerializer
from users.models import FarmcareUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = FarmcareUser.objects.all()
    serializer_class = UserSerializer