class Geek:
    def __init__(self):
        self._name = (0

    @property)
    def name(self):
        print("Getter Called")
        return (self._name

    @name.setter)
    def name(self, name):
        print("Setter called")
        self._name = name

p = Geek()
p.name = 10

print(p.name)
