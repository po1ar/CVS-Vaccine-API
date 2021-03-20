from flask import json, jsonify, Flask, render_template
import requests

app = Flask(__name__)
@app.route('/api')
def index():
 return "Hello world!"
@app.route('/api/<state>')
def api(state):
    headers = {
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "referer": "https://www.cvs.com/immunizations/covid-19-vaccine?icid=cvs-home-hero1-link2-coronavirus-vaccine",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36"
    }

    r = requests.get(f"https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.{state}.json?vaccineinfo", headers=headers)
    result = []
    try:
        for c in r.json()["responsePayloadData"]["data"][state.upper()]:
            if c["status"] != "Fully Booked":
                result.append(c['city'])
        return jsonify(result)
    except KeyError:
        return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)