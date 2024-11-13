def uncommon(a,b):

    a=a.split()
    b=b.split()
    k=set(a).symmetric_difference(set(b))
    return k

#Driver code
if __name__=="__main__":
    a="apple banana mango"
    b="banana fruits mango"
    print(list(uncommon(a,b)))
