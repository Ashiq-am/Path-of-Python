def tree_sort(arr):
    if not arr:
        return arr

    root = None
    for key in arr:
        root = insert(root, key)

    sorted_arr = []
    inorder_traversal(root, sorted_arr)
    return sorted_arr
