# Import pandas package
import pandas as pd


def normalize(x, y):
    x_new = ((x - np.mean([x, y])) /
             (max(x, y) - min(x, y)))

    # print(x_new)
    return x_new


def main():
    # create a dictionary with three fields each
    data = {
        'X': [1, 2, 3],
        'Y': [45, 65, 89]}

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    df['X'] = df.apply(lambda row: normalize(row['X'],
                                             row['Y']), axis=1)

    print('\nNormalized:')
    print(df)


if __name__ == '__main__':
    main()
