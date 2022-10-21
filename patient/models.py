from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class user_Ab(AbstractUser):
    is_Patient = models.BooleanField(default=False)
    is_Doctor = models.BooleanField(default=False)


class Prescription(models.Model):
    Title = models.CharField(max_length=100)
    File = models.FileField(upload_to ='File/')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class CONSULT(models.Model):
    follower = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='follower')
    consulting = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='consulting')

    def user_consult(sender, instance, *args, **kwargs):
        consult = instance
        sender = consult.follower
        consulting = follow.consulting
        notify = Notification(sender=sender, user=consulting, notification_type=3)
        notify.save()

    def user_unfollow(sender, instance, *args, **kwargs):
        follow = instance
        sender = follow.follower
        consulting = follow.consulting

        notify = Notification.objects.filter(sender=sender, user=consulting, notification_type=3)
        notify.delete()
