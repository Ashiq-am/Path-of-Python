@app.route('/')
def home():
    # rendering the homepage of project
    return render_template("index.html")


@app.route('/CheckSlot')
def check():
    # for checking the slot available or not

    # fetching pin codes from flask
    pin = request.args.get("pincode")

    # fetching age from flask
    age = request.args.get("age")
    data = list()

    # finding the slot
    result = findSlot(age, pin, data)

    if (result == 0):
        return render_template("noavailable.html")
    return render_template("slot.html", data=data)
