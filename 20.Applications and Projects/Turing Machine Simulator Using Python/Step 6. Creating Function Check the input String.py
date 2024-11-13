def check_string(self):
    string = self.string_input.get()
    option = self.selected_option.get()
    if option == 0:
        if self.accepts_odd_ones_even_zeros(string):
            messagebox.showinfo("Result",
                                f"The string '{string}' is accepted.")
        else:
            messagebox.showinfo("Result",
                                f"The string '{string}' is not accepted.")
    elif option == 1:
        if self.accepts_even_ones_odd_zeros(string):
            messagebox.showinfo("Result",
                                f"The string '{string}' is accepted.")
        else:
            messagebox.showinfo("Result",
                                f"The string '{string}' is not accepted.")
    elif option == 2:
        if self.accepts_even_ones_even_zeros(string):
            messagebox.showinfo("Result",
                                f"The string '{string}' is accepted.")
        else:
            messagebox.showinfo("Result",
                                f"The string '{string}' is not accepted.")
    elif option == 3:
        if self.accepts_odd_ones_odd_zeros(string):
            messagebox.showinfo("Result",
                                f"The string '{string}' is accepted.")
        else:
            messagebox.showinfo("Result",
                                f"The string '{string}' is not accepted.")

    restart_button = tk.Button(self, text='Restart',
                               font=('sans-serif', 12), command=self.restart)
    restart_button.pack(side="left", padx=115, pady=30)

    exit_button = tk.Button(self, text='Exit', padx=10,
                            font=('sans-serif', 12), command=self.exit)
    exit_button.pack(side="left", padx=125, pady=30)


def accepts_odd_ones_even_zeros(self, string):
    state = 0
    for symbol in string:
        if state == 0:
            if symbol == '0':
                state = 2
            elif symbol == '1':
                state = 1
            else:
                return False
        elif state == 1:
            if symbol == '0':
                state = 3
            elif symbol == '1':
                state = 0
            else:
                return False
        elif state == 2:
            if symbol == '0':
                state = 0
            elif symbol == '1':
                state = 3
            else:
                return False
        elif state == 3:
            if symbol == '0':
                state = 1
            elif symbol == '1':
                state = 2
            else:
                return False
    return state == 1


def accepts_even_ones_odd_zeros(self, string):
    state = 0
    for symbol in string:
        if state == 0:
            if symbol == '0':
                state = 2
            elif symbol == '1':
                state = 1
            else:
                return False
        elif state == 1:
            if symbol == '0':
                state = 3
            elif symbol == '1':
                state = 0
            else:
                return False
        elif state == 2:
            if symbol == '0':
                state = 0
            elif symbol == '1':
                state = 3
            else:
                return False
        elif state == 3:
            if symbol == '0':
                state = 1
            elif symbol == '1':
                state = 2
            else:
                return False
    return state == 2


def accepts_even_ones_even_zeros(self, string):
    state = 0
    for symbol in string:
        if state == 0:
            if symbol == '0':
                state = 1
            elif symbol == '1':
                state = 2
            else:
                return False
        elif state == 1:
            if symbol == '0':
                state = 0
            elif symbol == '1':
                state = 3
            else:
                return False
        elif state == 2:
            if symbol == '0':
                state = 3
            elif symbol == '1':
                state = 0
            else:
                return False
        elif state == 3:
            if symbol == '0':
                state = 2
            elif symbol == '1':
                state = 1
            else:
                return False
    return state == 0


def accepts_odd_ones_odd_zeros(self, string):
    state = 0
    for symbol in string:
        if state == 0:
            if symbol == '0':
                state = 2
            elif symbol == '1':
                state = 1
            else:
                return False
        elif state == 1:
            if symbol == '0':
                state = 3
            elif symbol == '1':
                state = 0
            else:
                return False
        elif state == 2:
            if symbol == '0':
                state = 0
            elif symbol == '1':
                state = 3
            else:
                return False
        elif state == 3:
            if symbol == '0':
                state = 1
            elif symbol == '1':
                state = 2
            else:
                return False
    return state == 3
