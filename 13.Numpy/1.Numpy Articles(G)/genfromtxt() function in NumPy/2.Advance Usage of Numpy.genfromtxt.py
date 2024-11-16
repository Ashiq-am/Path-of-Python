# importing the numpy library
import numpy as np

# driver code
if __name__ == "__main__":

    # performing the function and fill the required parameters
    data = np.genfromtxt(
        'data.csv',
        delimiter=',',
        dtype=[
            ('id', int),
            ('name', 'U10'),
            ('age', int),
            ('codingscore', float),
            ('totalscore', float),
            ('potd', int)
        ],
        names=True,
        converters={
            2: lambda x: int(x) if x else 1,
            3: lambda x: float(x) if x else 1.0,
            4: lambda x: float(x) if x else 1.0
        },
        missing_values={'age': '', 'codingscore': '', 'totalscore': '', 'potd': ''},
        filling_values={'age': 1, 'codingscore': 1.0, 'totalscore': 1.0, 'potd': 1}
    )
    # displaying the data
    for i in data:
        print(i)
