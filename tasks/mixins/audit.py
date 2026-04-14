class AuditMixin:

    def perform_create(self, serializer):
        extra_kwargs = {"created_by": self.request.user}

        if serializer.Meta.model.__name__ == "Comment":
            extra_kwargs["user"] = self.request.user

        serializer.save(**extra_kwargs)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    def perform_destroy(self, instance):
        instance._history_user = self.request.user
        instance.delete()
