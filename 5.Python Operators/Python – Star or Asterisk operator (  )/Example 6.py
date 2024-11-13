# using asterisk
def food(**kwargs):
    for items in kwargs:
        print(f"{kwargs[items]} is a {items}")


food(fruit='cherry', vegetable='potato', boy='srikrishna')
