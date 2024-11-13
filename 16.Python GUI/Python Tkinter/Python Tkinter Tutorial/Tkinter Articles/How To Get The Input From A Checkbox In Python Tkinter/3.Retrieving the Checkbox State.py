def get_checkbox_state():
    if check_var.get():
        print("Checkbox is checked")
    else:
        print("Checkbox is unchecked")

submit_button = tk.Button(root, text="Submit",
                          command=get_checkbox_state)
submit_button.pack(pady=10)
