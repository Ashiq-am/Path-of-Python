# UI SETUP - Whatever the user sees is handled here

# create constants that simply containers color codes,
# font family, sizes and styles

# COLORS
BORDER = "#3C2C3E"
FG = 'khaki'
BG = "#4B5D67"

# FONT FAMILIES
FONT_FAMILY1 = 'Calibri'
FONT_FAMILY2 = 'Helvetica'


# FONT SIZES
FONT_SIZE1 = 14
FONT_SIZE2 = 18
FONT_SIZE3 = 24


# FONT STYLES
FONT_STYLE1 = 'normal'
FONT_STYLE2 = 'italic'
FONT_STYLE3 = 'bold'

# creating a font from family, style and size for the UI
PARA_FONT = (FONT_FAMILY1, FONT_SIZE1, FONT_STYLE3)
PARA_FONT2 = (FONT_FAMILY1, 12, FONT_STYLE2)
HEAD_FONT = (FONT_FAMILY2, FONT_SIZE3, FONT_STYLE1)

# welcoming heading of our UI
heading = "WRITE WITH MAGICAL INK"
# instruction to use app
instruction = "If you don't press any key for 5 seconds,\
the text you have written will disappear"


# CREATING THE WINDOW IN WHICH OUR PROGRAM IS SEEN.

"""
1. Creating an window object in which our program
is seen using Tk class.
2. Give it a title that shows on the window's tab
using title method on window object.
3. Use config method of window object to set various
other properties: background color,
padding on x-axis and padding on y-axis. Padding
is simply the empty space between
contents and boundary of the window in
which our program is viewed.
"""
window = Tk()
window.title('Disappearing Text Desktop App')
window.config(bg=BG, padx=20, pady=10)


# CREATING WIDGETS FOR OUR APPLICATION

# heading.
heading = Label(text=heading, font=HEAD_FONT,
				bg=BG, fg=FG, padx=10, pady=10)

# instructions.
instruction = Label(text=instruction, font=PARA_FONT2,
					fg=FG, bg=BG, pady=10)

# typing area in which user types his text.
typing_area = Text(font=PARA_FONT, bg=BG, fg=FG,
				width=100, height=15, wrap='w',
				highlightcolor=BORDER,
				highlightthickness=4,
				highlightbackground=BORDER,
				padx=5, pady=5)

# attaching a function to text area. This function
# does main calculations for the app.
typing_area.bind('<KeyPress>', start_calculating)

# a reset button so that user can explicitly reset
# the application if he wants to.
reset_btn = Button(text='Reset', fg=FG, bg=BG, font=PARA_FONT,
				highlightbackground=FG,
				highlightcolor=FG,
				highlightthickness=0, border=3,
				command=reset_app, width=50)


# a save button for user to save his text in a text file
save_btn = Button(text='Save', fg=FG, bg=BG,
				font=PARA_FONT,
				highlightbackground=FG,
				highlightcolor=FG, highlightthickness=0,
				border=3,
				command=save_text, width=50)


# PLACING THE WIDGETS ON THE WINDOW
heading.grid(row=0, column=0, columnspan=3)
instruction.grid(row=2, column=0, columnspan=3)
typing_area.grid(row=3, column=0, columnspan=3)
reset_btn.grid(row=4, column=0)
save_btn.grid(row=4, column=2)

"""we keep the window open, until closed
explicity by user using
mainloop method of window object."""
window.mainloop()
