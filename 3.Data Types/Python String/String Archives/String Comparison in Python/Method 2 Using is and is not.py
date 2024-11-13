str1 = "Geek"
str2 = "Geek"
str3 = str1

print("ID of str1 =", hex(id(str1)))
print("ID of str2 =", hex(id(str2)))
print("ID of str3 =", hex(id(str3)))
print(str1 is str1)
print(str1 is str2)
print(str1 is str3)

str1 += "s"
str4 = "Geeks"

print("\nID of changed str1 =", hex(id(str1)))
print("ID of str4 =", hex(id(str4)))
print(str1 is str4)
