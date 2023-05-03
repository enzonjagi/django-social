from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

# Create a Profile for each new User
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Should help with automatic Profile and User creation and association"""

    # checks if user was created successfully, 
    # then creates a Profile instance for it
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

class Dweet(models.Model):
    """Allows for the creation of Dweets by users"""

    user = models.ForeignKey(
        User,
        related_name="dweets",
        on_delete=models.DO_NOTHING,
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Displays a clear description of the Dweet"""

        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )
