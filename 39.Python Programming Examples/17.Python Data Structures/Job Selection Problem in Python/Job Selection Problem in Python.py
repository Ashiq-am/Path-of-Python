# Python program to minimize loss using stable sort.
import functools
import operator
from typing import List


# compare function is given so that we can specify
# how to compare a pair of jobs
class cmp_pair:
    def __call__(self, a, b):
        a_Li, a_Ti, b_Li, b_Ti = a.li, a.ti, b.li, b.ti

        # To compare a/b and c/d, compare ad and bc
        return -1 if (a_Li * b_Ti) > (b_Li * a_Ti) else 1


class job:
    def __init__(self, i, l, t):
        self.index, self.ti, self.li = i, t, l


def printOptimal(L: List[int], T: List[int], N: int) -> None:
    job_list = []
    for i in range(N):
        t, l = T[i], L[i]

        # Each element is: (Job Index, (Li, Ti) )
        job_list.append(job(i + 1, l, t))
    job_list.sort(key=functools.cmp_to_key(cmp_pair()))

    # traverse the list and print job numbers
    print("Job numbers in optimal sequence are")
    for i in range(N):
        print(job_list[i].index, end=" ")


L = [1, 2, 3, 5, 6]
T = [2, 4, 1, 3, 2]
N = len(L)
printOptimal(L, T, N)
