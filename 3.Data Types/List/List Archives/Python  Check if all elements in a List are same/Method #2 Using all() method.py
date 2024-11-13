# Python program to check if all
# elements in a List are same
res = False


def chkList(lst):
    if len(lst) < 0:
        res = True
    res = all(ele == lst[0] for ele in lst)

    if (res):
        print("Equal")
    else:
        print("Not equal")

    # Driver Code


lst = ['Geeks', 'Geeks', 'Geeks', 'Geeks']
chkList(lst)
