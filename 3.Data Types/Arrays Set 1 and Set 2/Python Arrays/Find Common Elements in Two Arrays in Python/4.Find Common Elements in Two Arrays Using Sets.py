# Python Program for the above approach
from array import array
def find_common_elements(arr1, arr2):
    # Convert arrays to sets for faster lookup
    set1 = set(arr1)
    set2 = set(arr2)
    # Find intersection of the sets (common elements)
    common_elements = set1.intersection(set2)
    return list(common_elements)

# Driver Code
arr1 = array('i', [1, 2, 3, 4, 5])
arr2 = array('i', [3, 4, 5, 6, 7])
common_elements = find_common_elements(arr1, arr2)
print("Common elements:", common_elements)
