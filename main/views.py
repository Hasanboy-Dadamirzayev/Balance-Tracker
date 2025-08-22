from rest_framework.generics import (
    CreateAPIView, get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from .serializers import *
from .models import *
from rest_framework.permissions import *

class TranzitListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tranzit.objects.all()
    serializer_class = TransitSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        tranzit = serializer.save(user=self.request.user)


        user = self.request.user
        if tranzit.type == 'Income':
            user.balance += tranzit.amount
        elif tranzit.type == 'Expense':
            user.balance -= tranzit.amount
        user.save()

class TranzitRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Tranzit.objects.all()
    serializer_class = TransitSerializer







