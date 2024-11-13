# put unsafe operation in try block
try:
    print("code start")

    # unsafe operation perform
    print(1 / 0)

# if error occur the it goes in except block
except:
    print("an error occurs")

# final code in finally block
finally:
    print("GeeksForGeeks")
