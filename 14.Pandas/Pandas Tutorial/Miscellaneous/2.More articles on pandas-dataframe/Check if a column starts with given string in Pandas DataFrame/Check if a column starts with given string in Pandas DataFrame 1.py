# importing library pandas as pd
import pandas as pd

# creating data frame for student
df = pd.DataFrame({
    'Student_id': ['TCS101', 'TCS103', 'PCS671',
                   'ECS881', 'MCS961'],

    'date_of_joining': ['12/12/2016', '07/12/2015',
                        '11/11/2011', '09/12/2014',
                        '01/01/2017'],

    'Branch': ['Computer Science', 'Computer Science',
               'Petroleum', 'Electrical', 'Mechanical']
})

# joining new column in dataframe
# .startswith function used to check
df['student_id_starts_with_TCS'] = list(
    map(lambda x: x.startswith('TCS'), df['Student_id']))

# printing new data frame
df
