#셋 컴프리헨션을 이용하여 range(10) 에서 홀수 셋을 만들어라.
odd = {number for number in range(10) if number % 2 == 1}
print(odd)