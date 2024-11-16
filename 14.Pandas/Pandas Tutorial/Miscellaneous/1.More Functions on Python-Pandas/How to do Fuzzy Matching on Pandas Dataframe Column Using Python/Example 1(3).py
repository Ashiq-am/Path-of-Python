# iterating through the closest
# matches to filter out the
# maximum closest match
for j in dframe1['matches']:
    for k in j:

        if k[1] >= threshold:
            p.append(k[0])

    mat2.append(",".join(p))
    p = []

# storing the resultant matches
# back to dframe1
dframe1['matches'] = mat2

dframe1.show()
