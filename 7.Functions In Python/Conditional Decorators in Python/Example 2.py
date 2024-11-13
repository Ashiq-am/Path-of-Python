def decorator1(func):
    def wrapper():
        oldstring = func()
        newstring = oldstring.upper()
        return newstring

    return wrapper


def decorator2(func):
    def wrapper():
        oldstring = func()
        newstring = oldstring.lower()
        return newstring

    return wrapper


cond = 1

if cond == 1:
    @decorator1
    def func():
        return 'GeeksFORGeeKs'
elif cond == 2:
    @decorator2
    def func():
        return 'GeeksFORGeeKs'
else:
    def func():
        return 'GeeksFORGeeKs'

print(func())
