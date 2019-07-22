from flask import Flask
from flask import request
app = Flask(__name__)
@app.route('/')
def my_route():
    page = request.args.get('string', default="Don't Input", type=str)
    if page == "helloworld":
        return "Me Too!"
    else:
        return "helloworld"
if __name__ == '__main__':
    app.run(host='localhost',port=100,debug=True)