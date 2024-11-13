# Importing required module
import json
import datetime

# Store time in "now"
now = datetime.datetime.now()

# Serializing time stored in now
json.dumps(now)
