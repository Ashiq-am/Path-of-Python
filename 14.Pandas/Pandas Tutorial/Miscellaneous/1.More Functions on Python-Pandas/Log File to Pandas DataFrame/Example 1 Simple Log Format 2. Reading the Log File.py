# Example 1: Simple Log Format
simple_log_data = [
    "INFO [2023-05-17 12:34:56.789] This is a simple log message",
    "ERROR [2023-05-18 01:23:45.678] An error occurred",
    "WARNING [2023-05-19 10:20:30.123] This is a warning message"
]

level = []
time = []
text = []

for line in simple_log_data:
    parts = line.split('[')
    level.append(parts[0].strip())
    time.append(parts[1].split(']')[0].strip())
    text.append(parts[1].split(']')[1].strip())

df_simple = pd.DataFrame({'Level': level, 'Time': time, 'Text': text})
df_simple['Time'] = pd.to_datetime(df_simple['Time'], format='%Y-%m-%d %H:%M:%S.%f')
print("Example 1: Simple Log Format")
print(df_simple)
