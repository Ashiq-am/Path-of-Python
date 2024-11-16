# Example 2: CSV-like Log Format
csv_log_data = [
    "Type,Timestamp,Source,EventID,Description,Details",
    "ERROR,2023-05-17 12:34:56,Server,1001,Connection Timeout,Details: Timeout=30s",
    "INFO,2023-05-18 01:23:45,Client,2001,Request Sent,Details: Request=GET /api/data",
    "WARNING,2023-05-19 10:20:30,Server,3001,Disk Full,Details: DiskSpace=95%"
]

df_csv = pd.read_csv(io.StringIO('\n'.join(csv_log_data)), sep=',')
df_csv['Timestamp'] = pd.to_datetime(df_csv['Timestamp'], format='%Y-%m-%d %H:%M:%S')
print("\nExample 2: CSV-like Log Format")
print(df_csv)
