# importing the pandas library as pd
import pandas as pd

# ADDING MULTI INDEX TO DATA FRAME
new_index = pd.MultiIndex.from_tuples([('E4', 'ECE'),
                                       ('E5', 'ECE'),
                                       ('E6', 'ECE'),
                                       ('E7', 'ECE'),
                                       ('E8', 'ECE')],
                                      names=['BATCH', 'BRANCH'])
# Creating the dataframe AB
data = ({'Roll Number': ['9917102206', '9917102250',
                         '9917102203', '9917102204',
                         '9917102231'],
         'Name': ['TANYA', 'PREETIKA', 'KUSHAGRA',
                  'PRAKHAR', 'ASHISH'],
         'Score': [99, 98, 50, 45, 97],
         'Grade': ['A+', 'A+', 'C+', 'C', 'A'],
         'Subject': ['Operating Systems', 'Operating Systems',
                     'Operating Systems', 'Operating Systems',
                     'Operating Systems']})

# COMBING DATA FRAME AND MULTI INDEX
# VALUES AND FORMING DATA FRAME
AB = pd.DataFrame(data, columns=['Roll Number', 'Name', 'Score', 'Grade', 'Subject'],
                  index=new_index)

# MAKING MULTI INDEX NOW A PART OF COLUMN
# OF DATAFRAME
AB.reset_index(inplace=True)

AB
