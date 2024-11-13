import os

for folder, subfolders, files in os.walk('csv/'):

    for file in files:

        # checking if file is
        # of .txt type
        if file.endswith('.csv'):
            path = os.path.join(folder, file)

            # printing the path of the file
            # to be deleted
            print('deleted : ', path)

            # deleting the csv file
            os.remove(path)
