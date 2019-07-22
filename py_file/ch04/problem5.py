#딕셔너리 컴프리헨션을 이용하여 squares 딕셔너리를 생성하라. range(10) 의 반환값을 키로 하고, 각 키의 제곱을 값으로 한다.
squares = {key:key*key for key in range(10)}
print(squares)