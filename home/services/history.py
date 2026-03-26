from django.db import transaction
from home.models import Home
from home.models import HomeStatusHistory


class HomeService:

    @staticmethod
    @transaction.atomic
    def change_status(home_id: int, new_status: str, user=None):
        home = Home.objects.select_for_update().get(id=home_id)

        old_status = home.home_status

        if old_status == new_status:
            return home

        home.home_status = new_status
        home.save(update_fields=["home_status"])

        HomeStatusHistory.objects.create(home=home, from_status=old_status, to_status=new_status, changed_by=user)

        return home
