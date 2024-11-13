# Python Program for find commom element using two array
import array

arr1 = array.array('i', [1, 2, 3, 4, 5])
arr2 = array.array('i', [3, 4, 5, 6, 7])
result = array.array('i')

print("Common elements are:", end=" ")

# To traverse array1.
for i in range(len(arr1)):
    # To traverse array2.
    for j in range(len(arr2)):
        # To match elements of array1 with elements of array2.
        if arr1[i] == arr2[j]:
            # Check whether the found element is already present in the result array or not.
            if arr1[i] not in result:
                result.append(arr1[i])
                print(arr1[i], end=" ")
                break
