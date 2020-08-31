from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.models import Accounts


def home_page(request):
	context = {}
	user = request.user
	if user.is_authenticated:
		return render(request, 'home.html', context)
	else:
		return redirect('accounts:login')
