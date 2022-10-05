from .models import Profile
from django.contrib.auth.models import User
from django.db.models import signals

# @receiver(signals.post_save, sender=Profile)
def profilepUpdated(sender, instance, created, **kwargs):
    print("Saved")
    print(sender)
    print(instance)
    print(created)

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
    print("Saved")
    print(sender)
    print(instance)
    print(created)

def profileDeleted(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print('deleted')

signals.post_save.connect(profilepUpdated, sender=Profile)
signals.post_save.connect(createProfile, sender=User)
signals.post_delete.connect(profileDeleted, sender=Profile)