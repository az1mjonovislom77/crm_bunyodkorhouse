from user.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
from utils.compressor import check_image_size


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=500)
    floors = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='projects/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP', 'heic',
                                'heif']), check_image_size], null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title
