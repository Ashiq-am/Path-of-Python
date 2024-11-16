import pandas as pd

# creating a dataframe
sales_data = pd.DataFrame({
    'customer_id': [3005, 3001, 3002, 3009, 3005, 3007,
                    3002, 3004, 3009, 3008, 3003, 3002],

    'salesman_id': [102, 105, 101, 103, 102, 101, 101,
                    106, 103, 102, 107, 101],

    'purchase_amt': [1500, 2700, 1525, 1100, 948, 2400,
                     5700, 2000, 1280, 2500, 750, 5050]})

sales_data
