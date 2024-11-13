# Python3 program of the
# above approach
maxN = 2002


# Function to find the count of
# the subsequence of given type
def countSubsequece(a, n):
    # Stores the count
    # of quadruples
    answer = 0

    # Generate all possible
    # combinations of quadruples
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):

                    # Check if 1st element is
                    # equal to 3rd element
                    if (a[j] == a[l] and

                            # Check if 2nd element is
                            # equal to 4th element
                            a[i] == a[k]):
                        answer += 1

    return answer


# Driver Code
if __name__ == '__main__':
    a = [1, 2, 3, 2, 1, 3, 2]

    print(countSubsequece(a, 7))
