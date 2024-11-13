def bell_numbers(n):
    # Initialize the previous row of the Bell triangle with dp[0] = 1
    dp = [1] + [0] * n

    for i in range(1, n+1):
        # The first element in each row is the same as the last element in the previous row
        prev = dp[0]
        dp[0] = dp[i-1]
        for j in range(1, i+1):
            # The Bell number for n is the sum of the Bell numbers for all previous partitions
            temp = dp[j]
            dp[j] = prev + dp[j-1]
            prev = temp

    return dp[0]


n = 5
print(bell_numbers(n))
