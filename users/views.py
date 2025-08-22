from rest_framework.generics import (
    CreateAPIView, get_object_or_404, RetrieveAPIView
)
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView
)


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class MyAccountRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    def get_object(self):
        return self.request.user

class UserRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer


