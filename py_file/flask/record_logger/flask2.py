import time
from flask import Flask
from flask import request
import logging
from logging.handlers import RotatingFileHandler
 
app = Flask(__name__)
@app.route('/')
 
def my_route():
    app.logger.info(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+","+str(request.remote_addr))
    page = request.args.get('string', default = "Don't Input", type = str)
    if page == "코드레드":
        return "비상 상황을 감지하였습니다."
    else:
        return "처리 불가"
 
if __name__ == '__main__':
    logHandler = RotatingFileHandler('my_log.csv', maxBytes=1000, backupCount=1)
    logHandler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(logHandler)
 
    app.run()