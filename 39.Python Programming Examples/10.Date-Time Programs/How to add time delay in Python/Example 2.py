# importing time module
import time


def message(string):
    for i in string:
        # printing each character of the message
        print(i, end="")

        # adding time delay of half second
        time.sleep(0.5)


# main function
if __name__ == '__main__':
    msg = "Its looks like auto typing"

    # calling the function for printing the
    # characters with delay
    message(msg)
