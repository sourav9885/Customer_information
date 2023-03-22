from rest_framework import serializers
from .models import Customer, Car, Address

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'age', 'date_of_birth', 'phone', 'email', 'id')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('model_name', 'manufacturing_date', 'manufacturer', 'color', 'id')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('street_name', 'pincode', 'city', 'state', 'country_code', 'id')

class CustomerCarAddressSerializer(serializers.ModelSerializer):
    car = CarSerializer()
    address = AddressSerializer()
    
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'age', 'date_of_birth', 'phone', 'email', 'id', 'car', 'address')
