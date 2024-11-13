def credentials_cls(need_proxy=False, tfa=False):
	# need proxy for openId services
	if need_proxy:
		print("Open Id Service")
		keys = ['service_name', 'email_address']
	else:
		print("Traditional Login")
		keys = ['username', 'password']

		# two factor authentication for traditional login
		if tfa:
			keys.append('auth_token')

	class CredentialCheck(object):
		required_keys = set(keys)

		def __init__(self, **kwargs):
			# checking whether key matches based on login service
			if self.required_keys != set(kwargs.keys()):
				raise ValueError('Mismatch')

			# storing the keys and values to the credential object
			for k, v in kwargs.items():
				setattr(self, k, v)

	return CredentialCheck


CredCheck = credentials_cls(False, False)
crdTraditional = CredCheck(username='uname', password='******')

OpenIDCheck = credentials_cls(True, False)
crdOpenID = OpenIDCheck(service_name='sname', email_address='email@gmail.com')
