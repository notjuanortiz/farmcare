from rest_framework.viewsets import ModelViewSet
from users.serializers import FarmcareRegisterSerializer
from users.models import FarmcareUser

class UserViewSet(ModelViewSet):
    queryset = FarmcareUser.objects.all()
    serializer_class = FarmcareRegisterSerializer