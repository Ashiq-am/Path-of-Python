# Python program to print all
# prime number in an interval
#number should be greater than 1
start = 11
end = 25

for i in range(start,end):
    if i>1:
        for j in range(2,i):
            if(i % j==0):
                break

        else:
            print(i)
