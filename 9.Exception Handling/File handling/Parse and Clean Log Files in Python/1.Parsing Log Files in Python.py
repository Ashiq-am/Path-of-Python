import re

# Define the regex pattern for Apache log entries
log_pattern = r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S*)" (\d{3}) (\d+)'

# Example log entry
log_entry = '192.168.1.1 - - [25/May/2023:10:15:32 +0000] "GET /index.html HTTP/1.1" 200 54321'

# Parse the log entry using regex
match = re.match(log_pattern, log_entry)
if match:
    ip_address = match.group(1)
    date_time = match.group(4)
    method = match.group(5)
    requested_url = match.group(6)
    http_status = match.group(8)
    bytes_transferred = match.group(9)

    print("IP Address:", ip_address)
    print("Date/Time:", date_time)
    print("Method:", method)
    print("Requested URL:", requested_url)
    print("HTTP Status:", http_status)
    print("Bytes Transferred:", bytes_transferred)
else:
    print("Log entry does not match the expected format.")
