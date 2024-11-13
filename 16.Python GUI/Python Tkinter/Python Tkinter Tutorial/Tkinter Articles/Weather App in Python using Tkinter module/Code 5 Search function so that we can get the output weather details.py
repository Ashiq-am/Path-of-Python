# explicit function to
# search city
def search():
    city = city_text.get()
    weather = getweather(city)

    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3]) + " Degree Celsius"
        weather_l['text'] = weather[4]

    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))
