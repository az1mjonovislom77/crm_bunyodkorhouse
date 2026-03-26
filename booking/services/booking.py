from django.db import transaction
from django.core.exceptions import ValidationError
from booking.models import Booking
from home.models import Home
from home.services.history import HomeService


@transaction.atomic
def create_booking(*, client, home, **extra):
    home = Home.objects.select_for_update().get(id=home.id)

    if home.home_status != Home.HomeStatus.AVAILABLE:
        raise ValidationError("Uy band yoki sotilgan")

    booking = Booking.objects.create(client=client, home=home, **extra)

    HomeService.change_status(home_id=home.id, new_status=Home.HomeStatus.SOLD, user=client)

    return booking


@transaction.atomic
def delete_booking(booking_id):
    booking = Booking.objects.select_related('home').get(id=booking_id)
    home = Home.objects.select_for_update().get(id=booking.home_id)

    booking.delete()

    if not home.bookings.exists():
        HomeService.change_status(home_id=home.id, new_status=Home.HomeStatus.AVAILABLE)
