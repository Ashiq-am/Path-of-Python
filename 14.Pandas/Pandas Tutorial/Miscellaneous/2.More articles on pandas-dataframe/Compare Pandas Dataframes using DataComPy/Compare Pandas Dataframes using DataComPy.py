from io import StringIO
import pandas as pd
import datacompy

data1 = """employee_id, name 
1, rajiv kapoor 
2, rahul agarwal 
3, alice johnson 
"""

data2 = """employee_id, name 
1, rajiv khanna 
2, rahul aggarwal 
3, alice tyson 
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,

    # You can also specify a list
    # of columns
    join_columns='employee_id',

    # Optional, defaults to 0
    abs_tol=0,

    # Optional, defaults to 0
    rel_tol=0,

    # Optional, defaults to 'df1'
    df1_name='Original',

    # Optional, defaults to 'df2'
    df2_name='New'
)

# if ignore_exra_columns=True,
# the function won't return False
# in case of non-overlapping
# column names
compare.matches(ignore_extra_columns=False)

# This method prints out a human-readable
# report summarizing and sampling
# differences
print(compare.report())
