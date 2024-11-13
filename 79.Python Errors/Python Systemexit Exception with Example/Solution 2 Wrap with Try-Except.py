import sys


def exit_safely(message):
    try:
        sys.exit(message)
    except SystemExit as e:
        print(f"Caught SystemExit: {e}")


# Call the function instead of sys.exit directly
exit_safely("Exiting the program")

# Continue with the program execution if needed
print("Program continues after handling SystemExit")
