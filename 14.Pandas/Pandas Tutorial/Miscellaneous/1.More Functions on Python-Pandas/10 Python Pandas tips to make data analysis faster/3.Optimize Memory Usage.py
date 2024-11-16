import pandas as pd
# Sample DataFrame
data = {'column': [1.0, 2.5, 3.8, 4.2, 5.6]}
df = pd.DataFrame(data)
# Original DataFrame
print("Original DataFrame:")
print(df)
print(df.info())
# Check memory usage
print("\nMemory usage before optimization:")
print(df.memory_usage())
