# here we have taken Transaction
# date column
Order_Details['Time'] = pd.to_datetime(Order_Details['Transaction Date'])

# After that we extracted hour
# from Transaction date column
Order_Details['Hour'] = (Order_Details['Time']).dt.hour
