from django.urls import path
from .views import *

urlpatterns = [
    path('transactions/', TranzitListCreateAPIView.as_view()),
    path('transactions/<int:pk>/', TranzitRetrieveUpdateDestroyAPIView.as_view()),
]