from django.db.models import Count, Q
from home.models import Home
from projects.models.showroom_models import Showroom


def get_blocks_stats():
    return (
        Showroom.objects
        .select_related('blocks')
        .annotate(
            homes_count=Count('blocks__homes'),
            available_homes=Count('blocks__homes', filter=Q(blocks__homes__home_status=Home.HomeStatus.AVAILABLE)),
            sold_homes=Count('blocks__homes', filter=Q(blocks__homes__home_status=Home.HomeStatus.SOLD)),
            reserved_homes=Count('blocks__homes', filter=Q(blocks__homes__home_status=Home.HomeStatus.RESERVED))))
