# Python code to implement the approach

# Function to count the number of
# good pairs that satisfy the conditions
def maximum_subseq(s):
    n = len(s)

    # To store how many zero appear
    # in front of that to form good pair
    number_of_zero_suffix = []
    for i in range(0, n + 1):
        number_of_zero_suffix.append(0)

    # Checking if its value is 0
    number_of_zero_suffix[n - 1] = (s[n - 1] == '0')

    for i in range(n - 2, -1, -1):
        number_of_zero_suffix[i] = number_of_zero_suffix[i + 1] + (s[i] == '0')

    # Prefix array to count the number of
    # '1' which appear before to it which
    # would decrease the number of good pairs
    number_of_one_prefix = []
    for i in range(0, n):
        number_of_one_prefix.append(0)

    number_of_one_prefix[0] = (s[0] == '1')

    for i in range(1, n):
        number_of_one_prefix[i] = number_of_one_prefix[i - 1] + (s[i] == '1')

    initial_answer = 0

    for i in range(0, n):
        if (s[i] == '1'):
            # Counting initial answer in
            # the original string
            initial_answer += number_of_zero_suffix[i + 1]

    maxi = 0

    profit = 0
    loss = 0
    for i in range(0, n):
        if (s[i] == '0'):
            if (i == n - 1):
                profit = 0
            else:
                profit = number_of_zero_suffix[i + 1]
            if (i == 0):
                loss = 0
            else:
                loss = number_of_one_prefix[i - 1]

            # Calculating net profit
            net = profit - loss

            # Storing maximum value of net
            # profit after performing
            # the operation.
            maxi = max(maxi, net)

    # Calculating final answer.
    answer = initial_answer + maxi

    return answer


# Driver code
# First test case
S1 = "1110"
print(maximum_subseq(S1))

# Second test case
S2 = "10110"
print(maximum_subseq(S2))

# Third test case
S3 = "101100"
print(maximum_subseq(S3))

# This code is contributed by akashish__
