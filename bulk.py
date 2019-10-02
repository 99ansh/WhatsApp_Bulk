from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
from tkinter import *
import pandas as pd
import easygui

driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe")
url = "https://web.whatsapp.com/"
driver.get(url)
#print(driver.page_source)
#print(driver.current_url)
driver.implicitly_wait
search = driver.find_element_by_css_selector('#app > div > div > div.landing-window > div.landing-main > div > div._2d3Jz > div > img')
print(search.get_attribute("alt"))
time.sleep(3)
element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#side > div._2HS9r > div > label > input')))
time.sleep(5)

root = Tk()
root.title('WhatsApp Bulk Messages')
root.minsize(width=410,height=350)
root.geometry("+800+0")

L1 = Label(root, text="Recipients")
L1.place(x=5,y=10)
E1 = Text(root, bd =5,width=40,height=1)
E1.place(x=70,y=10)

def recipients():
    print("imported")
    path=easygui.fileopenbox(msg="Recipients",title="Choose",default="",filetypes="*.csv") #Opening Dialog Box for Selection
    data = pd.read_csv(path)
    contacts=data['recipients'].tolist()
    E1.insert('1.0',','.join(contacts))
    
def message():
    print("imported")
    
menu = Menu(root)
root.config(menu=menu)
first=Menu(menu)
menu.add_cascade(label="Import",menu=first)
first.add_command(label="Recipients",command=recipients)
first.add_command(label="Message",command=message)



L2 = Label(root, text="Message")
L2.place(x=5,y=40)
E2 = Text(root, bd =5,width=40,height=10)
E2.place(x=70,y=40)

L3 = Label(root, text="Info")
L3.place(x=5,y=250)
E3 = Text(root, bd =5,width=40,height=3)
E3.place(x=70,y=250)

def inp():
    
    inpu = E1.get('1.0','end-1c')
    l=inpu.split(',')
    message=E2.get('1.0','end-1c')
    ct=0
    for i in l:
        element.send_keys(i)
        element.send_keys(Keys.RETURN)
        try:
            time.sleep(2)
            if(driver.find_element_by_css_selector("#pane-side > div._13U-5._2dEsb > div > span").text=="No chats, contacts or messages found"):
                print(i+" not found")
                ct+=1
                driver.find_element_by_css_selector("#side > div._2HS9r > div > span > button").click()
                continue
        except NoSuchElementException:
            try:                
                message_element = driver.find_element_by_css_selector("#main > footer > div._2i7Ej.copyable-area > div._13mgZ > div > div._3u328.copyable-text.selectable-text")
                message_element.send_keys(message)
                message_element.send_keys(Keys.RETURN)
            except NoSuchElementException:
                driver.find_element_by_css_selector("#side > div._2HS9r > div > span > button").click()
    print(inpu)
    print(message)
    E3.insert('1.0',"Total Recipients -> "+ str(len(l)-ct)+"\n")
    E3.insert('2.0',"Message -> "+ str(message)+"\n")
    E3.insert('3.0',"----------------------------------------"+"\n")
    
sub_btn = Button(root, text="Send Bulk", command=inp)
sub_btn.place(x=200,y=220)

root.mainloop()

#pane-side > div._13U-5._2dEsb > div > span
