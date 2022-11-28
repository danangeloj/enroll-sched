# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 04:58:37 2020

@author: Dan Julongbayan
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import xlrd
import REGISTRATIONANDLOGIN

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # sets up main window name and size
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1217, 754)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFixedSize(1217,754)
        
        #initializes the layout of the widgets
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 931, 691))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setObjectName("layout")
        
        #create the schedule grid
        self.scheduleGrid = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.scheduleGrid.setAcceptDrops(True)                                  #apply drag and drop functionality
        self.scheduleGrid.setDragEnabled(True)
        self.scheduleGrid.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.scheduleGrid.setDefaultDropAction(QtCore.Qt.MoveAction)            #sets dragdrop function as 'move'
        self.scheduleGrid.setAlternatingRowColors(True)
        self.scheduleGrid.setGridStyle(QtCore.Qt.DashLine)
        self.scheduleGrid.setRowCount(28)
        self.scheduleGrid.setColumnCount(6)
        self.scheduleGrid.setObjectName("scheduleGrid")
        
        # create vertical and horizontal headers
        for i in range(0, 28):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(60)
            item.setFont(font)
            self.scheduleGrid.setVerticalHeaderItem(i, item)
        for i in range(0, 6):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            self.scheduleGrid.setHorizontalHeaderItem(i, item)
        
        # set grid properties
        self.scheduleGrid.horizontalHeader().setVisible(True)
        self.scheduleGrid.horizontalHeader().setCascadingSectionResizes(False)
        self.scheduleGrid.horizontalHeader().setDefaultSectionSize(133)
        self.scheduleGrid.horizontalHeader().setMinimumSectionSize(133)
        self.scheduleGrid.verticalHeader().setVisible(True)
        self.scheduleGrid.verticalHeader().setDefaultSectionSize(24)
        self.scheduleGrid.verticalHeader().setMinimumSectionSize(24)
        self.scheduleGrid.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        #add grid to layout
        self.layout.addWidget(self.scheduleGrid, 0, 0, 1, 1)
        
        #Course list
        self.courselist = QtWidgets.QListWidget(self.centralwidget)
        self.courselist.setGeometry(QtCore.QRect(950, 110, 261, 451))
        self.courselist.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.courselist.setObjectName("courselist")

        #initialize items for courselist
        self.colors = [[85, 255, 255],[85, 255, 127],[255, 85, 255],[255, 238, 41],
                  [170, 170, 127],[230, 21, 25],[235, 121, 27],[198, 15, 234],
                  [39, 67, 247]]
        for i in range(0, 9):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            brush = QtGui.QBrush(QtGui.QColor(self.colors[i][0], self.colors[i][1], self.colors[i][2]))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)
            self.courselist.addItem(item)
            
        #add buttons
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(950, 570, 261, 28))
        self.submit.setObjectName("submit")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(950, 610, 261, 28))
        self.clear.setObjectName("clear")
        self.debug = QtWidgets.QPushButton(self.centralwidget)
        self.debug.setGeometry(QtCore.QRect(950, 650, 261, 28))
        
        #labels
        self.studentinfo = QtWidgets.QLabel(self.centralwidget)
        self.studentinfo.setGeometry(QtCore.QRect(950, 10, 241, 16))
        self.studentinfo.setObjectName("studentinfo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(950, 20, 261, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.studentprogram = QtWidgets.QLabel(self.centralwidget)
        self.studentprogram.setGeometry(QtCore.QRect(950, 30, 251, 20))
        self.studentprogram.setObjectName("studentprogram")
        self.schoolyear = QtWidgets.QLabel(self.centralwidget)
        self.schoolyear.setGeometry(QtCore.QRect(950, 50, 251, 16))
        self.schoolyear.setObjectName("schoolyear")
        self.Courselabel = QtWidgets.QLabel(self.centralwidget)
        self.Courselabel.setGeometry(QtCore.QRect(950, 70, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Courselabel.setFont(font)
        self.Courselabel.setObjectName("Courselabel")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        #menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,1400,26))
        self.menubar.setObjectName("menubar")
        #account tab
        self.menuAccount = QtWidgets.QMenu(self.menubar)
        self.menuAccount.setObjectName("menuAccount")
        MainWindow.setMenuBar(self.menubar)
        #status bar below window
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #logout on account tab
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.triggered.connect(MainWindow.close)
        self.actionLogout.triggered.connect(self.Logout)
        self.actionLogout.setObjectName("actionLogout")
        self.menuAccount.addAction(self.actionLogout)
        self.menubar.addAction(self.menuAccount.menuAction())
        
        #retranslate -- rename
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Logout(self):
        self.switch = REGISTRATIONANDLOGIN.Login()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Scheduler"))
        
        starttime = 7
        endtime = 8
        
        #Vertical Header Items (Timestamps of SchedulerGrid)
        for i in range(1, 29):
            if i % 2 != 0 and i < 9:
                item = self.scheduleGrid.verticalHeaderItem(i-1)
                item.setText(_translate("MainWindow", f"{starttime}:30-{endtime}:00AM"))
            elif i % 2 == 0 and i < 9:
                item = self.scheduleGrid.verticalHeaderItem(i-1)
                item.setText(_translate("MainWindow", f"{endtime}:00-{endtime}:30AM"))
            elif i % 2 != 0 and i >= 9:
                item = self.scheduleGrid.verticalHeaderItem(i-1)
                item.setText(_translate("MainWindow", f"{starttime}:30-{endtime}:00PM"))
            else:
                item = self.scheduleGrid.verticalHeaderItem(i-1)
                item.setText(_translate("MainWindow", f"{endtime}:00-{endtime}:30PM"))
            if i % 2 == 0:
                starttime += 1
                endtime += 1
            if starttime > 12:
                starttime = 1
            if endtime > 12:
                endtime = 1
                
        #Horizontal Header Items (Days of SchedulerGrid)
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        for i in range(0, 6):
            item = self.scheduleGrid.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", days[i]))
        
        #Course List)
        __sortingEnabled = self.courselist.isSortingEnabled()
        self.courselist.setSortingEnabled(False)
        
        self.courses = ["CPE009", "MATH013", "MATH017", "PHYS001C", "GEE001", "GEC004", "MATH019A", "PE002", "NSTP002"]
        for i in range(0,9):
            item = self.courselist.item(i)
            item.setText(_translate("MainWindow", self.courses[i]))
        self.courselist.setSortingEnabled(__sortingEnabled)
        
        #labels
        file1 = open('accounts.txt','r')
        file2 = open('index.txt','r')
        name = []
        program = []
        index = int(file2.readline())
        for row in file1:
            item = row.split(',')
            name.append("{}, {} {}.".format(item[2].title(),item[1].title(),item[3].upper()[:1]))
            program.append(item[6])
        
        self.studentinfo.setText(_translate("MainWindow", "Logged in as: {}".format(name[index])))
        self.studentprogram.setText(_translate("MainWindow", "Program: {}".format(program[index])))
        #self.studentinfo.setText(_translate("MainWindow", "Logged in as: <name>"))
        #self.studentprogram.setText(_translate("MainWindow", "Program: <program>"))
        self.schoolyear.setText(_translate("MainWindow", "School Year: 2020"))
        self.Courselabel.setText(_translate("MainWindow", "COURSES:"))
        
        #Buttons 
        self.submit.setToolTip(_translate("MainWindow","Submits this schedule"))
        self.submit.setText(_translate("MainWindow","Submit"))
        self.clear.setToolTip(_translate("MainWindow","Clears current schedule"))
        self.clear.setText(_translate("MainWindow","Clear"))
        self.menuAccount.setTitle(_translate("MainWindow","Account"))
        self.actionLogout.setText(_translate("MainWindow","Logout"))
        self.actionLogout.setStatusTip(_translate("MainWindow","Quits the scheduler"))
        self.debug.setToolTip(_translate("MainWindow","This will debug the program"))
        self.debug.setText(_translate("MainWindow","Debug"))
        
        #button functions
        self.submit.clicked.connect(self.check)
        self.clear.clicked.connect(self.clean)
        self.debug.clicked.connect(self.debugfunc)
        
    def check(self):
        workbook = xlrd.open_workbook('section-schedules.xlsx')
        sheetnames = workbook.sheet_names()
        for col in range(self.scheduleGrid.columnCount()):
            for row in range(self.scheduleGrid.rowCount()):
                it = self.scheduleGrid.item(row,col)
                if it and it.text():
                    tempit = it
                    for sheet in range(6):
                        worksheet = workbook.sheet_by_index(sheet)
                        if row < 2:
                            tempArow = 0
                            if row == 1:
                                tempBrow = 3
                            else:
                                tempBrow = 2
                        elif row >= 3 or row <= 25:
                            tempArow = row-2
                            tempBrow = row+2
                        elif row > 26:
                            if row == 27:
                                tempArow = 25
                            else:
                                tempArow = 26
                            tempBrow = 28
                        for sheetrow in range(tempArow, tempBrow):
                            if worksheet.cell(sheetrow, col).value == it.text():
                                tempit = it.text()
                                print(f"{tempit} course found in section: {sheetnames[sheet]}")
                                for detectitem in range(tempArow, tempBrow):
                                    if it.text() == worksheet.cell(detectitem, col).value:
                                        itemrow = detectitem
                                        break
                                for detectempty in range(itemrow, self.scheduleGrid.rowCount()):
                                    if worksheet.cell(detectempty, col).value == it.text():
                                        continue
                                    elif worksheet.cell(detectempty, col).value == xlrd.empty_cell.value:
                                        continue
                                    else:
                                        break
                                for paint in range(detectitem, detectempty):
                                    emptyitem = self.scheduleGrid.item(paint, col)
                                    if not emptyitem:
                                        item = QtWidgets.QTableWidgetItem()
                                        if paint != detectempty-1:
                                            item.setText('|')
                                        else:
                                            item.setText('V')
                                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                                        self.scheduleGrid.setItem(paint, col, item)
                                        index = self.courses.index(it.text())
                                        self.scheduleGrid.item(paint, col).setBackground(QtGui.QColor(self.colors[index][0], self.colors[index][1], self.colors[index][2]))
                                    elif emptyitem.text() == '':
                                        item = QtWidgets.QTableWidgetItem()
                                        if paint != detectempty-1:
                                            item.setText('|')
                                        else:
                                            item.setText('V')
                                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                                        self.scheduleGrid.setItem(paint, col, item)
                                        index = self.courses.index(it.text())
                                        self.scheduleGrid.item(paint, col).setBackground(QtGui.QColor(self.colors[index][0], self.colors[index][1], self.colors[index][2]))
                                    else:
                                        continue
                                it.setText(f"{tempit} - {sheetnames[sheet]}")
        ##clean schedules that are not found
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        for col in range(self.scheduleGrid.columnCount()):
            for row in range(self.scheduleGrid.rowCount()):
                it = self.scheduleGrid.item(row,col)
                if (row+1)%2 == 0:
                    brush.setColor(QtGui.QColor(245,245,245))
                else:
                    brush.setColor(QtGui.QColor(255, 255, 255))
                if it and it.text():
                    for elem in self.courses:
                        if it.text() == elem:
                            it.setText('')
                            it.setBackground(brush)

    def clean(self):
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        for row in range(self.scheduleGrid.rowCount()):
            for col in range(0,6):
                if (row+1)%2 == 0:
                    brush.setColor(QtGui.QColor(245,245,245))
                else:
                    brush.setColor(QtGui.QColor(255, 255, 255))
                it = self.scheduleGrid.item(row,col)
                if it:
                    it.setText('')
                    it.setBackground(brush)
        if self.scheduleGrid.rowCount() > 28:
            for i in range(28, self.scheduleGrid.rowCount()):
                self.scheduleGrid.removeRow(i)
                
    def debugfunc(self):
        for row in range(28, self.scheduleGrid.rowCount()):
            self.scheduleGrid.removeRow(row)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        
