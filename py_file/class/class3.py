#위에서 작성한 Quadrangle 클래스를 기반으로 직사각형 1개 객체와 정사각형 1개 객체를 만들되,
#너비(width), 높이(height), 색상(color)를 한번에 설정할 수 있는 메서드만들고, 다음 값으로 각 객체의 속성값을 변경한 후, 
#사각형 너비와 색상도 함께 출력하기
#직사각형2개 속성: width=10, height=5, color='red'
#정사각형2개 속성: width=7, height=7, color='blue'
class Quadrangle:
    width = 0
    height = 0
    color = "black"
 
    def get_area(self):
        return self.width * self.height
    z
    def set_area(self, data1, data2, data3):
        self.width = data1 
        self.height = data2
        self.color = data
 
square1 = Quadrangle()
square2 = Quadrangle()
 
square1.set_area(10, 5, 'red')
square2.set_area(7, 7, 'blue')
 
print(square1.get_area())
print(square2.get_area())
