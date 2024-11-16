# import pandas library
import pandas as pd


# this user defines function
# creates a series
# from the passed list.
def createSeries(series_list):
    # create a seriesPython | Merge, Join and Concatenate DataFrames using Panda


    series_list = pd.Series(series_list)
    return series_list

# create a series of students
students = createSeries(['ABC', 'DEF',
                         'GHI', 'JKL',
                         'MNO', 'PQR'])
# create a series of subjects
subject = createSeries(['C++', 'C#',
                        'RUBY', 'SWIFT',
                        'GO', 'PYTHON'])
# create a series of marks
marks = createSeries([90, 30,
                      50, 70,
                      80, 60])
# create a dictonary
data = {"students": students,
        "subject": subject,
        "marks": marks}

# Concatenating the series side
# by side as depicted by axis=1
# If you want to concatenate the
# series one below the other
# change the axis to zero.
df = pd.concat(data,
               axis=1)

# show the dataframe
df
