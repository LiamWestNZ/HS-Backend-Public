from django.contrib import admin
from django.urls import path

from .views import (
    profile_detail_api_view,
    profile_update_api_view,
)
urlpatterns = [
    path('<str:username>', profile_detail_api_view),
    path('<str:username>/edit', profile_update_api_view),
]