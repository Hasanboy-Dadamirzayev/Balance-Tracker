from rest_framework.serializers import *
from .models import *

class TransitSerializer(ModelSerializer):
    class Meta:
        model = Tranzit
        fields = "__all__"

        extra_kwargs = {
            'created_at': {
                'read_only': True
            },
            'user': {
                'read_only': True
            },
        }

