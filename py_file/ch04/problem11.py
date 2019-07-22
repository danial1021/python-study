#OopsException이라는 예외를 정의하라. 이 예외를 발생시켜서 무슨 일이 일어나는지 살펴보라.
#이 예외를 잡아서 'Caught an oops'를 출력하는 코드를 작성하라.
class OopsException(Exception):
    pass

try:
    raise OopsException
except OopsException:
    print('Caught an oops')