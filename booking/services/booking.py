from django.db import transaction
from booking.models import Booking
from home.models import Home
from home.services.home import HomeService


@transaction.atomic
def delete_booking(booking_id, user=None):
    booking = Booking.objects.select_related('home').get(id=booking_id)
    home = Home.objects.select_for_update().get(id=booking.home_id)

    booking.delete()

    if not hasattr(home, 'booking'):
        HomeService.change_status(home_id=home.id, new_status=Home.HomeStatus.AVAILABLE, user=user)
