# importing library pandas as pd
import pandas as pd

# creating data frame for employee
df = pd.DataFrame({
    'Company_id': ['IF101', 'IF103', 'GFG671',
                   'GFG881', 'CAPG961', 'WPR981'],

    'Company': ['Infosys', 'Infosys', 'GeeksforGeeks',
                'GeeksforGeeks', 'Capgemini', 'Wipro'],

    'Joining_Date': ['12/12/2011', '07/12/2012',
                     '11/11/2014', '09/12/2015',
                     '01/01/2016', '01/01/2009'],

    'Company_Emp_id': ['abc@infosys.com', 'xyz@infosys.com',
                       'acd@gfg.com', 'aed@gfg.com',
                       'klm@capg.com', 'xyz@wipro.com']
})
# printing the given data frame
print("Printing Original Student DataFrame:")

df
