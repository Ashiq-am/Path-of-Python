#  Example 3: Custom Log Format
custom_log_data = [
    "Device Model: XYZ123",
    "Serial Number: 98765",
    "Export timestamp: 2023-05-17_12-34-56",
    "Software Version: 1.0.0"
]

data = {'Model': [], 'S/N': [], 'Export timestamp': [], 'SW-Version': []}

for line in custom_log_data:
    if 'Model:' in line:
        data['Model'].append(line.split(':')[1].strip())
    elif 'Serial Number:' in line:
        data['S/N'].append(line.split(':')[1].strip())
    elif 'Export timestamp:' in line:
        data['Export timestamp'].append(line.split(':')[1].strip())
    elif 'Software Version:' in line:
        data['SW-Version'].append(line.split(':')[1].strip())

df_custom = pd.DataFrame(data)
df_custom['Export timestamp'] = pd.to_datetime(df_custom['Export timestamp'], format='%Y-%m-%d_%H-%M-%S')
print("\nExample 3: Custom Log Format")
print(df_custom)
