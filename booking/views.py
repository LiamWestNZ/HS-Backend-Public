from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

from .forms import ServiceCreateForm, ServiceUpdateForm, OrderForm
from .models import Services, Orders

# scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('hsbooking.json', scope)
# client = gspread.authorize(creds)

def booking_view(request):
    context = {}
    return render(request, 'booking/booking.html', context)

def new_booking(request):
	context = {}
	return render(request, 'booking/new_booking.html', context)
# 	user = request.user
# 	context = {}
# 	sheet = client.open('hsbooking').sheet1
# 	if request.user.is_authenticated:
# 		name = user.first_name + " " + user.last_name
# 		email = user.email
# 		phone = user.number
# 	if request.POST:
# 		dt = datetime.datetime.now()
# 		form = OrderForm(request.POST)
# 		if form.is_valid():
# 			form.save(commit=False)
# 			pet = form.cleaned_data.get('pet')
# 			date = form.cleaned_data.get('dateBooked')
# 			time = form.cleaned_data.get('time')
# 			sheet.append_row[(dt, name, pet, date, time, email)]
# 			form.save()
# 		else:
# 			context = {form: 'form'}
# 	else:
# 		form = OrderForm()
# 		context = {form: 'form'}

def booking_history(request):
	context = {}
	return render(request, 'booking/history.html', context)

def service_create(request):
	context = {}
	
	if request.POST:
		form = ServiceCreateForm(request.POST)
		if form.is_valid():
			form.save()

		else:
			context = {"form": form}
	else:
		form = ServiceCreateForm()
		context = {"form": form}
	return render(request, 'booking/serviceCreate.html', context)

def service_update(request):
	obj = Services.objects.get(id=id)
	form = ServiceUpdateForm(request.POST or None, instance=obj)
	if request.POST:
		if form.is_valid():
			form.save()

	context={"form": form}
	return render(request, 'booking/serviceUpdate.html', context)