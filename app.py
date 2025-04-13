from flask import Flask, render_template, jsonify, request
import requests
import certifi

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get_quote", methods=["POST"])
def get_quote():
    try:
        # Explicitly use the certifi certificate bundle
        res = requests.get("https://zenquotes.io/api/random", verify=certifi.where())
        data = res.json()
        quote = f"{data[0]['q']} — {data[0]['a']}"

    except Exception as e:
        print("⚠️ Error fetching quote:", e)
        quote = "Push yourself, because no one else is going to do it for you. — Anonymous"

    return jsonify({'reply': quote})


if __name__ == '__main__':
    app.run(debug=True)





