from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


import time

print("ASU SEATS")
driver = webdriver.Chrome()
driver.get("https://catalog.apps.asu.edu/catalog/classes/classlist?advanced=true&campusOrOnlineSelection=C&honors=F&level=grad&promod=F&searchType=open&subject=CSE&term=2237")
time.sleep(2)
source = driver.page_source
soup = bs(source, "lxml")

course_names = []
cn1 = []
cn2 = []
available_open_seats=[]




for td in soup.findAll("td", { "class":"titleColumnValue" }):
        cn1 = (str(td)).split('i>')
        cn2 = (str(cn1[2])).split('<span')
        ress = cn2[0].replace(' ', '').replace('\n', '').replace('\t', '').replace('<!--', '')
        if ress=='':
            ress="Course 598"
        course_names.append(ress)

ras_button = driver.find_elements(by=By.XPATH, value="//*[contains(@class, 'bold-hyperlink')]")

for x in range(len(ras_button)):
        
        try:
            
            txt=ras_button[x].text
            if(txt.startswith("CSE 5") and (not txt.startswith("CSE 59")) and (not txt.startswith("CSE 58"))):
                    print(txt)
                    print(ras_button[x+1].text)
                    ras_button[x].click()
                    #print("clicked?")
                    time.sleep(2)
                    x1 = driver.find_elements(by=By.XPATH, value="//*[contains(@class, 'table table-sm reserved-seats')]")
                    #print("stuff=",x1[-1].text[-15:])
                    rass = ((x1[-1].text).split(' ')[-1])
                    available_open_seats.append(rass)
                    print ("Seats = ", rass)
                    intrass = int(rass)
                    #if(intrass>0 and intrass<20):
                        #send email notification : ToDo
        except:
            available_open_seats.append("0")






