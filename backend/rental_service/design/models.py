from django.db import models

class Rental(models.Model):
    COMPACT = 'Compact'
    PREMIUM = 'Premium'
    MINIVAN = 'Minivan'
    
    CAR_CATEGORY_CHOICES = [
        (COMPACT, 'Compact'),
        (PREMIUM, 'Premium'),
        (MINIVAN, 'Minivan'),
    ]

    booking_number = models.CharField(max_length=10, unique=True, null=False)
    customer_name = models.CharField(max_length=100)
    car_category = models.CharField(max_length=10, choices=CAR_CATEGORY_CHOICES)
    rental_date = models.DateTimeField()
    pickup_mileage = models.PositiveIntegerField()
    actual_return_date = models.DateTimeField(null=True, blank=True)
    return_mileage = models.PositiveIntegerField(null=True, blank=True)
    number_of_days = models.PositiveIntegerField(default=0)
    number_of_kilometers = models.PositiveIntegerField(default=0)  # Add the number_of_kilometers field

    def __str__(self):
        return f'Booking #{self.booking_number} - {self.customer_name}'


class ReturnCar(models.Model):
    car_category = models.CharField(max_length=10, choices=Rental.CAR_CATEGORY_CHOICES)
    booking_number = models.CharField(max_length=50)
    return_date = models.DateTimeField()
    actual_return_date = models.DateTimeField(null=True, blank=True)
    return_mileage = models.PositiveIntegerField()
    number_of_kilometers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Car Return #{self.booking_number}"
