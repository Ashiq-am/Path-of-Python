# import tkinter module
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Read-Only Text Widget Example")
root.geometry("400x300")

# Create the Text widget
text_widget = tk.Text(root, wrap='word', height=10, width=40)
text_widget.pack(padx=10, pady=10)

# Insert some text into the Text widget
sample_text = """This is an example of a read-only Text widget.You can display multiple lines of text here.
                 However, users won't be able to modify this text.
              """
text_widget.insert(tk.END, sample_text)

# Make the Text widget read-only
text_widget.config(state=tk.DISABLED)

# Run the main event loop
root.mainloop()
