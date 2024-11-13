# Python code for the above approach
# Function for finding sum of larger numbers
def findSum(str1, str2):
    # Before proceeding further, make
    # sure length of str2 is larger
    if (len(str1) > len(str2)):
        temp = str1;
        str1 = str2;
        str2 = temp;

    # Stores resulting sum
    str = [];

    # Calculate length of both string
    n1 = len(str1)
    n2 = len(str2)

    # Reverse both of strings
    str1 = list(str1)
    str2 = list(str2)
    str1.reverse();
    str2.reverse();

    carry = 0;
    for i in range(n1):
        # Compute sum of current
        # digits and carry
        sum = ((ord(str1[i]) - ord('0')) + (ord(str2[i]) - ord('0')) + carry);
        str.append(chr(sum % 10 + ord('0')));

        # Carry for next step
        carry = sum // 10

    # Add remaining digits
    for i in range(n1, n2):
        sum = ((ord(str2[i]) - ord('0')) + carry);
        str.append(chr(sum % 10 + ord('0')));
        carry = sum // 10

    # Add remaining carry
    if (carry):
        str.append(chr(carry + ord('0')));

    # Reverse string
    str.reverse();

    # Return Answer
    return ''.join(str)


# Function to find sum of all prefixes
# of a string representing a number
def sumPrefix(str):
    # Stores the desired sum
    sum = "0";

    # Stores the current prefix
    curPre = "";

    # Loop to iterate str
    for i in range(len(str)):
        # Update current prefix
        curPre += str[i];

        # Update Sum
        sum = findSum(curPre, sum);

    # Return Answer
    return sum;


# Driver Code
str = "1225";
print(sumPrefix(str));

# This code is contributed by Saurabh Jaiswal
