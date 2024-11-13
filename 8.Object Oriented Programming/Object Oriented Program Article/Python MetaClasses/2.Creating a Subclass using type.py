class FoodType(object):
    def __init__(self, ftype):
        self.ftype = ftype


def getFtype(self):
    return self.ftype


class VegType(FoodType):
    def vegFoods(self):
        return {'Spinach', 'Bitter Guard'}


def main():
    vType = VegType(ftype='Vegetarian')


print(vType.getFtype())
print(vType.vegFoods())

main()
