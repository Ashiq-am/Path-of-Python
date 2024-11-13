# main app class
class Main(MDApp):
    def build(self):
        return Builder.load_string(KV)

    # creating a function for time_picker
    def show_time_picker(self):
        # converting string to time format
        default_time = datetime.strptime("12:00:00", '%H:%M:%S').time()
        # gets time picker
        t = MDTimePicker()
        # Setting the default time for time picker
        t.set_time(default_time)
        # opens time picker
        t.open()


# running app
Main().run()
