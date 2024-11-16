import pandas as pd
import numpy as np


# Define the function to return the MAPE values
def calculate_mape(actual, predicted) -> float:
    # Convert actual and predicted
    # to numpy array data type if not already
    if not all([isinstance(actual, np.ndarray),
                isinstance(predicted, np.ndarray)]):
        actual, predicted = np.array(actual),
        np.array(predicted)

    # Calculate the MAPE value and return
    return round(np.mean(np.abs((
                                        actual - predicted) / actual)) * 100, 2)


if __name__ == '__main__':
    # CALCULATE MAPE FROM PYTHON LIST
    actual = [136, 120, 138, 155, 149]
    predicted = [134, 124, 132, 141, 149]

    # Get MAPE for python list as parameters
    print("py list :",
          calculate_mape(actual,
                         predicted), "%")

    # CALCULATE MAPE FROM NUMPY ARRAY
    actual = np.array([136, 120, 138, 155, 149])
    predicted = np.array([134, 124, 132, 141, 149])

    # Get MAPE for python list as parameters
    print("np array :",
          calculate_mape(actual,
                         predicted), "%")

    # CALCULATE MAPE FROM PANDAS DATAFRAME

    # Define the pandas dataframe
    sales_df = pd.DataFrame({
        "actual": [136, 120, 138, 155, 149],
        "predicted": [134, 124, 132, 141, 149]
    })

    # Get MAPE for pandas series as parameters
    print("pandas df:",
          calculate_mape(sales_df.actual,
                         sales_df.predicted), "%")
