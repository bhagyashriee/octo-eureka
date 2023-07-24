from django.urls import path
from .views import rented_cars, RentalRegistrationView, CarReturnView

urlpatterns = [
    path('rental-registration/', RentalRegistrationView.as_view(), name='rental-registration'),
    path('car-return/', CarReturnView.as_view(), name='car-return'),
    path('car-return/<str:booking_number>/', CarReturnView.as_view(), name='car_return'),
    path('rented_cars/', rented_cars.as_view(), name='rented_cars'),
]

