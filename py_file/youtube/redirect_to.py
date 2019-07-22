from flask import Flask

app = Flask(__name__)
# redirect_to 옵션에 다른 url이 아닌 함수를 전달할 수 있음
# 미리 함수를 정의 해야하고 
# 정의된 함수의 첫번째 인자는 adapter라는 인자를 사용(필수)
@app.route('/aaa',redirect_to='/new_aaa')
def aaa():
    return "/aaa로 호출한 페이지 입니다"

@app.route('/new_aaa')
def new_aaa():
    return '/new_aaa로 호출한 페이지 입니다'


if __name__ == '__main__':
    app.run()