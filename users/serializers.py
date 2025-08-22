from rest_framework.serializers import *
from .models import *

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'balance', 'date_joined']

        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'date_joined': {
                'required': False
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'balance', 'date_joined']