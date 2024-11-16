# importing pandas library
import numpy as np

# Creating pandas dataframe
df = pd.DataFrame(
    [
        ("Corona Positive", 65, 99),
        ("Corona Negative", 52, 98.7),
        ("Corona Positive", 43, 100.1),
        ("Corona Positive", 26, 99.6),
        ("Corona Negative", 30, 98.1),
    ],

    index=["Patient 1", "Patient 2", "Patient 3",
           "Patient 4", "Patient 5"],

    columns=("Status", "Age(in Years)", "Temperature"),
)

# show dataframe
print(df)
