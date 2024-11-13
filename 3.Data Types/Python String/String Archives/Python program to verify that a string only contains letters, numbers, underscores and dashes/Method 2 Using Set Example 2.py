allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-")

string = "__Val1d__"

validation = set((string))

if validation.issubset(allowed_chars):
    print("True")

else:
    print("False")
