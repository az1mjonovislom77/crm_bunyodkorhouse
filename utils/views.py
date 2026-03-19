from drf_spectacular.utils import extend_schema
from utils.base.views_base import BaseUserViewSet
from utils.models import Basement, Blocks, Floors, Renovation, Rooms
from utils.serializers import BasementSerializer, BlocksCreateSerializer, BlocksGetSerializer, FloorsSerializer, \
    RenovationSerializer, RoomsSerializer


@extend_schema(tags=['Blocks'])
class BlocksViewSet(BaseUserViewSet):
    queryset = Blocks.objects.select_related('projects')

    def get_serializer_class(self):
        if self.action == 'create':
            return BlocksCreateSerializer
        return BlocksGetSerializer


@extend_schema(tags=['Floors'])
class FloorsViewSet(BaseUserViewSet):
    queryset = Floors.objects.all()
    serializer_class = FloorsSerializer


@extend_schema(tags=['Rooms'])
class RoomsViewSet(BaseUserViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


@extend_schema(tags=['Renovation'])
class RenovationViewSet(BaseUserViewSet):
    queryset = Renovation.objects.all()
    serializer_class = RenovationSerializer


@extend_schema(tags=['Basement'])
class BasementViewSet(BaseUserViewSet):
    queryset = Basement.objects.all()
    serializer_class = BasementSerializer
