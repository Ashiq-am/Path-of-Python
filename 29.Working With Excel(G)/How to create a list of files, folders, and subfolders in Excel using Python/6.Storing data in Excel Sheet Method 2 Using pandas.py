# Function will create a data frame using pandas and
# write File/Folder, and their path to excel file.
def create_excel_using_pandas_dataframe(name_list,
                                        path_list, path):
    # Default Frame (a dictionary) is created with
    # File/Folder names and their path with the given lists
    frame = {'Name': name_list,
             'Path': path_list
             }

    # Creates the dataframe using pandas with the given
    # dictionary
    df_data = pd.DataFrame(frame)

    # Creates and saves the data to an excel file
    df_data.to_excel('Final.xlsx', index=False)


create_excel_using_pandas_dataframe(name_list,
                                    path_list, path)
