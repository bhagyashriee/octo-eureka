from datetime import timedelta
from django.http import JsonResponse
from django.views import View
import pytz

from .models import Rental, ReturnCar

def calculate_rental_price(car_category, total_days, number_of_kilometers):
    base_day_rental = 100  
    kilometer_price = 2  

    if car_category == Rental.COMPACT:
        price = base_day_rental * total_days
    elif car_category == Rental.PREMIUM:
        price = base_day_rental * total_days * 1.2 + kilometer_price * number_of_kilometers
    elif car_category == Rental.MINIVAN:
        price = base_day_rental * total_days * 1.7 + (kilometer_price * number_of_kilometers * 1.5)
    else:
        price = 0.0

    return price

def get_response_data(return_car):
    try:
        rental = Rental.objects.get(booking_number=return_car.booking_number)
    except Rental.DoesNotExist:
        return None

    total_days = (return_car.actual_return_date - rental.rental_date).days + 1

    response_data = {
        "booking_number": return_car.booking_number,
        "return_date": return_car.return_date.strftime('%Y-%m-%d %H:%M:%S'),
        "actual_return_date": return_car.actual_return_date.strftime('%Y-%m-%d %H:%M:%S') if return_car.actual_return_date else None,
        "return_mileage": return_car.return_mileage,
        "price": calculate_rental_price(rental.car_category, total_days, return_car.number_of_kilometers),
        "number_of_kilometers": return_car.number_of_kilometers,
        "car_category": str(return_car.car_category),
        "customer_name": rental.customer_name,
    }

    return response_data

class RentalRegistrationView(View):
    def get(self, request):
        rentals = Rental.objects.all()

        rental_data = []
        for rental in rentals:
            data = {
                "booking_number": rental.booking_number,
                "customer_name": rental.customer_name,
                "car_category": rental.car_category,
                "rental_date": rental.rental_date,
                "pickup_mileage": rental.pickup_mileage,
            }
            rental_data.append(data)

        return JsonResponse(rental_data, safe=False)

class CarReturnView(View):
    def get(self, request, booking_number=None):
        if booking_number is not None:
            try:
                return_car = ReturnCar.objects.get(booking_number=booking_number)
            except ReturnCar.DoesNotExist:
                return JsonResponse({"error": f"Return car with booking number {booking_number} not found."}, status=404)

            response_data = get_response_data(return_car)
            if response_data:
                return JsonResponse(response_data, safe=False)
            else:
                return JsonResponse({"error": f"No rental found for booking number {booking_number}."}, status=404)

        else:
            return_cars = ReturnCar.objects.all()
            booking_numbers = [car.booking_number for car in return_cars]

            if booking_numbers:
                return JsonResponse({"booking_numbers": booking_numbers}, safe=False)
            else:
                return JsonResponse({"error": "No returned cars found."}, status=404)
            
class rented_cars(View):
    def get(self, request):
        rental_booking_numbers = Rental.objects.values_list('booking_number', flat=True)
        returned_booking_numbers = ReturnCar.objects.values_list('booking_number', flat=True)
        pending_booking_numbers = list(set(rental_booking_numbers) - set(returned_booking_numbers))

        if pending_booking_numbers:
            return JsonResponse({"pending_booking_numbers": pending_booking_numbers}, safe=False)
        else:
            return JsonResponse({"error": "No pending booking numbers found."}, status=404)