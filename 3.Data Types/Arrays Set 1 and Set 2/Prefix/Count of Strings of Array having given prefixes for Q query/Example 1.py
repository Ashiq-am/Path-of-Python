# Python3 code to implement the approach

# Function to return an array containing
# the number of words having the given prefix
# for each query
def GeekAndString(words, Queries) :
    ans = [];
    for x in Queries :

        # To count number of number of
        # matching prefixes in word array
        count = 0;
        for word in words :

            if len(word) < len(x) :
                continue;

            # If prefix found then increment counter
            if (word[0 : len(x)] == x) :
                count += 1;

        ans.append(count);

    return ans;

# Driver Code
if __name__ == "__main__" :

    words = [ "geekf", "geeks", "geeksforgeeks","string", "strong" ];
    queries = [ "geek", "gel", "str" ];

    # Function call
    ans = GeekAndString(words, queries);
    for x in ans:
        print(x,end=" ");

    # This code is contributed by AnkThon