from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from crops.models import Crop
from users.serializers import UserSerializer, UserCropSerializer
from users.models import FarmcareUser, UserCrop
from users.storage import ImageBBStorage
from crops.crop_lens import crop_lens


class UserViewSet(ModelViewSet):
    '''
    A view of all users in the system.
    All CRUD (create, read, update, delete) options available
    '''
    permission_classes = [AllowAny]
    queryset = FarmcareUser.objects.all()
    serializer_class = UserSerializer


class UserDashboardView(RetrieveAPIView):
    '''
    A user's dashboard view (login required)
    This view is readonly.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = FarmcareUser.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def get(self, request):
        try:
            user = request.user
            status_code = status.HTTP_200_OK
            response = {
                'user': [{
                    'first_name': user.first_name,
                    'crops': user.crops.all()[:10],
                    # 'crops_with_diseases' : user.crops.filter(disease__isnull=False).count(),
                    'zipcode': user.zipcode,
                }]
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'error': str(e)
            }
        return Response(response, status=status_code)


class AddUserCropView(CreateAPIView):
    '''
    Used to create user-crop relationships.
    The uploaded crop image is stored externally and the url to that image is stored on-premise.
    This alleviates us from having to serve files ourselves.
    '''
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        crop_name = request.data['name'].lower()
        crop_image = request.data['image']

        storage = ImageBBStorage()
        image_url = storage.save(crop_name, crop_image)
        print(crop_name)

        crop, created = Crop.objects.get_or_create(
            name=crop_name,
            image=image_url
        )

        user_crop: UserCrop = UserCrop(
            user=request.user,
            crop=crop,
            user_submitted_image=image_url
        )

        user_crop.save()
        detected_name = crop_lens.crop_lens(image_url)
        temp = detected_name.split('__')
        detected_crop = temp[0]
        disease = temp[1].replace('_', ' ')
        serializer = UserCropSerializer(user_crop)

        return Response(
            {
                'data' : serializer.data,
                'detected_crop': detected_crop,
                'disease' : disease
            },
            status=status.HTTP_201_CREATED)
