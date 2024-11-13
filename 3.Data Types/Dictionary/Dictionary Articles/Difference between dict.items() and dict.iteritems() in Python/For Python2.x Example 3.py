# Python2 code to demonstrate
# d.items()


d = {
    "fantasy": "harrypotter",
    "romance": "me before you",
    "fiction": "divergent"
}

# places the tuples in a list.
print(d.items())

# returns iterators and never builds a list fully.
print(d.iteritems())
