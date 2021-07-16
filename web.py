from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def home():
    files = [os.join("pet", f) for f in os.listdir("pet") if os.isfile(f)]
    return render_template("index.html.jinja", pets=files)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")