def addition(decorated):
    class AddSubclass(Addition):
        def run(self, *args, **kwargs):

            if args:
                add = 0
                for arg in args:
                    add = arg + add
                return add

            else:
                return decorated(*args, **kwargs)

    return AddSubclass()
