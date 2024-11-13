import psutil


def check_quota_psutil(directory, limit):
	partition = psutil.disk_usage(directory)
	if partition.used > limit:
		print(
			f"Quota exceeded in {directory}. Used: {partition.used / (2**30):.2f} GB, Limit: {limit / (2**30):.2f} GB")
		# Take necessary actions
	else:
		print("Quota within limits.")


# Example usage
directory_path = "/path/to/directory"
quota_limit = 10 * (2**30) # 10 GB limit
check_quota_psutil(directory_path, quota_limit)
