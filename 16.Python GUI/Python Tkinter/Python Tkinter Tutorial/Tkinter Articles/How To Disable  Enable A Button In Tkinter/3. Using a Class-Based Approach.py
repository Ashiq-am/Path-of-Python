import tkinter as tk

class ButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Class-Based Approach Example")

        # Create the main button
        self.button = tk.Button(root, text="Click Me!",
                                command=self.disable_button)
        self.button.pack(pady=20)

        # Create the button to enable the main button
        self.enable_btn = tk.Button(
            root, text="Enable Button", command=self.enable_button)
        self.enable_btn.pack(pady=20)

    def disable_button(self):
        self.button.config(state=tk.DISABLED)

    def enable_button(self):
        self.button.config(state=tk.NORMAL)


# Create the main window
root = tk.Tk()

# Instantiate the application
app = ButtonApp(root)

# Run the application
root.mainloop()
