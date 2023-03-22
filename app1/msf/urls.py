#API urls 
from django.urls import path,include
from msf import views
from rest_framework import routers
from .views import CustomerViewSet, CarViewSet, AddressViewSet, AllDataViewSet
from django.urls import path,include
from msf import views

router = routers.DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('cars', CarViewSet)
router.register('addresses', AddressViewSet)
router.register('alldata', AllDataViewSet, basename='alldata')


urlpatterns = [
    #front urls
    path('',views.HomePage,name='home'),
    path('customer/', views.customerpage, name='customerpage'),
    path('customeraddress/',views.addresspage,name='addresspage'),
    path('carinfo/',views.carinfopage,name='carinfopage'),

    #APi Urls
    path('customer_address_car_data/', views.get_all_data),
    path('data/create/', views.create_data),
    path('', include(router.urls)), 
]

