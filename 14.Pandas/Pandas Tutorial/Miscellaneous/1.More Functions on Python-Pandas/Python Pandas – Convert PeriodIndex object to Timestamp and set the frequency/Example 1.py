# import packages
import pandas as pd

# Create a PeriodIndex object
# freq ='Y' represents year.
periodIndex = pd.PeriodIndex(['2022-12-21 09:30:20', '2021-11-20 06:45:40',
							'2020-10-19 03:38:15', '2019-09-18 01:30:30'],
							freq="Y")

print('period index object : ' + str(periodIndex))
print("frequency of the periodIndex object : ", periodIndex.freq)

# Display PeriodIndex frequency as string
print("frequency object as a string : ", periodIndex.freqstr)

# Converting PeriodIndex object to timestamp
print("Timestamp object : ", periodIndex.to_timestamp())
