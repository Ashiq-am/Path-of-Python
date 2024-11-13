# Python3 program to print all the numbers
# divisible by 5 or 7 for a given number

# Result generator with N
def NumGen(n):
    # iterate from 0 to N
    for j in range(1, n + 1):

        # Short-circuit operator is used
        if j % 5 == 0 or j % 7 == 0:
            yield j

        # Driver code


if __name__ == "__main__":

    # input goes here
    N = 50

    # Iterating over generator function
    for j in NumGen(N):
        print(j, end=" ")
