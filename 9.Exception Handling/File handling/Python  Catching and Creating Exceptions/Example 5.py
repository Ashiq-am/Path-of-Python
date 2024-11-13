class NetworkError(Exception):
	pass
class HostnameError(NetworkError):
	pass
class TimeoutError(NetworkError):
	pass
class ProtocolError(NetworkError):
	pass
