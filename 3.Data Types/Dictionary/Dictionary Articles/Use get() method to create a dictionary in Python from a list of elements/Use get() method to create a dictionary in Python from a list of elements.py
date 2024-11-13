li = ['a', 'b', 'c', 'a', 'd', 'e', 'b', 'a']
di = {}

for ele in li:

    # Increase the value of key
    # if exists
    if ele in di:
        di[ele] = di[ele] + 1
    else:

        # Insert the new key:value
        # pair
        di[ele] = 1

print(di)
