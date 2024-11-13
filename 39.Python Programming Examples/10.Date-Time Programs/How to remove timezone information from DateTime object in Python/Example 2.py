from datetime import datetime, timezone

# Get the datetime object with timezone
# information
dt_obj_w_tz = datetime.now(tz=timezone.utc)
print(dt_obj_w_tz)

# Remove the timezone information from the
# datetime object
dt_obj_wo_tz = dt_obj_w_tz.replace(tzinfo=None)
print(dt_obj_wo_tz)
