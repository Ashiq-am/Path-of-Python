import polars as pl

# Create a Polars DataFrame with a timestamp column
data = {
    "timestamp": ["2023-01-01 10:00:00",
                  "2023-01-02 11:30:00",
                  "2023-01-03 14:45:00"],
    "value": [10, 20, 30]
}
df = pl.DataFrame(data)

# Select the timestamp column using the select method
timestamp_col = df.select("timestamp")

print(timestamp_col)
