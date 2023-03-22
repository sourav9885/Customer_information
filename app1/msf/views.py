from django.shortcuts import render

# Create your views here.
#from rest_framework import generics
from .models import Address, Customer, Car
from .serializers import AddressSerializer, CustomerSerializer, CarSerializer
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from .models import Address, Customer, Car
from .forms import CarForm
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Car, Address
from .serializers import CustomerSerializer, CarSerializer, AddressSerializer,CustomerCarAddressSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer

def HomePage(request):
    if request.method=='POST':
        return redirect('customerpage')
       
    return render(request,'add.html')

def customerpage(request):

    #form=CustomerForm()

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        age=request.POST['age']
        date_of_birth=request.POST['date_of_birth']
        phone=request.POST['phone']
        my_model_save=Customer(first_name=first_name,last_name=last_name,email=email, age=age, date_of_birth=date_of_birth, phone=phone )
        my_model_save.save()
        return redirect('addresspage')
    return render(request,'customer_details.html')
      
def addresspage(request):
    if request.method=='POST':
        street_name=request.POST['street_name']
        pincode=request.POST['pincode']
        city=request.POST['city']
        state=request.POST['state']
        country_code=request.POST['country_code']
        my_model_save2=Address(street_name=street_name, pincode=pincode, city=city,state=state,country_code=country_code)
        my_model_save2.save()
        return redirect('carinfopage')
    return render(request,'customer_address.html')

def carinfopage(request):
    form=CarForm()

    if request.method=='POST':
        form=CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={'form':form}
    return render(request,"car_info.html",context)



class CustomerCarAddressView(APIView):
    def get(self, request, pk):
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response(status=404)

        serializer = CustomerCarAddressSerializer(customer)
        return Response(serializer.data)



@api_view(['GET'])
def get_all_data(request):
    customers = Customer.objects.all()
    cars = Car.objects.all()
    addresses = Address.objects.all()
    customer_serializer = CustomerSerializer(customers, many=True)
    car_serializer = CarSerializer(cars, many=True)
    address_serializer = AddressSerializer(addresses, many=True)
    data = {
        'customers': customer_serializer.data,
        'cars': car_serializer.data,
        'addresses': address_serializer.data,
    }
    return Response(data)

@api_view(['POST'])
def create_data(request):
    customer_serializer = CustomerSerializer(data=request.data['customer'])
    car_serializer = CarSerializer(data=request.data['car'])
    address_serializer = AddressSerializer(data=request.data['address'])
    if customer_serializer.is_valid() and car_serializer.is_valid() and address_serializer.is_valid():
        customer_serializer.save()
        car_serializer.save()
        address_serializer.save()
        return Response({'success': True})
    else:
        return Response({'success': False, 'errors': {
            'customer': customer_serializer.errors,
            'car': car_serializer.errors,
            'address': address_serializer.errors,
        }})





class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
class AllDataSerializer(serializers.Serializer):
    customers = CustomerSerializer(many=True)
    cars = CarSerializer(many=True)
    addresses = AddressSerializer(many=True)

class AllDataViewSet(viewsets.ViewSet):
    def list(self, request):
        customers = Customer.objects.all()
        cars = Car.objects.all()
        addresses = Address.objects.all()

        serializer = AllDataSerializer({
            'customers': customers,
            'cars': cars,
            'addresses': addresses
        })

        return Response(serializer.data)
