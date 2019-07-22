#range(10) 의 홀수를 반환하는 get_odds 제너레이터 함수를 정의하라.
#for 문으로 반환된 세 번째 홀수를 찾아서 출력하라.
def get_odds():
    for number in range(1,10,2):
        yield number


for count, number in enumerate(get_odds(),1):
    if count == 3:
        print("The third odd number is",number)
        break        