# declare set1
set1 = {"java", "python", "c/cpp", "html"}

# declare set2
set2 = {"php", "html", "java", "R"}

# declare set3
set3 = {"java", "python", "ml", "dl"}

# declare set4
set4 = {"python", "java", "swift", "R"}

# display sets
print(set1, set2, set3, set4)

# perform intersection_update operation on
# all the sets
set.intersection_update(set1, set2, set3, set4)

# display the result set
print(set1)
