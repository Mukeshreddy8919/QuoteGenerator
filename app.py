from flask import Flask, render_template, jsonify, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_quote', methods=['POST'])
def get_quote():
    try:
        res = requests.get("http://api.quotable.io/random?tags=inspirational")
        res.raise_for_status()
        data = res.json()
        quote = f"{data['content']} — {data['author']}"
    except Exception as e:
        print("⚠️ Error fetching quote:", e)
        quote = "Push yourself, because no one else is going to do it for you. — Anonymous"

    return jsonify({'reply': quote})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)


