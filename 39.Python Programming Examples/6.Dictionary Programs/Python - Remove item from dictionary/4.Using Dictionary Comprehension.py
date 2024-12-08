a = {1:"Apple", 2:"Banana", 3:"Grapes", 4:"Orange", 5: "Plum"}

# removing item with key 3 using dictionary comprehension
b = {key: a[key] for key in a if key != 3}
print(b)