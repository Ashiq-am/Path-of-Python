import pandas as pd
import modin.pandas as mpd
import time

start = time.time()

# Creating a Custom Dataframe
data = {'Name': ['Tom', 'nick', 'krish', 'jack',
                 'ash', 'singh', 'shilpa', 'nav'],

        'Age': [20, 21, 19, 18, 6, 12, 18, 20]}

df = pd.DataFrame(data)

# Appending the dataframe to itself 10 times.
for _ in range(10):
    df = df.append(df)

end = time.time()
print(f"Pandas Appending Time :{end - start}")

start = time.time()
modin_df = mpd.DataFrame(data)

# Appending the dataframe to itself 10 times.
for _ in range(10):
    modin_df = modin_df.append(modin_df)

end = time.time()
print(f"Modin Appending Time :{end - start}")
