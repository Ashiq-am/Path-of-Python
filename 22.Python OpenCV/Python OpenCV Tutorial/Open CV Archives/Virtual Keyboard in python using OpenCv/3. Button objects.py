button_list = []

# Create Button objects based on keyboard_keys layout
for k in range(len(keyboard_keys)):
    for x, key in enumerate(keyboard_keys[k]):
        if key != "SPACE" and key != "ENTER" and key != "BACKSPACE":
            button_list.append(Button((100 * x + 25, 100 * k + 50), key))
        elif key == "ENTER":
            button_list.append(
                Button((100 * x - 30, 100 * k + 50), key, (220, 85)))
        elif key == "SPACE":
            button_list.append(
                Button((100 * x + 780, 100 * k + 50), key, (220, 85)))
        elif key == "BACKSPACE":
            button_list.append(
                Button((100 * x + 140, 100 * k + 50), key, (400, 85)))
