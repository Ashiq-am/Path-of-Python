from datetime import datetime, timezone

# Get the datetime object using datetime
# module
dt_obj_w_tz = datetime.now()
print(dt_obj_w_tz)

# Add timezone information to the datetime
# object
dt_obj_w_tz = dt_obj_w_tz.replace(tzinfo=timezone.utc)
print(dt_obj_w_tz)

# Remove the timezone information from the datetime
# object
dt_obj_wo_tz = dt_obj_w_tz.replace(tzinfo=None)
print(dt_obj_wo_tz)
