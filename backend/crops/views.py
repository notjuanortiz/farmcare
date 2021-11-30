from rest_framework.viewsets import ModelViewSet
from .models import Crop
from .serializers import CropSerializer

# Create your views here.

class CropViewSet(ModelViewSet):
   queryset = Crop.objects.all()
   serializer_class = CropSerializer