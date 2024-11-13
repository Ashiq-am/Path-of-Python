from datetime import datetime

# Saves a .txt file with file name
# as 2020-01-11-10-20-23.txt
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"), "w")as myfile:
    # Content of the file
    myfile.write("Hello World !")
