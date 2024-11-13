# Python program for the above approach

# Function to find the frequency of
# all character after performing N operations
def processString(S, Dict):
    N = len(S);
    mx = '';

    # Vector to store the frequency
    # of all characters
    ans = [0 for i in range(26)];
    for i in range(N):
        mx = chr(96);
        for j in range(i + 1):
            mx = chr(max(ord(mx), ord(S[j])));

        for j in range(i + 1):

            # If S[j] is ord('a') and
            # Dict[S[j]] is -1 then
            # make S[j] equals to 'z'
            if (ord(S[j]) + Dict[ord(mx) - ord('a')] < 97):
                S[j] = ord(S[j] + Dict[ord(mx) - ord('a')] + 26);

            # If S[j] is 'z' and
            # Dict[S[j]] is 1
            # then make S[j] equals to ord('a')
            elif (ord(S[j]) + Dict[ord(mx) - ord('a')] > 122):
                S[j] = ord(ord(S[j]) + Dict[ord(mx) - ord('a')] - 26);


            else:
                tempc = chr(ord(S[j]) + Dict[ord(mx) - ord('a')]);
                S = S[0:j] + tempc + S[j:]
            # S[j] = tempc;

    for i in range(N):
        ans[ord(S[i]) - ord('a')] += 1;

    for x in ans:
        print(x, end=" ");


# Driver code
if __name__ == '__main__':
    S = "ab";
    Dict = [1, -1, 1, 1, 1, -1, 1, 1, 1,
            -1, 1, -1, 1, -1, 1, 1, 1,
            1, -1, -1, -1, 1, 1, -1, 1 - 1];
    processString(S, Dict);

# This code is contributed by 29AjayKumar
