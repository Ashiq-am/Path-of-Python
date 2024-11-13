def distinct_substrings(s):
    n = len(s)
    substrings = set()  # Initialize an empty set to store the substrings
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.add(s[i:j])  # Add each substring to the set
    return substrings  # Return the set of substrings

def count_distinct_substrings(s):
    substrings = distinct_substrings(s)  # Get all distinct substrings
    counts = [0] * len(s)
    # Count the number of substrings of each length
    for substring in substrings:
        counts[len(substring)-1] += 1
    return counts  # Return the counts

def main():
    s = "abab"  # Define the string
    counts = count_distinct_substrings(s)
    print(*counts)  # Print the counts

if __name__ == "__main__":
    main()
