from django.db import models


class DummyUserModel(models.Model):
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=128)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=("username", "email"), name="unique_username_email"
            ),
        )

    def __str__(self):
        return self.username
