import os

dir_li=os.listdir('k:/files')

if len(dir_li)==0:
    print("Error!! Directory not empty!!")
else:
    os.rmdir('k:/files')
