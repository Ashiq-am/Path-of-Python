def compare(p1, p2, user_input):
    # store the follower count of
    # account1 in a variable
    sum1 = p1['follower_count']

    # store the follower count of
    # account2 in a variable
    sum2 = p2['follower_count']

    # make an empty variable max, where
    # we will store the name of account
    # with highest followers, then compare
    # it with user input name.
    max = ""

    # if account1 has greater follower count
    if sum1 > sum2:

        # max is name of account1
        max = p1['name']
    elif sum1 < sum2:

        # otherwise, if account2 has higher
        # follower count,
        # max is name of account two.
        max = p2['name']

    # now compare the name of account with greater
    # follwoer count againt the user input name,
    # if user is correct, retunr True
    if max == user_input:
        return True
    else:
        # otherwise retunr False
        return False
