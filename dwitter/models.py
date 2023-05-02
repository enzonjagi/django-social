from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """Creates a Profile Model for Users on the App"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True,
    )


    def __str__(self):
        """A description of the User who owns this profile"""

        return self.user.username
