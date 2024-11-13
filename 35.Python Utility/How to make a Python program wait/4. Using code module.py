# import code
import code

print("GeeksforGeeks printed immediately.")

# implementation of code.interact().
code.interact(banner='Paused. Press ^D (Ctrl+D) to continue.', local=globals())
print("GeeksforGeeks.")
