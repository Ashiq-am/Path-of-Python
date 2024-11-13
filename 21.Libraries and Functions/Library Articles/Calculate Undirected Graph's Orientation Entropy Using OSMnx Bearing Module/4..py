bearings = []
min_length = 0
weight = None

for u, v, data in chicago_mdigr_bearing.edges(data=True):
    # ignore self-loops and checks minimum length
    if u != v and data["length"] >= min_length:
        if weight:
            # weight edges' bearings by some edge attribute value
            bearings.extend([data["bearing"]] * int(data[weight]))
        else:
            # don't weight bearings, just take one value per edge
            bearings.append(data["bearing"])

len(bearings)
