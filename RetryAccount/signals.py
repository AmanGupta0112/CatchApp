from django.db.models.signals import post_save
from django.contrib.auth.models import User
from RetryAccount.models import Profile

def create_user_profile(sender, instance, created=False, **kwargs):
    user = instance
    if created:
        Profile.objects.create(user=user)
post_save.connect(create_user_profile, sender=User)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(save_user_profile, sender=User)
