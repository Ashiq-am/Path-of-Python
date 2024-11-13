from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError


class UsernameMaxAdapter(DefaultAccountAdapter):
    def clean_username(self, username):
        if len(username) > 'Your Max Size':
            raise ValidationError('Please enter a username valueless than the current one')

            # For other default validations.
        return DefaultAccountAdapter.clean_username(self, username)
