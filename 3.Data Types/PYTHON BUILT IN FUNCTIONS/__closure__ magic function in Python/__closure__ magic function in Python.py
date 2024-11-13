# this is a nested function
def gfg(raise_power_to):

    def power(number):
        return number ** raise_power_to
    return power

raise_power_to_3 = gfg(3)
print(raise_power_to_3.__closure__)

print(raise_power_to_3.__closure__[0].cell_contents)
