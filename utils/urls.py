from django.urls import include, path
from rest_framework.routers import DefaultRouter
from utils.views import BasementViewSet, BlocksViewSet, FloorsViewSet, RenovationViewSet

router = DefaultRouter()
router.register('blocks', BlocksViewSet, basename='blocks')
router.register('floors', FloorsViewSet, basename='floors')
router.register('renovation', RenovationViewSet, basename='renovation')
router.register('basement', BasementViewSet, basename='basement')

urlpatterns = [
    path('', include(router.urls)),
]
