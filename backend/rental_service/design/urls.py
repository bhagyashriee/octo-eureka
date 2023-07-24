from django.urls import path
from .views import RentalRegistrationView, CarReturnView, get_returned_cars

urlpatterns = [
    path('rental-registration/', RentalRegistrationView.as_view(), name='rental-registration'),
    path('car-return/', CarReturnView.as_view(), name='car-return'),
    path('get-returned-cars/', get_returned_cars, name='get_returned_cars'),
]
