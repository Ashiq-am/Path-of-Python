@app.route('/', methods=['GET', 'POST'])

def home():
    if(request.method == 'POST'):
        db.session.add(Event(date=datetime.datetime.now().__str__(), event=request.form['eventBox']))
        db.session.commit()
        return redirect(url_for('home'))
        return render_template('home.html', eventsList=db.session.execute(db.select(Event).order_by(Event.date)).scalars())

    return app
