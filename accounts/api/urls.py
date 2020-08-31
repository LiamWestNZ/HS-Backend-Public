from django.contrib import admin
from django.urls import path

from .views import (
    registration_view,
    CustomAuthToken
)

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register', registration_view),
    path('login', CustomAuthToken.as_view()),
]