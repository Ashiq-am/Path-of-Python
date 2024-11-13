import tkinter as tk

def toggle_switch(row, col):
    if switches[row][col] == 0:
        switches[row][col] = 1
    else:
        switches[row][col] = 0
    update_lights()


def update_lights():
    for row in range(5):
        for col in range(5):
            if switches[row][col] == 0:
                lights[row][col].configure(bg='black')
            else:
                lights[row][col].configure(bg='yellow')


window = tk.Tk()
window.title("Light Switch Puzzle")

switches = [[0 for _ in range(5)] for _ in range(5)]
lights = [[None for _ in range(5)] for _ in range(5)]

for row in range(5):
    for col in range(5):
        switch_button = tk.Button(
            window, width=10, height=5, bg='black', command=lambda r=row, c=col: toggle_switch(r, c))
        switch_button.grid(row=row, column=col, padx=5, pady=5)
        lights[row][col] = switch_button

window.mainloop()
