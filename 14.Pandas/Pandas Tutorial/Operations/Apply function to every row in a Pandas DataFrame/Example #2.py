'''

'''
'''You can use the numpy function as the parameters to the dataframe as well.'''

import pandas as pd
import numpy as np


def main():
    # create a dictionary with
    # five fields each
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    # applying function to each row in the dataframe
    # and storing result in a new coloumn
    df['add'] = df.apply(np.sum, axis=1)

    print('\nAfter Applying Function: ')
    # printing the new dataframe
    print(df)


if __name__ == '__main__':
    main()
