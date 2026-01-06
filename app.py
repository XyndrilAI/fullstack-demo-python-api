from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Python backend running"

@app.route("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    app.run()
