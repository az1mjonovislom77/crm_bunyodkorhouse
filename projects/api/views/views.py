from drf_spectacular.utils import extend_schema
from projects.api.serializers.serializers import ProjectsSerializer
from projects.selectors.projects_selectors import get_projects_with_stats
from projects.services.project_service import ProjectService
from utils.base.views_base import BaseUserViewSet


@extend_schema(tags=['Projects'])
class ProjectsViewSet(BaseUserViewSet):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return get_projects_with_stats()

    def perform_create(self, serializer):
        ProjectService.create_project(serializer.validated_data)

    def perform_update(self, serializer):
        ProjectService.update_project(instance=self.get_object(), validated_data=serializer.validated_data)
