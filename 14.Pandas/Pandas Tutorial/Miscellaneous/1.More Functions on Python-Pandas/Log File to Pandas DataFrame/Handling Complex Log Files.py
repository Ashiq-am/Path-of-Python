# Handling Complex Log Files
complex_log_data = [
    "[2023-05-17 12:34:56] Start of log entry\n",
    "Type: ERROR\n",
    "Message: An error occurred\n",
    "[2023-05-18 01:23:45] Another log entry\n",
    "Type: INFO\n",
    "Message: Information message\n",
    "Details: Additional details\n",
    "[2023-05-19 10:20:30] Yet another log entry\n",
    "Type: WARNING\n",
    "Message: Warning message\n"
]

entries = []
entry = {}

for line in complex_log_data:
    if '[' in line:
        if entry:
            entries.append(entry)
            entry = {}
        entry['Timestamp'] = line.strip()
    elif 'Type:' in line:
        entry['Type'] = line.split(':')[1].strip()
    elif 'Message:' in line:
        entry['Message'] = line.split(':')[1].strip()
    elif 'Details:' in line:
        entry['Details'] = line.split(':')[1].strip()

if entry:
    entries.append(entry)

df_complex = pd.DataFrame(entries)
# Filter out entries with non-timestamp values
df_complex = df_complex[df_complex['Timestamp'].str.contains(r'^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}]$', regex=True)]
df_complex['Timestamp'] = pd.to_datetime(df_complex['Timestamp'].str.strip('[]'), format='%Y-%m-%d %H:%M:%S')
print("\nHandling Complex Log Files")
print(df_complex)
