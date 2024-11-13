import pandas as pd

def retrieve_description(course_name, filename):
    df = pd.read_csv(filename)
    description = df.loc[df['Course'] == course_name, 'Description'].values[0]
    return description

filename = 'data.csv'
course_name = 'ReactJS'
description = retrieve_description(course_name, filename)
print(f"Description of {course_name}: {description}")
