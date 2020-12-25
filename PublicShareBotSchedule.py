#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import holidays
from datetime import date
import calendar
from datetime import datetime   
import pause           
from selenium.webdriver.chrome.options import Options
import pyautogui


#Setup
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://accounts.google.com/Login?hl=en")

#Times and dates
wedone="7:30-8:10 a.m. : "
wedtwo="8:15-9:05 a.m. : "
wedthree="9:05-9:15 a.m. : "
wedfour="9:15- 9:55 a.m. : "
wedfive="10:00-10:40 a.m. : "
wedsix="10:45-11:25 a.m. : "
wedseven="11:30-12:10 p.m. : " 
wedeight="12:10-12:35 p.m. : "
wednine="12:35-1:55 p.m. : "

one="7:30-8:20 a.m. : "
two="8:25-9:15 a.m. : "
three="9:15-9:30 a.m. : "
four="9:30- 10:20 a.m. : "
five="10:25-11:15 a.m. : "
six="11:15-12:10 p.m. : "
seven="12:10-1:00 p.m. : "  
eight="1:05-1:55 p.m. : "

Holidays = [
"2020-11-25","2020-11-26","2020-11-27",
"2020-12-24","2020-12-25","2020-12-26","2020-12-27","2020-12-28","2020-12-29","2020-12-30","2020-12-31","2021-01-01"
,"2021-01-18","2021-01-19",
"2021-02-12","2021-02-15","2021-02-16","2021-02-17","2021-02-18","2021-02-19"
,"2021-04-02","2021-04-19","2021-04-20","2021-04-21","2021-04-22","2021-04-23"
"2021-05-31"]

HalfDays = ["2021-01-13","2021-03-03","2021-03-31","2021-05-05"]
#Functions
def signIn():
        ActionChains(driver).send_keys("Username").send_keys(Keys.ENTER).perform()
        pause.seconds(10)
        ActionChains(driver).send_keys("Password").send_keys(Keys.ENTER).perform()
        pause.seconds(10)
        driver.get("Link to a document")
        pause.seconds(2)
def finish():
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
        ActionChains(driver).key_down(Keys.SHIFT).send_keys("e").perform()
        pause.seconds(3)
        ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.CONTROL).perform()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
        ActionChains(driver).move_to_element(size).click(size).perform()
        ActionChains(driver).key_up(Keys.CONTROL).perform()
        ActionChains(driver).send_keys("11").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).move_to_element(top).click(top).perform()
def clear():
        lastTable = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[10]/td[1]/div[1]/div[1]/div[1]")
        dots = driver.find_element_by_xpath("//div[@id='moreButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        fill = driver.find_element_by_xpath("//div[@id='cellColorMenuButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        top = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]")
        ActionChains(driver).move_to_element(lastTable).click(lastTable).perform()
        time.sleep(10)
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()        
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='white']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        time.sleep(2)
        ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
        for i in range(10):
                ActionChains(driver).move_to_element(dots).click(dots).perform()        
                ActionChains(driver).move_to_element(fill).click(fill).perform()
                Color = driver.find_element_by_xpath("//div[@title='white']")
                ActionChains(driver).move_to_element(Color).click(Color).perform()
                ActionChains(driver).move_to_element(dots).click(dots).perform()
                ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
                ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
        ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
        ActionChains(driver).send_keys(Keys.BACKSPACE).perform()        
def message():
        lastTable = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[10]/td[1]/div[1]/div[1]/div[1]")
        dots = driver.find_element_by_xpath("//div[@id='moreButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        fill = driver.find_element_by_xpath("//div[@id='cellColorMenuButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        top = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]")
        ActionChains(driver).move_to_element(dots).click(dots).perform()        
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='red']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys("This Schedule is automated, and coded to a standard schedule. Some items might be incorrect. For more information, please contact 9001181@franklinps.net. Thanks-The Bot").perform()            

def geo(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        geoColor = driver.find_element_by_xpath("//td[@id='docs-material-colorpalette-cell-313']/div[1]")
        ActionChains(driver).move_to_element(geoColor).click(geoColor).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" A period Geography: A link goes here").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()      
