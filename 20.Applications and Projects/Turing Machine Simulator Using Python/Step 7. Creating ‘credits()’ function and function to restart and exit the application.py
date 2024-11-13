def restart(self):
    for widget in self.winfo_children():
        widget.destroy()
    self.create_welcome_page()


def exit(self):
    for widget in self.winfo_children():
        widget.destroy()

    self.exit_frame = tk.Frame(self)
    self.exit_frame.pack(pady=30)

    self.exit_label = tk.Label(self.exit_frame
                               , font=('Helvetica', 24))

    self.exit_label.config(text='Thank'
                                + 'You for using the Simulator')
    self.exit_label.pack()

    self.after(1000, self.destroy)


def credits(self):
    made_by_label = tk.Label(self, text='GFG',
                             font=('Helvetica', 10)
                             , fg='blue', cursor='hand2')
    made_by_label.pack(side='bottom', pady=10)
    made_by_label.bind('<Button-1>'
                       , lambda e: webbrowser.open_new("https:"
                                                       + "//www.geeksforgeeks.org/"))
