# Python3 program to Reverse order
# of incrementing integers in list

def reverseOrder(lst):
    break_ = [0] + [i for i in range(1, len(lst))
                    if lst[i - 1] > lst[i]] + [len(lst)]

    block = [list(reversed(lst[i:j]))
             for i, j in zip(break_[:-1], break_[1:])]

    return (sum(block, []))


# Driver code
lst = [0, 1, 9, 8, 7, 5, 3, 14]
print(reverseOrder(lst))
