#huey_tasks.py
from huey.contrib.djhuey import task
from PIL import Image
from django.conf import settings
import os
import logging
import time
from datetime import datetime


logger = logging.getLogger(__name__)
huey_logger = logging.getLogger('huey')

@task()
def resize_profile_image_task(profile_id):
    try:
        from .models import Profile
        start_time = time.time()
        logger.info(f"{datetime.now().strftime('%H:%M:%S')} - \
            Starting image processing for profile ID: {profile_id}")
        time.sleep(5)
        instance = Profile.objects.get(id=profile_id)
        if instance.image:
            img_path = os.path.join(settings.MEDIA_ROOT, str(instance.image))
            img = Image.open(img_path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(img_path)


            elapsed_time = time.time() - start_time
            logger.info(f"{datetime.now().strftime('%H:%M:%S')} - \
                Image processing complete for user: \
                    {instance.user.username} in {elapsed_time:.3f} seconds",
                                    extra={'elapsed': elapsed_time})
            huey_logger.info(f"{datetime.now().strftime('%H:%M:%S')} - \
                    Image processing complete for user: \
                        {instance.user.username} in {elapsed_time:.3f} seconds",
                                 extra={'elapsed': elapsed_time})
        else:
            logger.warning(f"{datetime.now().strftime('%H:%M:%S')} - \
                    No image found for user: {instance.user.username}")
    except Profile.DoesNotExist:
        logger.error(f"{datetime.now().strftime('%H:%M:%S')} -\
            Profile with id {profile_id} does not exist.")
