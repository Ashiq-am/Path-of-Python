def left_right_difference(arr):
    n = len(arr)
    left = 0
    sum = 0
    data = 0

    for i in range(n):
        sum += arr[i]

    for i in range(n):
        left += arr[i]
        data = abs(left - sum)
        sum -= arr[i]

        arr[i] = data

    return arr


N = 4
arr = [10, 4, 8, 3]

ans = left_right_difference(arr)
for i in range(N):
    print(ans[i], end=" ")
