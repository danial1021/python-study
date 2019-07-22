#위에서 작성한 Quadrangle 클래스를 기반으로 직사각형 1개 객체와 정사각형 1개 객체를 만들고, 각 사각형 너비 출력하기
#직사각형2개 속성: width=10, height=5, color='red'
#정사각형2개 속성: width=7, height=7, color='blue'
class Quadrangle:
    width = 0
    height = 0
    color = "black"
 
    def get_area(self):
        return self.width * self.height
    
    def set_area(self, data1, data2):
        self.width = data1 
        self.height = data2
 
square1 = Quadrangle()
square2 = Quadrangle()
 
square1.set_area(10, 5)
square2.set_area(7, 7)
square1.color = 'red'
square1.color = 'blue'
 
print(square1.get_area())
print(square2.get_area())