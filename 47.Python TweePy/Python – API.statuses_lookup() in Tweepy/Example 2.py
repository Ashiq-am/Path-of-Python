# list of status IDs to be fetched
from requests import api

id_ = [1266978261701210112, 1266735261012111360, 1266342841648898049]

# fetching the statuses
statuses = api.statuses_lookup(id_, trim_user = True)

# printing the statuses
for status in statuses:
	print(status.user.id)
