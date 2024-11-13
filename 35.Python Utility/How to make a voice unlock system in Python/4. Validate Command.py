if command == "lock my PC":
    ctypes.windll.user32.LockWorkStation()

elif command == "stop":
    sys.exit(0)

else:
    print("Not a command.")
    fxn()
