from django.urls import path


from .views import (
    booking_view,
    new_booking,
    booking_history,
    service_create,
    service_update,
)
app_name = 'booking'
urlpatterns = [
    path('home', booking_view, name='booking_home'),
    path('new', new_booking, name='new_booking'),
    path('history', booking_history, name='history'),
    path('createS', service_create, name='createS'),
	path('editS', service_update, name='editS'),

]
