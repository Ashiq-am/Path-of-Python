# Before optimization
for obj in objects:
    obj.method()

# After optimization
method = obj.method
for obj in objects:
    method()