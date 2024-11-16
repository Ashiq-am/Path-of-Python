# import pandas library
import pandas as pd

# create a Dataframe
data = pd.DataFrame({
    'course_name': ['Data Structures', 'Python',
                    'Machine Learning'],
    'student_name': ['A', 'B',
                     'C'],
    'student_city': ['Chennai', 'Pune',
                     'Delhi'],
    'student_gender': ['M', 'F',
                       'M']})

df = data.loc[:, data.columns != 'student_gender']

# show the dataframe
df
