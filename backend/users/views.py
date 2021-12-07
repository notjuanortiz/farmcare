from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from users.serializers import UserSerializer
from users.models import FarmcareUser, UserCrop


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
                    'crops': user.crops.all()[:10].values('name'),
                    #'crops_with_diseases' : user.crops.filter(disease__isnull=False).count(),
                    'zipcode': user.zipcode,
                }]
            }
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'error': str(e)
            }
        return Response(response, status=status_code)


class CreateUserCropView(CreateAPIView):
    '''
    Used to create user-crop relationships
    '''
    serializer_class = UserCrop
    permission_classes = [IsAuthenticated]