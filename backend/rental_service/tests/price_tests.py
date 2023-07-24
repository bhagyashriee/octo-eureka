import pytest
from design.models import Rental, ReturnCar
from design.views import calculate_rental_price


@pytest.mark.parametrize("car_category, total_days, number_of_kilometers, expected_price", [
    ("Compact", 3, 1500, 3300),
    ("Premium", 4, 2000, 4900),
    ("Minivan", 5, 2500, 11525),
    ("Compact", 1, 500, 100),
    ("Premium", 2, 1000, 2400),
    ("Minivan", 7, 3000, 27150),
    # Add more test cases for different car categories and scenarios
])

def test_calculate_rental_price_invalid_car_category():
    # Test with an invalid car category
    assert calculate_rental_price("InvalidCategory", 3, 1500) == 0.0

def test_calculate_rental_price_zero_days_kilometers():
    # Test with zero days and kilometers
    assert calculate_rental_price("Compact", 0, 0) == 0.0
def test_calculate_primium_price():
    assert  calculate_rental_price("Premium",5,1000)==2600
def test_calculate_rental_price_invalid_car_category():
    # Test with an invalid car category
    assert calculate_rental_price("InvalidCategory", 3, 1500) == 0.0