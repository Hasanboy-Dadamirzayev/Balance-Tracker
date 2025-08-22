from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view()),
    path('my-account/', MyAccountRetrieveAPIView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteAPIView.as_view()),
    path('get-token/', obtain_auth_token),

]