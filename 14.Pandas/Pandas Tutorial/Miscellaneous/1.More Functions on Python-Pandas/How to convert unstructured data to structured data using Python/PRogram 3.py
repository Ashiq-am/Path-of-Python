# Punch Records should start with
# the keyword 'in'. If it doesn't
# follow then we wil add 'in' and it
# significants that the employee forgot
# to do punch in
in_time = []
for i in range(len(second_door)):
    try:
        if ':in(Second Door)' not in second_door[i][0]:
            second_door[i].insert(0, 'in')

    except:
        pass

# Punch Records should end with the keyword
# 'out'. If it doesn't follow then we wil
# add 'out' and it significants that the
# employee forgot to do punch out
out_time = []
for i in range(len(second_door)):
    try:

        if ':out(Second Door)' not in second_door[i][(len(second_door[i])) - 1]:
            second_door[i].insert(((len(second_door[i]))), 'out')
    except:
        pass
second_door[0]
