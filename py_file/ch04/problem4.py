#리스트 컴프리헨션을 이용하여 range(10) 에서 짝수 리스트를 만들어라
even = [number for number in range(10) if number % 2 == 0]
print(even)