import atexit

a = 5
print("Twice of a:", a*2)

atexit.register(print, "Exiting Python Script")
