from django.db import models
from django.conf import settings
from django.db.models import Q

from pets.models import Pet

User = settings.AUTH_USER_MODEL

class Services(models.Model):
	GROOMING = 'Grm'
	BEDANDBATH = 'b&b'
	PHOTOGRAPHY = 'Photo'
	ADDONS = 'Ao'
	CATEGORY_CHOICES = [(GROOMING, 'Grooming'),(BEDANDBATH, 'Bed and Bath'),(PHOTOGRAPHY,'Photography'),(ADDONS,'Add-Ons')]
	name = models.CharField(max_length=30, null=True)
	description = models.CharField(max_length=150, null=True)
	price = models.DecimalField(max_digits=4, decimal_places=1, default=0)
	category = models.CharField(max_length=21, choices=CATEGORY_CHOICES, default=GROOMING)

	class Meta:
		verbose_name_plural = 'Services'

class Orders(models.Model):
	ref = models.CharField(max_length=15, default=1)
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
	paid = models.BooleanField(default=False)
	#paymentDetails
	services = models.ManyToManyField(Services)
	dateMade = models.DateTimeField(auto_now_add=True, null=True)
	dateBooked = models.DateTimeField(auto_now=False, null=True)
	timeBooked = models.TimeField(auto_now=False, null=True)
	pet = models.ManyToManyField(Pet)


	class Meta:
		verbose_name_plural = 'Orders'


