#signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from PIL import Image
import time
import logging


logger = logging.getLogger(__name__)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        start_time = time.time()
        Profile.objects.create(user=instance)
        elapsed_time = time.time() - start_time
        logger.info(f"Created Profile for user: \
                {instance.username} in {elapsed_time:.3f} seconds",
                        extra={'elapsed': elapsed_time})

@receiver(post_save, sender=Profile)
def resize_profile_image(sender, instance, **kwargs):
    if instance.image:
        start_time = time.time()
        time.sleep(5)
        logger.info(f"Image processing started for user: {instance.user.username}")
        img = Image.open(instance.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(instance.image.path)

        elapsed_time = time.time() - start_time
        logger.info(f"Image processing complete for user: \
                {instance.user.username} in {elapsed_time:.3f} seconds",
                    extra={'elapsed': elapsed_time})
