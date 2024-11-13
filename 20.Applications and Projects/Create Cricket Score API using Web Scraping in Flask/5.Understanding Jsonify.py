from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def cricgfg():
    # Creating a dictionary with data to test jsonfiy.
    result = {
        "Description": "Live score England vs India 3rd Test,Pataudi \
		Trophy, 2021",
        "Location": "Headingley, Leeds",
        "Status": "England lead by 223 runs",
        "Current": "Day 2 | Post Tea Session",
        "Team A": "England",
        "Team A Score": "301/3 (96.0)",
        "Team B": "India",
        "Team B Score": "78",
        "Full Scoreboard": "https://sports.ndtv.com//cricket/live-scorecard\
		/england-vs-india-3rd-test-leeds-enin08252021199051",
        "Credits": "NDTV Sports"
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
