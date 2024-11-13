import os
import shutil

def check_quota(directory, limit):
	total, used, free = shutil.disk_usage(directory)
	if used > limit:
		print(f"Quota exceeded in {directory}. Used: {used / (2**30):.2f} GB, Limit: {limit / (2**30):.2f} GB")
		# Take necessary actions, such as deleting old files or notifying users
	else:
		print("Quota within limits.")

# Example usage
directory_path = "/path/to/directory"
quota_limit = 10 * (2**30) # 10 GB limit
check_quota(directory_path, quota_limit)
