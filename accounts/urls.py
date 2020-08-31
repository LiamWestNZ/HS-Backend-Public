
from django.urls import path

from .views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
)
app_name = 'accounts'
urlpatterns = [
    path('register/', registration_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),

]