def orchestra(period):        
        ActionChains(driver).move_to_element(dots).click(dots).perform()        
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='white']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" Orchestra: Subscribe").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys("Form: A link").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys("OR").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(period+" Flex: Subscribe").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def screenbreak(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        scrColor = driver.find_element_by_xpath("//div[@class='docs-material-colorpalette-colorswatch']")
        ActionChains(driver).move_to_element(scrColor).click(scrColor).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" Screen Break").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def math(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        matColor = driver.find_element_by_xpath("//div[@title='light yellow 1']")
        ActionChains(driver).move_to_element(matColor).click(matColor).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" E period Math 1: Subscirbe").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys("E period Math 2: Link").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def pe(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='light magenta 1']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" PE: Subscribe").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def lunch(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@class='docs-material-colorpalette-colorswatch']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" Lunch Period: Rick Roll link goes here").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def sci(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        sciColor  = driver.find_element_by_xpath("//td[@id='docs-material-colorpalette-cell-326']/div[1]")
        ActionChains(driver).move_to_element(sciColor).click(sciColor).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" F period Science: Subscribe").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def ela(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='light orange 1']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" B period ELA: Link here").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def ExtraClass(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='light cornflower blue 1']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" Computers: Subscribe").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def flex(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()        
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='white']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" Flex: Link here").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def asynch(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()        
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='white']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" Asynchronous learning time: Link to a form goes here").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()        
def teamtime(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='cyan']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" Team Time: Subscribe").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
def spanish(period):
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='light magenta 1']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).send_keys(period+" Spanish: Subsribe").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()


#This part is very specific to my needs, and wont be useful to most. Because of this i commented it out
'''def landing():
        while True:
                now = datetime.now()
                current_hour = now.strftime("%H")
                current_minute = now.strftime("%M")
                timesumstr = (current_hour)+(current_minute)
                timesum = int(timesumstr) 
                if 0<=timesum<=2322:
                        pyautogui.hotkey('win','shift','1')
                        time.sleep(1)
                        pyautogui.write("A link\n",interval=0.01)
                        time.sleep(15)
                        pyautogui.press('enter')
                        time.sleep(1)
                        pyautogui.click(x=403, y=830, clicks=1, interval=0, button='right')
                        for i in range(9):
                                pyautogui.press('down')
                        pyautogui.press('enter')
                        time.sleep(1)
                        for i in range(2):
                                pyautogui.press('up')
                        time.sleep(1)   
                        pyautogui.hotkey('ctrl','c')
                        time.sleep(1)
                        pyautogui.hotkey('ctrl','shift','i')            
                        time.sleep(1)
                        pyautogui.hotkey('ctrl','l')
                        time.sleep(1)
                        pyautogui.write("https://html-online.com/editor/\n")
                        time.sleep(15)
                        time.sleep(5)
                        for i in range(2):
                                pyautogui.press('tab')
                                time.sleep(1)
                        
                        pyautogui.hotkey('ctrl','a')
                        time.sleep(1)
                        pyautogui.press('backspace')
                        time.sleep(1)
                        time.sleep(1)
                        pyautogui.hotkey('ctrl','v')
                        time.sleep(5)
                        pyautogui.click(x=403, y=870, clicks=1, interval=0, button='left')
                        time.sleep(1)
                        pyautogui.hotkey('ctrl','a')
                        time.sleep(1)   
                        pyautogui.hotkey('ctrl','c')
                        time.sleep(1)
                        
                        pyautogui.hotkey('ctrl','w')
                break         
        else:
                pause.seconds(30)      

def LandingExecute():
        landing()
        pause.seconds(4)
        lastTable = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[10]/td[1]/div[1]/div[1]/div[1]")      
        ActionChains(driver).move_to_element(lastTable).click(lastTable).perform()
        pause.seconds(3)
        pause.seconds(6)
        for i in range(9):
                ActionChains(driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).perform()
                pause.seconds(2)
        pause.seconds(3)
        ActionChains(driver).send_keys("Announcements for today(According to the Landing page):").perform()
        ActionChains(driver).send_keys(Keys.RETURN).perform()
        pause.seconds(3)
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() 
        pause.seconds(5)
        top = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]")
        finish() '''

