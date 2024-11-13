import tkinter as tk

def approach_2():
    # Create the main window
    root = tk.Tk()

    # Set the window size
    root.geometry("400x300")

    # Change the title bar text using wm_title
    root.wm_title("Custom Title Bar - Approach 2")

    # Run the application
    root.mainloop()

approach_2()
