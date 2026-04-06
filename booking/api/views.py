from drf_spectacular.utils import extend_schema
from booking.models import Booking, PaymentTerm
from booking.api.serializers import BookingCreateSerializer, BookingGetSerializer, PaymentTermSerializer
from booking.services.booking import delete_booking, create_booking
from common.base.views_base import BaseUserViewSet


@extend_schema(tags=['PaymentTerm'])
class PaymentTermViewSet(BaseUserViewSet):
    queryset = PaymentTerm.objects.all()
    serializer_class = PaymentTermSerializer


@extend_schema(tags=['Booking'])
class BookingViewSet(BaseUserViewSet):
    queryset = Booking.objects.select_related('home', 'home__blocks', 'home__floor', 'company', 'payment_term',
                                              'client')

    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        return BookingGetSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data.copy()

        home_status = validated_data.pop('home_status', None)
        booking = create_booking(data=validated_data, user=self.request.user, home_status=home_status)

        serializer.instance = booking

    def perform_destroy(self, instance):
        delete_booking(booking_id=instance.id, user=self.request.user)
