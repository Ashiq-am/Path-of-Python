# final_in contains PUNCH - IN
# records for all employees
final_in = []

# final_out contains PUNCH - OUT
# records for all employees
final_out = []

for k in range(len(second_door)):
    in_gate = []
    out_gate = []

    # even positon should be for Punch-
    # IN and odd position should be for
    # Punch - OUT if it doesn't follow
    # then we will create the pattern by
    # putting 'in' or 'out'
    for i in range(len(second_door[k])):
        if i % 2 == 0 and 'in' in second_door[k][i]:
            in_gate.append(second_door[k][i])
            try:
                if 'out' not in second_door[k][i + 1]:
                    out_gate.append('out')
            except:
                pass
        if i % 2 != 0 and 'out' in second_door[k][i]:
            out_gate.append(second_door[k][i])
            try:
                if 'in' not in second_door[k][i + 1]:
                    in_gate.append('in')
            except:
                pass
        if i % 2 != 0 and 'in' in second_door[k][i]:
            in_gate.append(second_door[k][i])

            try:
                if 'out' not in second_door[k][i + 1]:
                    out_gate.append('out')
            except:
                pass

        if i % 2 == 0 and 'out' in second_door[k][i]:
            out_gate.append(second_door[k][i])

            try:
                if 'in' not in second_door[k][i + 1]:
                    in_gate.append('in')
            except:
                pass
    final_in.append(in_gate)
    final_out.append(out_gate)

# final_in or final_out keep the
# records as a list under list form.
# to solve the problem we will merge the list

# aa contains merged list of Punch - IN
aa = final_in[0]
for i in range(len(final_in) - 1):
    aa = aa + final_in[i + 1]

# bb contains merged list of Punch - OUT
bb = final_out[0]
for i in range(len(final_out) - 1):
    bb = bb + final_out[i + 1]

for i in range(len(final_in[0])):
    print(final_in[0][i], ' ', final_out[0][i])
