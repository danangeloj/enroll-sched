import sys
import os
import Scheduler 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QComboBox, QDesktopWidget, QLabel, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtWidgets, QtGui

class Menu(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.title = 'MENU'
        self.width = 300
        self.height = 400
        self.initUI()
    
    def center(self):
        window = self.frameGeometry()
        x = QDesktopWidget().availableGeometry().center()
        window.moveCenter(x)
        self.move(window.topLeft())

    def initUI(self):
        self.setWindowTitle(self.title)
        self.resize(self.width,self.height)
        self.setWindowIcon(QIcon('pythonico')) 
        self.center()
        self.setFixedSize(self.width, self.height)
        self.label = QLabel('DRAG & DROP',self)
        self.label.move(60,30)
        self.label2 = QLabel('SCHEDULE',self)
        self.label2.move(133,30)
        self.label3 = QLabel('DESIGNER',self)
        self.label3.move(188,30)
        
        self.rbutton=QPushButton('Register',self)
        self.rbutton.resize(70,30)
        self.rbutton.move((self.width/2)-(70/2),(self.height/2)-50)
        self.rbutton.clicked.connect(self.registerbutton)
        
        self.lbutton=QPushButton('Login',self)
        self.lbutton.resize(70,30)
        self.lbutton.move((self.width/2)-(70/2),(self.height/2))
        self.lbutton.clicked.connect(self.loginbutton)
        
        self.exitbutton=QPushButton('Exit',self)
        self.exitbutton.resize(70,30)
        self.exitbutton.move((self.width/2)-(70/2),(self.height/2)+100)
        self.exitbutton.clicked.connect(self.exits)
        
        self.show()
        
    def registerbutton(self):
        self.close()
        self.switch = Registration()
    
    def loginbutton(self):
        self.close()
        self.switch = Login()
    
    def exits(self):
        exitbuttonReply = QMessageBox.question(self," ","Are you sure you want to Exit the program?",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if exitbuttonReply == QMessageBox.Yes:
            sys.exit()
            exit()
        else:
            pass
        
class Registration(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Registration"
        self.width = 450
        self.height = 550
        self.noinput = []
        self.labels = ["Firstname:","Lastname:","Middle Name:",
                       "Password:","Birthday:","Program:"]
        self.birthday = [QComboBox(self),QComboBox(self),QComboBox(self)]
        self.program = QComboBox(self)
        self.textboxes = [QLineEdit(self),QLineEdit(self),QLineEdit(self),
                         QLineEdit(self)]
        self.main()
        
    def center(self):
        window = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        window.moveCenter(center)
        self.move(window.topLeft())
        
    def main(self):
        
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("pass"))
        self.resize(self.width,self.height)
        self.center()
        self.setFixedSize(self.width, self.height)
        y1=0
        
        for elem in self.labels:
            self.label = QLabel(elem,self)
            self.label.move(50,50+y1)
            
            y1+=40
        
        y2=0
        
        self.textboxes[3].setEchoMode(QLineEdit.Password)
        for elem in self.textboxes:
            #self.userinput=QLineEdit(self)
            elem.move(140,50+y2)
            elem.resize(250,20)
            y2+=40
        
        self.birthday[0].addItem("Year")
        for i in range (1950,2021):
            self.birthday[0].addItem(f"{i}")
        
        self.birthday[1].resize(100,20)
        self.birthday[1].addItem("Month")
        self.birthday[0].activated.connect(self.monthupdate)
        
        self.birthday[2].addItem("Day")
        self.birthday[1].activated.connect(self.dayupdate)
        
        x1 = 140
        for elem in self.birthday:
            elem.resize(80,20)
            elem.move(x1,210)
            x1+=85
        
        program = ["","Architecture","Civil Engineering","Computer Engineering",
                   "Electrical Engineering","Electronics Engineerin",
                   "Environmental & Sanitary Engineering","Industrial Engineering",
                   "Information & Technology","Mechanical Engineering"]
        self.program.move(140,250)
        self.program.resize(250,20)
        for elem in program:
            self.program.addItem(elem)
        
        self.submitbutton = QPushButton("Submit",self)
        self.submitbutton.move(310,400)
        self.submitbutton.resize(70,25)
        self.submitbutton.clicked.connect(self.submit)
        
        self.clearbutton = QPushButton("Clear",self)
        self.clearbutton.move(225,400)
        self.clearbutton.resize(70,25)
        self.clearbutton.clicked.connect(self.clear)
        
        self.backbutton = QPushButton("Back",self)
        self.backbutton.move(140,400)
        self.backbutton.resize(70,25)
        self.backbutton.clicked.connect(self.back)
        
        self.show()
    
    def monthupdate(self):
        self.birthday[1].clear()
        months = ["Month","January","February","March","April","May",
                  "June","July","August","September","October",
                  "November","December"]
        for i in range (0,len(months)):
            self.birthday[1].addItem(months[i])
        self.birthday[2].clear()
        self.birthday[2].addItem("Day")
        
    def dayupdate(self):
        day31 = ["January","March","May","July","August","October","December"]
        self.birthday[2].clear()
        if self.birthday[1].currentText() == "Month":
            self.birthday[2].addItem("Day")
        elif self.birthday[1].currentText() == "February":
            if int(self.birthday[0].currentText())%4 == 0:
                if int(self.birthday[0].currentText())%100 == 0:
                    self.birthday[2].addItem("Day")
                    for i in range (1,28+1):
                        self.birthday[2].addItem(f"{i}")
                else:
                    self.birthday[2].addItem("Day")
                    for i in range (1,29+1):
                        self.birthday[2].addItem(f"{i}")
            else:
                self.birthday[2].addItem("Day")
                for i in range (1,28+1):
                    self.birthday[2].addItem(f"{i}")
        elif self.birthday[1].currentText() in day31:
            self.birthday[2].addItem("Day")
            for i in range (1,31+1):
                self.birthday[2].addItem(f"{i}")
        else:
            self.birthday[2].addItem("Day")
            for i in range (1,30+1):
                self.birthday[2].addItem(f"{i}")
    
    def back(self):
        self.close()
        self.switch = Menu()
    
    def clear(self):
        for elem in self.textboxes:
            elem.setText("")
        self.birthday[0].clear()
        self.birthday[0].addItem("Year")
        for i in range (1950,2021):
            self.birthday[0].addItem(f"{i}")
        self.birthday[1].clear()
        self.birthday[1].addItem("Month")
        self.birthday[2].clear()
        self.birthday[2].addItem("Day")
        self.program.clear()
        program = ["","Architecture","Civil Engineering","Computer Engineering",
                   "Electrical Engineering","Electronics Engineerin",
                   "Environmental & Sanitary Engineering","Industrial Engineering",
                   "Information & Technology","Mechanical Engineering"]
        self.program.move(140,250)
        self.program.resize(250,20)
        for elem in program:
            self.program.addItem(elem)
            
    def submit(self):
        for i in range (0,len(self.textboxes)):
            if self.textboxes[i].text() == '':
                self.noinput.append(self.labels[i])
                
        if self.birthday[0].currentText() == "Year":
            self.noinput.append("Birthday:")
        elif self.birthday[1].currentText() == "Month":
            self.noinput.append("Birthday:")
        elif self.birthday[2].currentText() == "Day":
            self.noinput.append("Birthday:")
        else:
            pass
        
        if self.program.currentText() == "":
            self.noinput.append("Program:")
            
        errormessage = "Please fill up the following: \n\n"
        for elem in self.noinput:
            errormessage += (elem[:-1])+'\n'
            
        if len(self.noinput)!=0:
            QMessageBox.warning(self,'Incomplete Information',errormessage,
                                QMessageBox.Ok,QMessageBox.Ok)
            for elem in self.noinput:
                self.noinput=[]
        
        else:
            QMessageBox.information(self,'Information Complete',
                                    'Registration Complete',QMessageBox.Ok,
                                    QMessageBox.Ok)
            username='z'+self.textboxes[0].text()[:1].lower()+self.textboxes[2].text()[:1].lower()+self.textboxes[1].text().lower()
            file = open('accounts.txt','a')
            file.write(username)
            for elem in self.textboxes:
                file.write(',')
                file.write(elem.text())
            file.write(",")
            file.write(f"{self.birthday[1].currentText()}-{self.birthday[2].currentText()}-{self.birthday[0].currentText()},")
            file.write(f"{self.program.currentText()}")
            file.write('\n')
            file.close()
            
            QMessageBox.warning(self,'Login Details',
                                    f"Please Remember:\t\n\nUsername: {username}\t\nPassword: {self.textboxes[3].text()}\t\n\n",
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)
            
            self.clear()
            self.back()
            
class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Login"
        self.width = 400
        self.height = 300
        self.usernames = []
        self.names = []
        self.lastnames = []
        self.middlenames = []
        self.passwords = []
        self.birthdays = []
        self.programs = []
        self.main()
        
    def center(self):
        window = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        window.moveCenter(center)
        self.move(window.topLeft())
        
    def main(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("pass"))
        self.resize(self.width,self.height)
        self.center()
        self.setFixedSize(self.width, self.height)
        
        self.username = QLabel('Username:',self)
        self.username.move(50,50)
        self.password = QLabel('Password:',self)
        self.password.move(50,90)
        
        self.usernameinput=QLineEdit(self)
        self.usernameinput.move(140,50)
        self.usernameinput.resize(200,20)
        self.passwordinput=QLineEdit(self)
        self.passwordinput.setEchoMode(QLineEdit.Password)
        self.passwordinput.move(140,90)
        self.passwordinput.resize(200,20)
        
        self.loginbutton=QPushButton('Login',self)
        self.loginbutton.move(260,150)
        self.loginbutton.clicked.connect(self.login)
        
        self.backbutton=QPushButton('Back',self)
        self.backbutton.move(50,150)
        self.backbutton.clicked.connect(self.back)
        
        self.show()
        
    def back(self):
        self.close()
        self.switch = Menu()
    
    def login(self):
        num = None
        
        if os.path.isfile('accounts.txt'):
            file = open('accounts.txt','r') 
            
            for row in file:
                element = row.split(',')
                self.usernames.append(element[0])
                self.names.append(element[1])
                self.lastnames.append(element[2])
                self.middlenames.append(element[3])
                self.passwords.append(element[4])
                self.birthdays.append(element[5])
                self.programs.append(element[6])
            
            if self.usernameinput.text().lower() in self.usernames:
                for elem in self.usernames:
                    if self.usernameinput.text().lower() == elem:
                        num = self.usernames.index(elem)
                        if self.passwordinput.text() == self.passwords[num]:
                            QMessageBox.information(self,'Success',
                                        'Login Complete',QMessageBox.Ok,
                                        QMessageBox.Ok)
                            self.usernameinput.setText('')
                            self.passwordinput.setText('')
                            self.proceed()
                        else:
                            QMessageBox.warning(self,'Login Failed',
                                        'Invalid Password!',QMessageBox.Ok,
                                        QMessageBox.Ok)
                            break
                file1 = open('index.txt','w')
                file1.write("{}".format(num))
                file1.close()    
                
            else:
                QMessageBox.warning(self,'Login Failed',
                                        'Invalid Username!',QMessageBox.Ok,
                                        QMessageBox.Ok)
            file.close()
        else:
            QMessageBox.warning(self,'Login Failed',
                                    'Invalid Username!',QMessageBox.Ok,
                                    QMessageBox.Ok)
        
            
    def proceed(self):
        self.close()
        self.window = QtWidgets.QMainWindow()
        self.ui = Scheduler.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def repeat(self):
        ex = Login()
        
        
if __name__ == '__main__':
    app = QApplication (sys.argv)
    ex = Menu()
    sys.exit (app.exec_())