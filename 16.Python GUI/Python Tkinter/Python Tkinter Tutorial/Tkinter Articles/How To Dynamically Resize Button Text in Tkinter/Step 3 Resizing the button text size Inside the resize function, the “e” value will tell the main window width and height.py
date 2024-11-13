# resize button text size
def resize(e):
    # get window width
    size = e.width / 10

    # define text size on diffrent condition

    # if window height is greater
    # than 300 and less than 400 (set font size 40)
    if e.height <= 400 and e.height > 300:
        button_1.config(font=("Helvetica", 40))

    # if window height is greater than
    # 200 and less than 300 (set font size 30)
    elif e.height < 300 and e.height > 200:
        button_1.config(font=("Helvetica", 30))

    # if window height is less than 200 (set font size 40)
    elif e.height < 200:
        button_1.config(font=("Helvetica", 40))
