import array

arr = array.array('i', [10, 20, 30, 20, 50])

# Loop through the array to find the index of 20
for i in range(len(arr)):
    if arr[i] == 20:
        print(i)
        break
