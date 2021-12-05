from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from users.models import FarmcareUser

class FarmcareRegisterSerializer(RegisterSerializer):
    zipcode = serializers.IntegerField(required = False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['zipcode'] = self.validated_data.get('zipcode')
        data_dict['crops'] = self.validated_data.get('crops')
        return data_dict

class FarmcareUserDetailsSerializer(UserDetailsSerializer):
    model = FarmcareUser
    fields = (
        'pk',
        'email',
        'zipcode',
        'crops'
        )
    read_only_fields = ('pk')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmcareUser
        fields = [
            'first_name',
            'crops',
        ]