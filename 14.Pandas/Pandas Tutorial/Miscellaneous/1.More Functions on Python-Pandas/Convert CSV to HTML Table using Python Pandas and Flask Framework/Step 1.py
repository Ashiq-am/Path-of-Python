# importing flask
from flask import Flask, render_template

# importing pandas module
import pandas as pd

app = Flask(__name__)

# reading the data in the csv file
df = pd.read_csv('sample_data.csv')
df.to_csv('sample_data.csv', index=None)


# route to html page - "table"
@app.route('/')
@app.route('/table')
def table():
    # converting csv to html
    data = pd.read_csv('sample_data.csv')
    return render_template('table.html', tables=[data.to_html()], titles=[''])


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
