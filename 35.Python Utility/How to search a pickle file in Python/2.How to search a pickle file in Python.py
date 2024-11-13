import pickle

print("GFG")


def search_file():
    f = open("travel.txt", 'rb')
    t_code = int(input("Enter the travel code to traveller : "))

    while True:
        try:

            L = pickle.load(f)

            if L[0] == t_code:
                print("Place", L[1], "\t\t Travellers :",
                      L[2], "\t\t Buses :", L[3])

                break

        except EOFError:

            print("Completed reading details")
    f.close()


print("entering the details of passengers in the pickle file")
write_file()

print("Search the file using the passenger Code")
search_file()
