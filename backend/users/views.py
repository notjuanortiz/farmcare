from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.serializers import JWTSerializer
from users.serializers import UserSerializer
from users.models import FarmcareUser


class UserDashboardView(RetrieveAPIView):
    permission_classes = (IsAuthenticated)
#    authentication_classes = JWTSerializer
    serializer_class = UserSerializer
    queryset = FarmcareUser.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.exists():
            return Response(user, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     obj = get_object_or_404(queryset, user=self.request.user)
    #     return obj

    # def get(self, request):
    #     try:
    #         auth_user = FarmcareUser.objects.get(user=request.user)
    #         status_code = status.HTTP_200_OK
    #         response = {
    #             'data': [{
    #                 'first_name': auth_user.first_name,
    #                 'crops': auth_user.admins.all()[:10],

    #             }]
    #         }
    #     except Exception as e:
    #         status_code = status.HTTP_400_BAD_REQUEST
    #         response = {
    #             'error': str(e)
    #         }
    #     return Response(response, status=status_code)
