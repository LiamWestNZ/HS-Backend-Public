from django import forms
from .models import Services, Services, Orders


class ServiceCreateForm(forms.ModelForm):

	class Meta:
		model = Services
		fields = (
			'name','description','price','category'
			)

class ServiceUpdateForm(forms.ModelForm):

	class Meta:
		model = Services
		fields = (
			'name','description','price','category'
			)

class OrderForm(forms.ModelForm):
	services = forms.CharField(max_length=30)
	pet = forms.CharField(max_length=30)
	dateBooked = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'], 
    )
	timeBooked = forms.TimeField()

	class Meta:
		model = Orders
		fields = (
			'services','pet','dateBooked', 'timeBooked')