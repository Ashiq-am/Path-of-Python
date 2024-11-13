# Python3 program to check if sum of
# any subarray of size atleast 2 is
# palindrome or not

# Function which checks whether a
# given number is palindrome or not
def checkPalindrome(n):
    # Store the reverse
    # of the number n
    rev = 0
    x = n

    while (x != 0):
        d = x % 10
        rev = rev * 10 + d
        x = x // 10

    if (rev == n):
        return True
    else:
        return False


# Function which checks if the
# requires subarray exists or not
def findSubarray(ar, n):
    # Making a prefix sum array of ar[]
    pref = [0 for i in range(n)]
    pref[0] = ar[0]

    for x in range(1, n):
        pref[x] = pref[x - 1] + ar[x]

    # Boolean variable that will store
    # whether such subarray exists or not
    found = False

    for x in range(n):
        for y in range(x + 1, n, 1):

            # Sum stores the sum of subarray
            # from index x to y of array
            sum = pref[y]
            if (x > 0):
                sum -= pref[x - 1]

            if (checkPalindrome(sum)):
                # Required subarray is found
                found = True
                break

        if (found):
            break
    if (found):
        print("Yes")
    else:
        print("No")

    # Driver code


if __name__ == '__main__':
    ar = [1, 11, 20, 35]
    n = len(ar)

    findSubarray(ar, n)
