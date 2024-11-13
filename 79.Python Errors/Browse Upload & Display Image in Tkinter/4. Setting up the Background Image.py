# Main method
if __name__ == "__main__":

	# defining tkinter object
	app = tk.Tk()

	# setting title and basic size to our App
	app.title("GeeksForGeeks Image Viewer")
	app.geometry("560x270")

	# adding background image
	img = ImageTk.PhotoImage(file='gfglogo1.png')
	imgLabel = Label(app, image=img)
	imgLabel.place(x=0, y=0)
