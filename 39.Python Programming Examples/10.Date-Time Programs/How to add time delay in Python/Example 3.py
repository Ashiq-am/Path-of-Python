# importing module
import time


# function to print the pattern
def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print('*', end=' ')

            # adding two second of time delay
            time.sleep(0.5)
        print(' ')


# main function
if __name__ == '__main__':
    # taking range from the user
    num = 4
    print("Printing the pattern")

    # calling function to print the pattern
    pattern(num)
