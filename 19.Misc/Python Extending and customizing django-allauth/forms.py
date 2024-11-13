from allauth.account.forms import SignupForm
from django import forms
#</code></pre>

class CustomSignupForm(SignupForm):
	first_name = forms.CharField(max_length=30, label='First Name')
	last_name = forms.CharField(max_length=30, label='Last Name')




def signup(self, request, user):
	user.first_name = self.cleaned_data['first_name']
	user.last_name = self.cleaned_data['last_name']
	user.save()
	return user











"""In the above snippet CustomSignupForm is extended the class which inherits all the features of 
SignupForm class and adds the necessary features. Here custom fields by the name first_nameand 
last_name are created and saved in using the signup module in the same class."""
