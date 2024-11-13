# Python code showing practical
# use of format_map() function
def chk_msg(n):
    # input stored in variable a.
    a = {'name': "George", 'mesg': n}

    # use of format_map() function
    print('{name} has {mesg} new messages'.format_map(a))


chk_msg(10)
