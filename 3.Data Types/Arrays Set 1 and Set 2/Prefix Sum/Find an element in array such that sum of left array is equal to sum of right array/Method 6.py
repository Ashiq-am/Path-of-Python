# Function to find equilibrium point in the array.
def sum(self, A):
    result = 0
    for item in A:
        result += item
    return result

def equilibriumPoint(self, A, N):
    # Your code here
    if N == 1:
        return 1
    eq_index = N // 2


    left_sum = self.sum(A[:eq_index])
    right_sum = self.sum(A[eq_index+1:])
    if (left_sum == right_sum):
        return eq_index + 1

    elif (left_sum > right_sum):
        while(eq_index >= 0):
            left_sum -= A[eq_index-1]
            right_sum += A[eq_index]
            eq_index -= 1
            if right_sum > left_sum:
                return -1
            elif left_sum == right_sum:
                return eq_index + 1


    elif (right_sum > left_sum):
        while(eq_index <= N-1):
            left_sum += A[eq_index]
            right_sum -= A[eq_index+1]
            eq_index += 1

            if left_sum > right_sum:
                return -1
            elif left_sum == right_sum:
                return eq_index + 1
    else:
        return -1
