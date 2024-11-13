def get():
    # accepting input from the user
    username = entryName.get()

    # creating a dictionary to store the data in the form of key-value pairs
    passwords = {}
    try:
        # opening the text file
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                # creating the key-value pair of username and password.
                passwords[i[0]] = i[1]
    except:
        # displaying the error message
        print("ERROR !!")

    if passwords:
        mess = "Your passwords:\n"
        for i in passwords:
            if i == username:
                mess += f"Password for {username} is {passwords[i]}\n"
                break
        else:
            mess += "No Such Username Exists !!"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "EMPTY LIST!!")
