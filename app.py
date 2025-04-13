# app.py
from flask import Flask, render_template, jsonify, request
import requests
import certifi
import os # Import os to access environment variables

app = Flask(__name__)

@app.route('/')
def index():
    # Assuming you have an index.html in a 'templates' folder
    return render_template('index.html')

@app.route("/get_quote", methods=["POST"])
def get_quote():
    try:
        # Explicitly use the certifi certificate bundle
        res = requests.get("https://zenquotes.io/api/random", verify=certifi.where())
        res.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        data = res.json()
        # Check if data is received and has the expected structure
        if data and isinstance(data, list) and len(data) > 0 and 'q' in data[0] and 'a' in data[0]:
            quote = f"{data[0]['q']} — {data[0]['a']}"
        else:
            print("⚠️ Unexpected data format received from API:", data)
            quote = "Be yourself; everyone else is already taken. — Oscar Wilde" # Different default quote
    except requests.exceptions.RequestException as e:
        print("⚠️ Error fetching quote (RequestException):", e)
        quote = "Act as if what you do makes a difference. It does. — William James" # Different default quote
    except Exception as e:
        print("⚠️ An unexpected error occurred:", e)
        quote = "Push yourself, because no one else is going to do it for you. — Anonymous" # Original default

    return jsonify({'reply': quote})


# This block is for running locally (e.g., python app.py)
# Gunicorn/Railway will ignore this based on the Procfile/Start Command
if __name__ == '__main__':
    # Use the PORT environment variable if available, otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Run on 0.0.0.0 to be accessible externally if needed locally
    app.run(host='0.0.0.0', port=port, debug=True)


