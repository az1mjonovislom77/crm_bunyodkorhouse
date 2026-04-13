class AuditMixin:

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            user=self.request.user if 'user' in serializer.fields else None
        )

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance._history_user = self.request.user
        instance.delete()
