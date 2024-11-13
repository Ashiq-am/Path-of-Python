import pickle


def delete_details():
    f1 = open("travel.txt", 'rb+')
    travelList = []
    t_place = input("Enter the place to delete :")

    while True:
        try:
            L = pickle.load(f1)
            if (L[1] != t_place):
                travelList.append(L)
        except EOFError:
            print("completed deleting details")
            break

    f1.seek(0)
    f1.truncate()

    for i in range(len(travelList)):
        pickle.dump(travelList[i], f1)
    else:
        f1.close()

    # reading content in the file.


def read_file():
    f = open("travel.txt", 'rb')
    while True:
        try:
            L = pickle.load(f)
            print("Place", L[1], "\t\t Travellers :",
                  L[2], "\t\t Buses :", L[3])

        except EOFError:
            print("Completed reading details")
            break
    f.close()


print("deleting the desired coloumn")
delete_details()

print("Reading the file")
read_file()
