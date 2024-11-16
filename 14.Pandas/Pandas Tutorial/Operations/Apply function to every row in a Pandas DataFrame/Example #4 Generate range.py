import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None


# Function to generate range
def generate_range(n):
    # printing the range for eg:
    # input is 67 output is 60-70
    n = int(n)

    lower_limit = n // 10 * 10
    upper_limit = lower_limit + 10

    return str(str(lower_limit) + '-' + str(upper_limit))


def replace(row):
    for i, item in enumerate(row):
        # updating the value of the row
        row[i] = generate_range(item)
    return row


def main():
    # create a dictionary with
    # three fields each
    data = {
        'A': [0, 2, 3],
        'B': [4, 15, 6],
        'C': [47, 8, 19]}

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)

    print('Before applying function: ')
    print(df)

    # applying function to each row in
    # dataframe and storing result in a new coloumn
    df = df.apply(lambda row: replace(row))

    print('After Applying Function: ')
    # printing the new dataframe
    print(df)


if __name__ == '__main__':
    main()
