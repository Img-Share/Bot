from flask import Flask, render_template
import os, os.path

from flask.helpers import send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    files = [f for f in os.listdir("pet") if os.path.isfile(os.path.join("pet", f))]
    return render_template("index.html.jinja", pets=files)
@app.route("/pets/<pet>")
def pet(pet):
    return send_from_directory("pet", pet)
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")