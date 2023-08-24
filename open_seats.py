from bs4 import BeautifulSoup as bs
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
time.sleep(2) #waiting for page to open
source = driver.page_source
soup = bs(source, "lxml")


course_names = []
cn1 = []
cn2 = []
available_open_seats=[]

for td in soup.findAll("td", { "class":"titleColumnValue" }):
        #html parsing magic - you'll understand it if you look at the HTML source code on the website :)
        cn1 = (str(td)).split('i>')
        cn2 = (str(cn1[2])).split('<span')
        ress = cn2[0].replace(' ', '').replace('\n', '').replace('\t', '').replace('<!--', '')
        # for some reason CSE 598 shows up empty
        if ress=='':
            ress="Course 598"
        course_names.append(ress)


ras_button = driver.find_elements(by=By.XPATH, value="//*[contains(@class, 'bold-hyperlink')]")

for x in range(len(ras_button)):
        
        try:
            course_number=ras_button[x].text
            if(course_number.startswith("CSE 5") and (not course_number.startswith("CSE 59")) and (not course_number.startswith("CSE 58"))):
                    print(course_number) #print course number
                    print(ras_button[x+1].text) #print course name
                    ras_button[x].click()
                    #wait for details to load
                    time.sleep(2)
                    x1 = driver.find_elements(by=By.XPATH, value="//*[contains(@class, 'table table-sm reserved-seats')]")
                    #parsing the element x1
                    #non reserved available seats
                    available_seats_nr = ((x1[-1].text).split(' ')[-1])
                    available_open_seats.append(int(available_seats_nr))
                    print ("Seats = ", available_seats_nr)
                    #if(available_seats_nr>0 and available_seats_nr<20):
                        #send email notification : ToDo
        except:
            available_open_seats.append(0)






