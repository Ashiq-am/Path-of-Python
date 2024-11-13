#django-allauth registraion settings
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

# 1 day
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 86400

#or any other page
ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/'

# redirects to profile page if not configured.
LOGIN_REDIRECT_URL = '/accounts/email/'
