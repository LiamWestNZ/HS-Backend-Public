from django.contrib import admin
from django.urls import path

from .views import (
    pet_detail_api_view,
    pet_list_api_view,
)
urlpatterns = [
    path('<int:id>', pet_detail_api_view),
    path('<str:username>', pet_list_api_view),
]