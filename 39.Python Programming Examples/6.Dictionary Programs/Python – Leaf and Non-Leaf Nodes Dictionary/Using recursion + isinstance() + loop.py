# Python3 code to demonstrate working of
# Leaf and Non-Leaf Nodes Dictionary
# Using recursion + isinstance() + loop

def hlpr_fnc(dict1, res={'non-leaf': 0, 'leaf': 0}):
    # res['non-leaf'] += 1
    nodes = dict1.keys()
    for node in nodes:
        subnode = dict1[node]
    if isinstance(subnode, dict):
        res['non-leaf'] += 1
        hlpr_fnc(subnode, res)
    else:
        res['leaf'] += 1
    return res


# initializing dictionary
test_dict = {'a': {'b': 1, 'c': {'d': {'e': 2, 'f': 1}}, 'g': {'h': {'i': 2, 'j': 1}}}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Leaf and Non-Leaf Nodes Dictionary
# Using recursion + isinstance() + loop
res = hlpr_fnc(test_dict)

# printing result
print("The leaf and Non-Leaf nodes : " + str(res))
