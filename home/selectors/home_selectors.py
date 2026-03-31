from django.db.models import DecimalField, F, ExpressionWrapper, Value
from django.db.models.functions import Coalesce
from home.models import Home


def get_homes_with_finance():
    return (
        Home.objects
        .select_related('blocks', 'blocks__projects', 'floor', 'renovation', 'booking', 'booking__payment_term')
        .annotate(
            total_price_annotated=ExpressionWrapper(
                Coalesce(F('area') * F('price_per_sqm'), 0) +
                Coalesce(F('renovation__price'), 0),
                output_field=DecimalField(max_digits=14, decimal_places=2)
            ),
            initial_payment_annotated=ExpressionWrapper(
                (Coalesce(F('area') * F('price_per_sqm'), 0) +
                 Coalesce(F('renovation__price'), 0)) *
                Coalesce(F('booking__down_payment'), 0) / Value(100),
                output_field=DecimalField(max_digits=14, decimal_places=2)
            ),
            monthly_payment_annotated=ExpressionWrapper(
                ((Coalesce(F('area') * F('price_per_sqm'), 0) +
                  Coalesce(F('renovation__price'), 0)) -
                 ((Coalesce(F('area') * F('price_per_sqm'), 0) +
                   Coalesce(F('renovation__price'), 0)) *
                  Coalesce(F('booking__down_payment'), 0) / Value(100))) /
                Coalesce(F('booking__payment_term__months'), 1),
                output_field=DecimalField(max_digits=14, decimal_places=2)
            )
        )
    )
