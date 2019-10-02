# sudo apt-get install python3-pyqt4 (for mac and linux)
import urllib.request as url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from PyQt4 import QtGui as qt
from PyQt4 import QtCore as qtc

class Window(qt.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Main")
        # self.setWindowIcon(qt.QIcon("name.png"))
        
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
    
        self.setGeometry(400,100,600,500)        
        self.show()
        
    def buttonClicked(self):

        toBePrinted = "Total Recepients =   "
        names = self.text_name.text().split(",")
        toBePrinted += "%d \n\n"%(len(names))
        toBePrinted += "Recepients : \n"
        for i in range(len(names)):
            toBePrinted += "%d. %s,  "%(i+1,names[i])
        toBePrinted += "\n\nMessage : \n"
        message = self.text_msg.toPlainText()
        toBePrinted += message

        driver = webdriver.Chrome('/home/shyam/chromedriver')
        driver.get('https://web.whatsapp.com')
        time.sleep(10)
        # ------------ Message details ---------------------

        # person = input("Enter the Recipient's name: ").strip().split(",")
        # message = input("Enter the message: ").strip()
        # number_of_messages = int(input("n = ").strip())
        # message = "Hey guys, let's solve this fun challenge to brush up your mathematical skills.\nAsk doubts if any! Happy Coding! 😀"

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

        self.text_status.setText(toBePrinted)

        
app = qt.QApplication(sys.argv)
GUI = Window()
app.exec_()
sys.exit()

# app.exec_() # this has to be added in mac and linux