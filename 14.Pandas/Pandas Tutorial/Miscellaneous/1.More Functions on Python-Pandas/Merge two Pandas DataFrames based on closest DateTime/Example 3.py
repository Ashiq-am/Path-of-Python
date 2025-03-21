# Importing the required package
import pandas as pd

# Creating the DataFrame of left side
left = pd.DataFrame({
    "time": [pd.Timestamp("2020-03-25 13:30:00.023"),
             pd.Timestamp("2020-03-25 13:30:00.023"),
             pd.Timestamp("2020-03-25 13:30:00.030"),
             pd.Timestamp("2020-03-25 13:30:00.041"),
             pd.Timestamp("2020-03-25 13:30:00.048"),
             pd.Timestamp("2020-03-25 13:30:00.049"),
             pd.Timestamp("2020-03-25 13:30:00.072"),
             pd.Timestamp("2020-03-25 13:30:00.075")
             ],
    "ticker": ["GOOG", "MSFT", "MSFT", "MSFT", "GOOG",
               "AAPL", "GOOG", "MSFT"],

    "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99,
            720.50, 52.01],

    "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01,
            720.88, 52.03]
})

# Creating the Dataframe of right side
right = pd.DataFrame({
    "time": [
        pd.Timestamp("2020-03-25 13:30:00.023"),
        pd.Timestamp("2020-03-25 13:30:00.038"),
        pd.Timestamp("2020-03-25 13:30:00.048"),
        pd.Timestamp("2020-03-25 13:30:00.048"),
        pd.Timestamp("2020-03-25 13:30:00.048")
    ],

    "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],

    "price": [51.95, 51.95, 720.77, 720.92, 98.0],

    "quantity": [75, 155, 100, 100, 100]
})

# Applying merge_asof on data and store it
# in a variable
merged_dataframe = pd.merge_asof(left, right, on="time", by="ticker",
                                 tolerance=pd.Timedelta("2ms"),
                                 allow_exact_matches=False)

# print the variable
print(merged_dataframe)
