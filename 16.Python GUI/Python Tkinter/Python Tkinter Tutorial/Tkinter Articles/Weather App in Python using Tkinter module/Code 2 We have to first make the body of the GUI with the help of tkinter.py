# create object
app = Tk()

# add title
app.title("Weather App")

# adjust window size
app.geometry("300x300")

# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

Search_btn = Button(app, text="Search Weather",
					width=12, command=search)
Search_btn.pack()

location_lbl = Label(app, text="Location",
					font={'bold', 20})
location_lbl.pack()

temperature_label = Label(app, text="")
temperature_label.pack()

weather_l = Label(app, text="")
weather_l.pack()

app.mainloop()
