from django.db.models import Count, Q
from user.models import User


def get_user_stats():
    return User.objects.aggregate(
        total_users=Count("id"),
        total_salers=Count("id", filter=Q(role=User.UserRoles.SELLER)),
        total_admins=Count("id", filter=Q(role=User.UserRoles.ADMIN)),
    )
