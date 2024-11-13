#initalizing the list
list1 = ["gf", "i", "be"]
list2 = ["g", "s", "st"]

#performing the zip() function
ans = [i[0]+i[1] for i in zip(list1, list2)]

#displaying the output
print(ans)