def orchestraBot():
        while True:
                now = datetime.now()
                current_hour = now.strftime("%H")
                current_minute = now.strftime("%M")
                timesumstr = (current_hour)+(current_minute)
                timesum = int(timesumstr) 
                if 819<=timesum<=825:
                        driver.get("https://hangouts.google.com/")
                        for i in range(11):
                                ActionChains(driver).send_keys(Keys.TAB)
                        ActionChains(driver).send_keys(Keys.RETURN)
                        pause.seconds(10)
                        ActionChains(driver).send_keys("Chat name")
                        pause.seconds(5)
                        ActionChains(driver).send_keys(Keys.RETURN)
                        pause.seconds(10)
                        ActionChains(driver).send_keys("REMINDER Please fill out the orchestra form: Form link").perform()
                        pause.seconds(10)
                        ActionChains(driver).send_keys(Keys.RETURN).perform()
                        pause.minutes(10)
                        ActionChains(driver).send_keys("2nd REMINDER Please fill out the orchestra form: Form link").perform() 
                        ActionChains(driver).send_keys(Keys.RETURN).perform()
                        break
                else:
                        pause.seconds(30)

        driver.get("Link to schedule")

def Days(dayCounter):
        lastTable = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[10]/td[1]/div[1]/div[1]/div[1]")
        dots = driver.find_element_by_xpath("//div[@id='moreButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        fill = driver.find_element_by_xpath("//div[@id='cellColorMenuButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        top = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]")
        clear()
        ActionChains(driver).send_keys("Day "+str(dayCounter)).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()
                
        if dayCounter == 1:
                geo(one)
                orchestra(two)
                screenbreak(three)
                ela(four)
                ExtraClass(five)
                lunch(six)
                pe(seven)
                math(eight)
        if dayCounter == 8:
                geo(one)
                flex(two)
                screenbreak(three)
                ela(four)
                ExtraClass(five)
                lunch(six)
                spanish(seven)
                math(eight)
        if dayCounter == 2:
                sci(one)
                flex(two)
                screenbreak(three)
                geo(four)
                ela(five)
                lunch(six)
                ExtraClass(seven)
                spanish(eight)
        if dayCounter == 9:
                sci(one)
                orchestra(two)
                screenbreak(three)
                geo(four)
                ela(five)
                lunch(six)
                ExtraClass(seven)
                pe(eight)    
        if dayCounter == 3:
                math(one)
                orchestra(two)
                screenbreak(three)
                sci(four)
                geo(five)
                lunch(six)
                ela(seven)
                ExtraClass(eight)
        if dayCounter == 10:
                math(one)
                flex(two)
                screenbreak(three)
                sci(four)
                geo(five)
                lunch(six)
                ela(seven)
                ExtraClass(eight)
        if dayCounter == 4:
                pe(one)
                flex(two)
                screenbreak(three)
                math(four)
                sci(five)
                lunch(six)
                ela(seven)
                geo(eight)
        if dayCounter == 11:
                spanish(one)
                orchestra(two)
                screenbreak(three)
                math(four)
                sci(five)
                lunch(six)
                ela(seven)
                geo(eight)
        if dayCounter == 5: 
                math(one)
                orchestra(two)
                screenbreak(three)
                ExtraClass(four)
                spanish(five)
                lunch(six)
                sci(seven)
                ela(eight)
        if dayCounter == 12:
                math(one)
                flex(two)
                screenbreak(three)
                ExtraClass(four)
                pe(five)
                lunch(six)
                sci(seven)
                ela(eight)
        if dayCounter == 6:
                sci(one)
                flex(two)
                screenbreak(three)
                math(four)
                ExtraClass(five)
                lunch(six)
                geo(seven)
                teamtime(eight)
        if dayCounter == 13:
                sci(one)
                orchestra(two)
                screenbreak(three)
                math(four)
                ExtraClass(five)
                lunch(six)
                geo(seven)
                teamtime(eight)
        if dayCounter == 7:
                geo(one)
                orchestra(two) 
                screenbreak(three)
                math(four)
                pe(five)
                lunch(six)
                sci(seven)
                ela(eight)
        if dayCounter == 14:
                geo(one)
                flex(two)
                screenbreak(three)
                math(four)
                spanish(five)
                lunch(six)
                sci(seven)
                ela(eight)        
        message()
        ActionChains(driver).send_keys(Keys.TAB).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        ActionChains(driver).move_to_element(fill).click(fill).perform()
        Color = driver.find_element_by_xpath("//div[@title='white']")
        ActionChains(driver).move_to_element(Color).click(Color).perform()
        ActionChains(driver).move_to_element(dots).click(dots).perform()
        finish()      
         

def Wednesdays(dayCounter):
        clear()
        ActionChains(driver).send_keys("Wednesday Day "+str(dayCounter)).perform()
        ActionChains(driver).send_keys(Keys.TAB).perform()              
        if dayCounter==1:
                geo(wedone)
                orchestra(wedtwo)
                screenbreak(wedthree)
                ela(wedfour)
                ExtraClass(wedfive)
                pe(wedsix)
                math(wedseven)
                lunch(wedeight)
                asynch(wednine)
        if dayCounter==7:
                geo(wedone)
                flex(wedtwo)
                screenbreak(wedthree)
                ela(wedfour)
                ExtraClass(wedfive)
                spanish(wedsix)
                math(wedseven)
                lunch(wedeight)
                asynch(wednine)
        if dayCounter==2:
                sci(wedone)
                flex(wedtwo)
                screenbreak(wedthree)
                geo(wedfour)
                ela(wedfive)
                ExtraClass(wedsix)
                spanish(wedseven)
                lunch(wedeight)
                asynch(wednine)
        if dayCounter==9: 
                sci(wedone)
                orchestra(wedtwo)
                screenbreak(wedthree)
                geo(wedfour)
                ela(wedfive)
                ExtraClass(wedsix)
                pe(wedseven)
                lunch(wedeight)
                asynch(wednine)
        if dayCounter==3:
                math(wedone)
                orchestra(wedtwo)
                screenbreak(wedthree)
                sci(wedfour)
                geo(wedfive)
                ela(wedsix)
                ExtraClass(wedseven)
                lunch(wedeight)
                asynch(wednine)
        if dayCounter==10:
                math(wedone)
                flex(wedtwo)
                screenbreak(wedthree)
                sci(wedfour)
                geo(wedfive)
                ela(wedsix)
                ExtraClass(wedseven)
                lunch(wedeight)
                asynch(wednine)  
        if dayCounter==4:
                pe(wedone)
                flex(wedtwo)
                screenbreak(wedthree)
                math(wedfour)
                sci(wedfive)
                ela(wedsix)
                geo(wedseven)
                lunch(wedeight)
                asynch(wednine)  
        if dayCounter==11:  
                spanish(wedone)
                orchestra(wedtwo)
                screenbreak(wedthree)
                math(wedfour)
                sci(wedfive)
                ela(wedsix)
                geo(wedseven)
                lunch(wedeight)
                asynch(wednine)   
        if dayCounter==5:
                math(wedone)
                orchestra(wedtwo)
                screenbreak(wedthree)
                ExtraClass(wedfour)
                spanish(wedfive)
                sci(wedsix)
                ela(wedseven)
                lunch(wedeight)
                asynch(wednine)
        if dayCounter==12:
                math(wedone)
                flex(wedtwo)
                screenbreak(wedthree)
                ExtraClass(wedfour)
                pe(wedfive)
                sci(wedsix)
                ela(wedseven)
                lunch(wedeight)
                asynch(wednine)                  
        if dayCounter==6:
                sci(wedone)
                flex(wedtwo)
                screenbreak(wedthree)
                math(wedfour)
                ExtraClass(wedfive)
                geo(wedsix)
                teamtime(wedseven)
                lunch(wedeight)
                asynch(wednine)  
        if dayCounter==13: 
                sci(wedone)
                orchestra(wedtwo)
                screenbreak(wedthree)
                math(wedfour)
                ExtraClass(wedfive)
                geo(wedsix)
                teamtime(wedseven)
                lunch(wedeight)
                asynch(wednine)  
        if dayCounter==7:
                geo(wedone)
                orchestra(wedtwo)
                screenbreak(wedthree)
                math(wedfour)
                pe(wedfive)
                sci(wedsix)
                ela(wedseven)
                lunch(wedeight)
                asynch(wednine)
        if dayCounter==14:
                geo(wedone)
                flex(wedtwo)
                screenbreak(wedthree)
                math(wedfour)
                spanish(wedfive)
                sci(wedsix)
                ela(wedseven)
                lunch(wedeight)
                asynch(wednine) 
        message()
        finish()      


def exceptions():
        lastTable = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[10]/td[1]/div[1]/div[1]/div[1]")
        dots = driver.find_element_by_xpath("//div[@id='moreButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        fill = driver.find_element_by_xpath("//div[@id='cellColorMenuButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        top = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]")
        if my_date in Holidays:
                clear()
                ActionChains(driver).send_keys("Previous Day: "+str(dayCounter)).perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).send_keys("Hello. Today is a holiday, and is most likely not a school day. If this information is incorrect please use the backup schedule attached below. The previous day was Day "+str(dayCounter)).perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).send_keys("A backup link here").perform()
                ActionChains(driver).send_keys(Keys.RETURN).perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).send_keys("Have a nice day").perform()
                ActionChains(driver).send_keys(Keys.TAB)
        if WeekDay == "Saturday" or WeekDay == "Sunday":
                clear()
                ActionChains(driver).send_keys("Previous Day: "+str(dayCounter)).perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).send_keys("Hello. Today is a weekend, and is most likely not a school day. If this information is incorrect please use the backup schedule attached below. The previous day was Day "+str(dayCounter)).perform()
                ActionChains(driver).send_keys(Keys.RETURN).perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).move_to_element(doc).click(doc).send_keys("A backup schedule link").perform()
                ActionChains(driver).send_keys(Keys.RETURN).perform()
                ActionChains(driver).send_keys(Keys.RETURN).perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).send_keys("Have a nice day").perform()
                ActionChains(driver).send_keys(Keys.RETURN)
                ActionChains(driver).send_keys(Keys.TAB)
        if my_date in HalfDays:
                clear()
                ActionChains(driver).send_keys("It's a Half Day!").perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).send_keys("Hi It's a halfday. This happens like 3 times so I didn't code it into the bot. Instead, check the homeroom google classroom: ").perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).send_keys("HR LINK").perform()
                ActionChains(driver).send_keys(Keys.RETURN).perform()
                ActionChains(driver).send_keys(Keys.TAB).perform()
                ActionChains(driver).send_keys("Have a nice day").perform()
                ActionChains(driver).send_keys(Keys.TAB)     


