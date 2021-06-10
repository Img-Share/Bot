from flask import Flask

app = Flask()

@app.route('/')
def home():
    return 'wip'

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1")