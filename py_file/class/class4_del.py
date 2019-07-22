#attribute: 정삼각형 한 변의 길이, 삼각형 이름
#method: 정삼각형 이름 리턴
#생성자에서 attribute 값 설정
#소멸자작성 후, 객체 소멸시 object is deleted 출력

import math
 
class Figure:
    def __init__(self, length, name):
        self.length = length
        self.name = name
 
    def get_area(self):
        return (math.sqrt(3) / 2) * self.length**2  # (math.sqrt(3) / 2) * math.pow(self.length, 2)도 가능 
 
    def get_name(self):
        return self.name
    
    def __del__(self):
        print ('object is deleted')
        
square = Figure(10, 'dave')
print (square.get_area(), square.get_name())

