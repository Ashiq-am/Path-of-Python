import array

def find_common_elements(arr1, arr2):
    # Convert arrays to lists for sorting
    arr1_list = list(arr1)
    arr2_list = list(arr2)

    # Sort both lists in non-decreasing order
    arr1_list.sort()
    arr2_list.sort()

    # Initialize pointers
    pointer1 = 0
    pointer2 = 0

    # Initialize an empty array to store common elements
    common_elements = array.array('i')

    # Iterate through both arrays simultaneously
    while pointer1 < len(arr1_list) and pointer2 < len(arr2_list):
        # If the elements pointed by pointer1 and pointer2 are equal
        if arr1_list[pointer1] == arr2_list[pointer2]:
            # Add the element to the result array
            common_elements.append(arr1_list[pointer1])
            # Move both pointers forward
            pointer1 += 1
            pointer2 += 1
        # If the element in arr1 pointed by pointer1 is less than the element in arr2 pointed by pointer2
        elif arr1_list[pointer1] < arr2_list[pointer2]:
            # Move pointer1 forward
            pointer1 += 1
        # If the element in arr2 pointed by pointer2 is less than the element in arr1 pointed by pointer1
        else:
            # Move pointer2 forward
            pointer2 += 1

    return common_elements


# Test the function with example arrays
arr1 = array.array('i', [1, 2, 3, 4, 5])
arr2 = array.array('i', [3, 4, 5, 6, 7])
common_elements = find_common_elements(arr1, arr2)
print("Common elements:",)
for element in common_elements:
    print(element,)
