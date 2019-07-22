from flask import Flask
from selenium import webdriver
from time import sleep

app = Flask(__name__)

def aaa():
    driver = webdriver.Chrome('C:\\Users\\ghkd0\\Desktop\\chromedriver.exe')    #크롬 드라이버 
    driver.get('http://www.weather.go.kr/weather/forecast/timeseries.jsp')      #가상청 광산구 동네예보
    sleep(1)    #1초 쉬어
    print(driver.find_element_by_xpath("//*[@id=\"dfs-panel\"]/div[2]/div[2]/dl/dd[1]").text)   #로그로 나타내고
    a = driver.find_element_by_xpath("//*[@id=\"dfs-panel\"]/div[2]/div[2]/dl/dd[1]").text      #a라는 변수에 온도 저장
    driver.quit()      #크롬드라이버 닫기
    return a  #a 리턴

an = aaa()  #함수 실행 후 an 변수 담기

@app.route('/') #127.0.0.1
def hello():    #서버를 실행할 때
    return an   #an값을 출력해라

if __name__ == '__main__': 
	app.run(host="127.0.0.1",port=3434)     #localhost주소의 3434포트를 열고 / 주소로 get 방식 접속을 하면 hello 함수를 실행해라.