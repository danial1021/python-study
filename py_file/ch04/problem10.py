#어떤 함수가 호출되면 'start'를, 끝나면 'end'를 출력하는 test 데커레이터를 정의하라.
def test(func):
    def new_func(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('end')
        return result
    return new_func


@test 
def greeting():
    print("Greetings,Earthling")   


greeting()