x = []
x.append(l)
x.append(2)

# delete the list from memory or
# assigning object x to None(Null)
del x
# x = None





#The reference count for the list created is now two. However,
# since it cannot be reached from inside Python and cannot possibly be used again,
# it is considered garbage. In the current version of Python, this list is never freed.