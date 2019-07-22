#제너레이터 컴프리헨션을 이용하여 문자열 'Got '과 range(10)의 각 숫자를 반환하라.
# for 문을 사용해서 제너레이터를 순회한다.
for thing in ('Got %s' % number for number in range(10)):
    print(thing) 