# Python3 code to implement the approach

# Function to return incremented string
# after all the operations
def findRollOut(s, a, n):
    s = list(s);
    # Initialize an array of size
    # N+1 and make it to 0
    arr = [0] * (n + 1);

    # Increment arr[0] by 1 and
    # decrement arr[a[i] by 1
    for i in range(n):
        arr[a[i]] -= 1;
        arr[0] += 1;

    # Make prefix array
    for i in range(1, n):
        arr[i] += arr[i - 1];

    # Increment the characters
    for i in range(n):
        arr[i] = (arr[i]) % 26;

        if (arr[i] + ord(s[i]) > ord('z')):
            s[i] = chr(ord(s[i]) + arr[i] - 26);
        else:
            s[i] = chr(ord(s[i]) + arr[i]);

    s = "".join(s);
    return s;


# Driver Code
if __name__ == "__main__":
    S = "bca";
    roll = [1, 2, 3];
    N = len(roll);

    # Function Call
    print(findRollOut(S, roll, N));

    # This code is contributed by AnkThon