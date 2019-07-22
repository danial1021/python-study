from flask import Flask # flask라는 모듈에서 Flask라는 class를 import

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()