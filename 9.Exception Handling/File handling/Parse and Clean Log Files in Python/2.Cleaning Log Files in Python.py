import re

# Example list of raw log entries
raw_logs = [
    "[DEBUG] 2023-05-25 10:15:32: Initializing application...",
    "[INFO] 2023-05-25 10:15:35: User 'John' logged in.",
    "[ERROR] 2023-05-25 10:15:40: Database connection failed.",
    "[DEBUG] 2023-05-25 10:15:45: Processing request...",
    "[INFO] 2023-05-25 10:15:50: Request completed successfully."
]

# Define regex pattern to match log entries
log_pattern = r'\[(\w+)\] (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}): (.*)'

# Function to clean log entries
def clean_logs(raw_logs):
    cleaned_logs = []
    for log in raw_logs:
        match = re.match(log_pattern, log)
        if match:
            log_level = match.group(1)
            timestamp = match.group(2)
            message = match.group(3)

            # Filter out DEBUG messages
            if log_level != 'DEBUG':
                cleaned_logs.append(
                    {'level': log_level, 'timestamp': timestamp, 'message': message})
        else:
            print("Log entry does not match the expected format:", log)
    return cleaned_logs


# Clean the raw logs
cleaned_logs = clean_logs(raw_logs)

# Print cleaned logs
for log in cleaned_logs:
    print(log)