#Start
pause.seconds(5)
signIn()

dayCounter = 9

doc = driver.find_element_by_xpath("//body")
lastTable = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[10]/td[1]/div[1]/div[1]/div[1]")
dots = driver.find_element_by_xpath("//div[@id='moreButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
fill = driver.find_element_by_xpath("//div[@id='cellColorMenuButton']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
top = driver.find_element_by_xpath("//div[@id='kix-appview']/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]")
size = driver.find_element_by_xpath("(//input[@class='goog-toolbar-combo-button-input jfk-textinput'])[2]")
driver.set_window_size(1920, 1080)
driver.maximize_window()

while True:       
        now = datetime.now()
        current_hour = now.strftime("%H")
        current_minute = now.strftime("%M")
        timesumstr = (current_hour)+(current_minute)
        timesum = int(timesumstr)     
        if 0<=timesum<=2439:
                
                my_date1 = date.today()
                my_date = str(my_date1)
                WeekDay = calendar.day_name[my_date1.weekday()]
                WeekDay = str(WeekDay)


                if my_date in Holidays or WeekDay == "Saturday" or WeekDay == "Sunday" or my_date in HalfDays:
                        exceptions()
                        ActionChains(driver).send_keys(Keys.TAB).perform()
                        ActionChains(driver).send_keys(Keys.RETURN)
                        message()
                        finish()
                        pause.minutes(20)
                        pause.minutes(20)     

                if (dayCounter<=14 and WeekDay != "Saturday" and WeekDay != "Wednesday" and WeekDay != "Sunday" and my_date not in Holidays and my_date not in HalfDays):
                        dayCounter += 1
                        if dayCounter==15:
                                dayCounter=1                  
                        driver.implicitly_wait(10)      
                        Days(dayCounter)   
                        if dayCounter%2!=0:
                                
                                orchestraBot()
                        pause.minutes(20)       
                

                if(dayCounter<=14 and WeekDay == "Wednesday" and my_date not in Holidays and my_date not in HalfDays):
                        dayCounter += 1
                        if dayCounter==15:
                                dayCounter=1
                        driver.implicitly_wait(10)      
                        Wednesdays(dayCounter)
                        pause.minutes(20)                
        else:
                pause.seconds(30)
#%windir%\System32\tscon.exe 2 /dest:console