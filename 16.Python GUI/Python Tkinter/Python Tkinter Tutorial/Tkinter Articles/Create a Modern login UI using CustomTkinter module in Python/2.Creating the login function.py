# defining the login function
def login():
    # pre-defined username
    username = "Geeks"
    # pre-defined password
    password = "12345"

    new_window = ctk.CTkToplevel(app)

    new_window.title("New Window")

    new_window.geometry("350x150")

    """If user provides the above username and password
           then a success window will be shown 
           and a new window will open with a simple message"""
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
        ctk.CTkLabel(new_window, text="GeeksforGeeks is best for learning ANYTHING !!").pack()

    #If the user provides the correct username but
     #the password is wrong then an warning window
     #will be shown

    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title="Wrong password", message="Please check your password")


    # If the user provides the wrong username but
        # the password is correct then an warning window
    # will be shown

    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username', message='Please check your username')


    #If the user provides wrong username and password
    # both then an error window will be shown
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")

