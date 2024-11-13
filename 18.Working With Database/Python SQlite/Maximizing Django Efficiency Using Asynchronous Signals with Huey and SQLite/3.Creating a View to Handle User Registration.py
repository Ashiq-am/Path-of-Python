#views.py
import logging
import time
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            image = form.cleaned_data['image']

            start_time = time.time()
            logger.info(f"{datetime.now().strftime('%H:%M:%S')} - Starting user creation process")

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            elapsed_time_user_creation = time.time() - start_time
            logger.info(f"{datetime.now().strftime('%H:%M:%S')} - \
                User created: {username} ({email}) in {elapsed_time_user_creation:.3f} seconds",
                        extra={'elapsed': elapsed_time_user_creation})

            # Create or update the profile with the image
            if image:
                start_time_profile = time.time()
                user.profile.image = image
                user.profile.save()
                elapsed_time_profile_update = time.time() - start_time_profile
                logger.info(f"{datetime.now().strftime('%H:%M:%S')} -\
                        Profile updated for user: {username} in {elapsed_time_profile_update:.3f} seconds",
                            extra={'elapsed': elapsed_time_profile_update})
            else:
                logger.warning(f"{datetime.now().strftime('%H:%M:%S')} - \
                    No image provided for user: {username}")

            logger.info(f"{datetime.now().strftime('%H:%M:%S')} -\
                Redirecting to login page after successful registration: {username}")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
