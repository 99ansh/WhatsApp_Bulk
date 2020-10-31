# sudo apt-get install python3-pyqt4 (for mac and linux)
import requests # line 2 and 3 were added to remove the queue error
from multiprocessing import Queue
import urllib.request as url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import sys
from PyQt4 import QtGui as qt
from PyQt4 import QtCore as qtc

class Window(qt.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("WhatsBulk")
        self.setStyleSheet("background-color:white;")
        self.setWindowIcon(qt.QIcon("logo.ico"))
        
        # recipient's name section
        self.lbl_name = qt.QLabel("Recipient's Name: ", self)
        self.lbl_name.setGeometry(qtc.QRect(100,20,150,20))  

        self.text_name = qt.QLineEdit(self)
        self.text_name.move(230,20)
        self.text_name.setGeometry(qtc.QRect(230,16,300,25))
        
        # message section
        self.lbl_msg = qt.QLabel("Message: ", self)
        self.lbl_msg.setGeometry(qtc.QRect(100,50,150,50))
        
        self.text_msg = qt.QTextEdit(self)
        self.text_msg.move(230,46)
        self.text_msg.setGeometry(qtc.QRect(230,46,300,80))        

        # send message button

        btn = qt.QPushButton("Send It",self)
        btn.clicked.connect(self.buttonClicked)
        btn.move(250,150)


        # status block 

        self.lbl_status = qt.QLabel("Status: ", self)
        self.lbl_status.setGeometry(qtc.QRect(80,170,120,170))

        self.text_status = qt.QTextEdit(self)
        self.text_status.setReadOnly(True)
        self.text_status.setGeometry(qtc.QRect(140,240,300,250))
    
        self.setGeometry(700,120,600,500)        
        self.show()
        
    def buttonClicked(self):

        toBePrinted = "Total Recepients =   "
        names = self.text_name.text().strip().split(",")
        toBePrinted += "%d \n\n"%(len(names))
        toBePrinted += "Recepients : \n"
        for i in range(len(names)):
            toBePrinted += "%d. %s,  "%(i+1,names[i])
        toBePrinted += "\n\nMessage : \n"
        message = self.text_msg.toPlainText()
        toBePrinted += message

        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
            driver = webdriver.Chrome(executable_path="chromedriver.exe",options=chrome_options)
            driver.implicitly_wait
            driver.set_window_position(0, 0)
            driver.set_window_size(564, 768)
            driver.get('https://web.whatsapp.com')
        except:
            toBePrinted = "Your Chrome version is not supported"
            driver.close()
            # ------------ Message details ---------------------

            # person = input("Enter the Recipient's name: ").strip().split(",")
            # message = input("Enter the message: ").strip()
            # number_of_messages = int(input("n = ").strip())
            # message = "Hey guys, let's solve this fun challenge to brush up your mathematical skills.\nAsk doubts if any! Happy Coding! 😀"
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._2zCfw')))
        except TimeoutException as e:
            toBePrinted = str(e)
            driver.close()
        try:
            for i in names:
                searchEle = driver.find_element_by_css_selector("._2zCfw")
                searchEle.clear()
                searchEle.send_keys(i)
                searchEle.send_keys(Keys.RETURN)

                meassageEle = driver.find_element_by_css_selector("._3u328")
                meassageEle.clear()
                meassageEle.send_keys(message)
                # meassageEle.send_keys((message+"\n")*number_of_messages)
                meassageEle.send_keys(Keys.RETURN)
                time.sleep(1)
            driver.close()
        except NoSuchElementException as e:
            toBePrinted = str(e)
            driver.close()    
        self.text_status.setText(toBePrinted)

app = qt.QApplication(sys.argv)
GUI = Window()
app.exec_()
sys.exit()

# app.exec_() # this has to be added in mac and linux
