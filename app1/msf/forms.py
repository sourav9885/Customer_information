from django import forms
from .models import Customer,Car

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'age', 'date_of_birth', 'phone', 'email']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

# class AddressForm(forms.ModelForm):a
#     class Meta:
#         model = Address
#         fields = ['street_name', 'pincode', 'city', 'state', 'country_code']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model_name', 'manufacturing_date', 'manufacturer', 'color']
        widgets = {
            'manufacturing_date': forms.DateInput(attrs={'type': 'date'}),
        }
