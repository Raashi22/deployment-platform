from django.db import models

class Deployment(models.Model):

    repo_url = models.URLField()

    status = models.CharField(
        max_length=50,
        default='Pending'
    )

    deployment_url = models.CharField(
        max_length=255,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.repo_url