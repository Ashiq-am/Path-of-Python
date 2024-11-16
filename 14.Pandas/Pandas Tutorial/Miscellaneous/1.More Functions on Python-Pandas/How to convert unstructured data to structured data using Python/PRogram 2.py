# Splitting the values by comma in 1
# no column (punch records)
for i in range(len(abc)):
    abc[1][i] = abc[1][i].split(",")

second_door = []

for i in range(len(abc)):
    s_d = []

    # Extracting all the values which contains
    # only :in(Second Door) or :out(Second Dorr)
    for j in range(len(abc[1][i])):
        if ':in(Second Door)' in abc[1][i][j]:
            s_d.append(abc[1][i][j])

        if 'out(Second Door)' in abc[1][i][j]:
            s_d.append(abc[1][i][j])

    second_door.append(s_d)
(second_door[0])
