#signals.py
import logging
import time
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from .huey_tasks import resize_profile_image_task

logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        start_time = time.time()
        profile = Profile.objects.create(user=instance)
        elapsed_time = time.time() - start_time
        logger.info(f"Created Profile for user: {instance.username} in {elapsed_time:.3f} seconds",
                    extra={'elapsed': elapsed_time})

@receiver(post_save, sender=Profile)
def resize_image(sender, instance, created, **kwargs):
    if created:
        start_time = time.time()
        resize_profile_image_task(profile_id=instance.id)
        elapsed_time = time.time() - start_time
        logger.info(f"Image resized for profile: {instance.id} in {elapsed_time:.3f} seconds",
                    extra={'elapsed': elapsed_time})
