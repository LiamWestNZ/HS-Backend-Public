from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home_page

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('pets/', include('pets.urls')),
    path('booking/', include('booking.urls')),
    path('api/accounts/', include('accounts.api.urls')),
    path('api/profile/', include('profiles.api.urls')),
    path('api/pets/', include('pets.api.urls')),


    ]
urlpatterns += staticfiles_urlpatterns()