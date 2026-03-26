from drf_spectacular.utils import extend_schema
from booking.models import Booking, PaymentTerm
from booking.serializers import BookingCreateSerializer, BookingGetSerializer, PaymentTermSerializer
from booking.services.booking import create_booking, delete_booking
from utils.base.views_base import BaseUserViewSet


@extend_schema(tags=['PaymentTerm'])
class PaymentTermViewSet(BaseUserViewSet):
    queryset = PaymentTerm.objects.all()
    serializer_class = PaymentTermSerializer


@extend_schema(tags=['Booking'])
class BookingViewSet(BaseUserViewSet):
    queryset = Booking.objects.select_related('home', 'payment_term')

    def get_serializer_class(self):
        if self.action == 'create':
            return BookingCreateSerializer
        return BookingGetSerializer

    def perform_create(self, serializer):
        create_booking(user=self.request.user, **serializer.validated_data)

    def perform_destroy(self, instance):
        delete_booking(instance.id)
