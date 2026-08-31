from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    city = "Hyderabad"
    weather = requests.get(f"https://wttr.in/{city}?format=3").text
    return weather

if __name__ == "__main__":
    app.run(debug=True)