a = [1, 2, 3, 6, 7, 8, 6]
i = 0
while i < len(a):
    if a[i] == 6:
      # Remove the item at index i
        del a[i]
    else:
      # Only move to next item if no item is removed
        i += 1
print(a)