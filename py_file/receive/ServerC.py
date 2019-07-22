from flask import Flask
import threading
import sys
import re
import time
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

app = Flask(__name__)

Entire={0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}

def SeleniumThread():
        driver = webdriver.Chrome("D:\\Coding\\Python\\Server\\chromedriver\\chromedriver.exe")

        driver.get('https://www.koreabaseball.com/Player/Search.aspx')

        baseballvalue=["HT","KT","LG","NC","SK","WO","OB","LT","SS","HH"]
        positionvalue=["1","2","3,4,5,6","7,8,9"]
        option_selected = "팀 선택"
    
        j=0

        while(j<10):
            select = driver.find_element_by_xpath("//option[@value='"+str(baseballvalue[j])+"']")
            select.click()

            soup = driver.page_source
            html = BeautifulSoup(soup,'html.parser')

            div1 = html.find("div",{"class":"sub-content"})

            div_selectForm = div1.find("div",{"class":"compare"})

            select = div_selectForm.find("select",{"id":"cphContents_cphContents_cphContents_ddlTeam"})

            tmpoption = select.find("option",{"selected":"selected"})
            tmpoption = tmpoption.get_text()
            while(True):
                if(tmpoption!=option_selected):
                    option_selected=tmpoption
                    break
                else:
                            
                    soup = driver.page_source
                    html = BeautifulSoup(soup,'html.parser')

                    div1 = html.find("div",{"class":"sub-content"})
                            
                    div_selectForm = div1.find("div",{"class":"compare"})

                    select = div_selectForm.find("select",{"id":"cphContents_cphContents_cphContents_ddlTeam"})

                    tmpoption = select.find("option",{"selected":"selected"})
                    tmpoption = tmpoption.get_text()

            divPag = html.find("div",{"class":"paging"})  
            btns = divPag.findAll("a")

            tbody = div1.find("tbody")
            trs = tbody.findAll("tr")
            Player = {'No': [], 'Name':[], 'Pos':[], 'Link':[]}
            i=1
            while (True):
                html = BeautifulSoup(driver.page_source, 'lxml')
                divPag = html.find("div",{"class":"paging"})  
                atmp = divPag.find("a",{"class":"on"})
                atmp = atmp.get_text()
                while(True):
                    if(int(i)==int(atmp)):
                        break
                    html = BeautifulSoup(driver.page_source, 'lxml')
                    divPag = html.find("div",{"class":"paging"}) 
                    atmp = divPag.find("a",{"class":"on"})
                    atmp = atmp.get_text()
                div1 = html.find("div",{"class":"sub-content"})
                tbody = div1.find("tbody")
                trs = tbody.findAll("tr")        
                for tr in trs:
                    tds = tr.findAll("td")
                    Player['No'].append(tds[0].get_text())
                    Player['Name'].append(tds[1].get_text())
                    Player['Pos'].append(tds[3].get_text())
                    a = tds[1].find("a")
                    Player['Link'].append("https://www.koreabaseball.com"+a.get('href'))
                if(i>=len(btns)-2):
                    break
                btn = driver.find_element_by_xpath("//a[@id='cphContents_cphContents_cphContents_ucPager_btnNo"+str(i+1)+"']")
                btn.click()
                i+=1
            Entire[j]=Player
            j+=1
        driver.quit()

SeleniumThread()

@app.route('/')
def hello():
    return json.dumps(Entire)

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000)
	
