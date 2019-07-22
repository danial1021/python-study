class Quadrangle:
    width = 0
    height = 0
    color = "black"
 
    #사각형 넓이 
    def get_area(self):
        return self.width * self.height
    
    #사각형 width, height 설정
    def set_area(self, data1, data2):
        self.width = data1 
        self.height = data2

square = Quadrangle()
square.set_area(5, 5)        
square.get_area()


# * width, height, color 속성을 가진 사각형 클래스를 만들고 다음 4개의 객체 만들기 (객체 속성을 바꾸고, 출력)
# - 직사각형 1개 객체 속성: width=10, height=5, color='red'
# - 정사각형 1개 객체 속성: width=7, height=7, color='blue'
class Dave:
    width = 0
    height = 0
    color = ''
 
square1 = Dave()
square2 = Dave()
 
square1.width = 10
square1.height = 5
square1.color = 'red'
 
square2.width = 7
square2.height = 7
square2.color= 'blue'
 
print (square1.width, square1.height, square1.color)
print (square2.width, square2.height, square2.color)

