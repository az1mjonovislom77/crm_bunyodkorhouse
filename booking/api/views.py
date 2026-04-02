from drf_spectacular.utils import extend_schema
from booking.models import Booking, PaymentTerm
from booking.api.serializers import BookingCreateSerializer, BookingGetSerializer, PaymentTermSerializer
from booking.services.booking import delete_booking
from common.base.views_base import BaseUserViewSet
from home.services.home import HomeService
from home.models import Home


@extend_schema(tags=['PaymentTerm'])
class PaymentTermViewSet(BaseUserViewSet):
    queryset = PaymentTerm.objects.all()
    serializer_class = PaymentTermSerializer


@extend_schema(tags=['Booking'])
class BookingViewSet(BaseUserViewSet):
    queryset = Booking.objects.select_related('home', 'home__blocks', 'home__floor', 'home__rooms', 'company',
                                              'payment_term', 'client')

    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        return BookingGetSerializer

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        delete_booking(booking_id=instance.id, user=self.request.user)
