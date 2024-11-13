import atexit

@atexit.register
def gfg_exit_handler():
    print("Bye, Geeks!")

print("Hello, Geeks!")
