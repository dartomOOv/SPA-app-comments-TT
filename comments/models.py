from django.db import models

from dummy_user.models import DummyUserModel


class CommentsModel(models.Model):
    text = models.TextField()
    user = models.ForeignKey(DummyUserModel, on_delete=models.DO_NOTHING)
    home_page = models.URLField(null=True, blank=True)
    response_to = models.OneToOneField("CommentsModel", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("id", "response_to"), name="unique_id_response_to"
            ),
        )

    def __str__(self):
        return f"{self.user.username} messaged: {self.text}"
