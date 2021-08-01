from django.urls import path
from .views import *


urlpatterns = [
    path('', UserRegisterView.as_view(), name='register'),
]
