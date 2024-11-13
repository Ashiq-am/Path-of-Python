s1 = {2, 5, 3, 7, 'c', 'a', 8}
s2 = {3, 7, 8, 'c'}

# subset check
w = s1 <= s2

# proper subset check
x = s1 < s2

# superset check
y = s1 >= s2

# proper superset check
z = s1 > s2
print(w, x, y, z)
