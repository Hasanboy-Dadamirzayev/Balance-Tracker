from django.contrib import admin
from django.urls import path, include
from main.urls import *
from users.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', include('main.urls')),
]
