from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import mysql.connector as sql
from datetime import datetime
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.DBname = None
        self.data = {"2000":0, "500":0, "200":0, "100":0, "50":0, "20":0, "10":0, "5":0, "2":0, "1":0, "Date":None, "Time":None}
        self.loginToDB()
        # To validate login credentials.
        try:
            self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd)
            self.cur = self.mydb.cursor()
        except:
            self.messageBox(["You entered wrong credentials.", "ERROR"], "w")
            sys.exit()
        if not self.DBname:
            self.connectToDB()
        # To validate database exists or not
        try:
            self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd, database = self.DBname)
            with open("recordsDB.key", "w") as f:
                    f.write(f"{self.host} {self.DBuser} {self.DBpswd} {self.DBname}")
            self.cur = self.mydb.cursor()
        except:
            ok = self.messageBox(["No database with specified name exists. Do you want to create one?", "NO DATABASE"], "w")
            if ok ==  QMessageBox.Ok:
                self.cur.execute(f"CREATE DATABASE {self.DBname}")
                with open("recordsDB.key", "w") as f:
                    f.write(f"{self.host} {self.DBuser} {self.DBpswd} {self.DBname}")
                self.messageBox(["Database created successfully", "SUCCESS"], "i")
                self.mydb.commit()
                self.mydb = sql.connect(host = self.host, user = self.DBuser, password = self.DBpswd, database = self.DBname)
                self.cur = self.mydb.cursor()
            else:
                sys.exit()
        self.readFromDB()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(879, 852)
        MainWindow.setStyleSheet("background-color: #daedd8")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 881, 91))
        self.frame.setStyleSheet("background-color: #1bcc2f;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.creditDebitLabel = QtWidgets.QLabel(self.frame)
        self.creditDebitLabel.setGeometry(QtCore.QRect(570, 30, 181, 41))
        self.creditDebitLabel.setStyleSheet("font: 30px; font-family: Impact; background-color: #1bcc2f; color: yellow;")
        self.creditDebitLabel.setObjectName("creditDebitLabel")

        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(440, 20, 3, 61))
        self.line_2.setStyleSheet("background-color: black;")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(426, 100, 31, 561))
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.den1 = QtWidgets.QLineEdit(self.centralwidget)
        self.den1.setGeometry(QtCore.QRect(470, 160, 81, 41))
        self.den1.setStyleSheet("background-color: white; font: 25px; color: blue; font-family: times new roman;")
        self.den1.setObjectName("den1")

        self.num1 = QtWidgets.QLineEdit(self.centralwidget)
        self.num1.setGeometry(QtCore.QRect(610, 160, 81, 41))
        self.num1.setStyleSheet("background-color: white; font: 25px; color: green; font-family: times new roman;")
        self.num1.setObjectName("num1")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 170, 21, 21))
        self.label.setStyleSheet("font: 30px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 170, 21, 21))
        self.label_2.setStyleSheet("font: 30px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 250, 21, 21))
        self.label_3.setStyleSheet("font: 30px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 250, 21, 21))
        self.label_4.setStyleSheet("font: 30px;")
        self.label_4.setObjectName("label_4")

        self.den2 = QtWidgets.QLineEdit(self.centralwidget)
        self.den2.setGeometry(QtCore.QRect(470, 240, 81, 41))
        self.den2.setStyleSheet("background-color: white; font: 25px; color: blue; font-family: times new roman;")
        self.den2.setObjectName("den2")

        self.num2 = QtWidgets.QLineEdit(self.centralwidget)
        self.num2.setGeometry(QtCore.QRect(610, 240, 81, 41))
        self.num2.setStyleSheet("background-color: white; font: 25px; color: green; font-family: times new roman;")
        self.num2.setObjectName("num2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 330, 21, 21))
        self.label_5.setStyleSheet("font: 30px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(710, 330, 21, 21))
        self.label_6.setStyleSheet("font: 30px;")
        self.label_6.setObjectName("label_6")
        self.den3 = QtWidgets.QLineEdit(self.centralwidget)

        self.den3.setGeometry(QtCore.QRect(470, 320, 81, 41))
        self.den3.setStyleSheet("background-color: white; font: 25px; color: blue; font-family: times new roman;")
        self.den3.setObjectName("den3")

        self.num3 = QtWidgets.QLineEdit(self.centralwidget)
        self.num3.setGeometry(QtCore.QRect(610, 320, 81, 41))
        self.num3.setStyleSheet("background-color: white; font: 25px; color: green; font-family: times new roman;")
        self.num3.setObjectName("num3")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 410, 21, 21))
        self.label_7.setStyleSheet("font: 30px;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(710, 410, 21, 21))
        self.label_8.setStyleSheet("font: 30px;")
        self.label_8.setObjectName("label_8")
        self.den4 = QtWidgets.QLineEdit(self.centralwidget)

        self.den4.setGeometry(QtCore.QRect(470, 400, 81, 41))
        self.den4.setStyleSheet("background-color: white; font: 25px; color: blue; font-family: times new roman;")
        self.den4.setObjectName("den4")
        
        self.num4 = QtWidgets.QLineEdit(self.centralwidget)
        self.num4.setGeometry(QtCore.QRect(610, 400, 81, 41))
        self.num4.setStyleSheet("background-color: white; font: 25px; color: green; font-family: times new roman;")
        self.num4.setObjectName("num4")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(570, 490, 21, 21))
        self.label_9.setStyleSheet("font: 30px;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(710, 490, 21, 21))
        self.label_10.setStyleSheet("font: 30px;")
        self.label_10.setObjectName("label_10")
        
        self.den5 = QtWidgets.QLineEdit(self.centralwidget)
        self.den5.setGeometry(QtCore.QRect(470, 480, 81, 41))
        self.den5.setStyleSheet("background-color: white; font: 25px; color: blue; font-family: times new roman;")
        self.den5.setObjectName("den5")
        
        self.num5 = QtWidgets.QLineEdit(self.centralwidget)
        self.num5.setGeometry(QtCore.QRect(610, 480, 81, 41))
        self.num5.setStyleSheet("background-color: white; font: 25px; color: green; font-family: times new roman;")
        self.num5.setObjectName("num5")
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(570, 570, 21, 21))
        self.label_11.setStyleSheet("font: 30px;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(710, 570, 21, 21))
        self.label_12.setStyleSheet("font: 30px;")
        self.label_12.setObjectName("label_12")
        
        self.den6 = QtWidgets.QLineEdit(self.centralwidget)
        self.den6.setGeometry(QtCore.QRect(470, 560, 81, 41))
        self.den6.setStyleSheet("background-color: white; font: 25px; color: blue; font-family: times new roman;")
        self.den6.setObjectName("den6")
        
        self.num6 = QtWidgets.QLineEdit(self.centralwidget)
        self.num6.setGeometry(QtCore.QRect(610, 560, 81, 41))
        self.num6.setStyleSheet("background-color: white; font: 25px; color: green; font-family: times new roman;")
        self.num6.setObjectName("num6")
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(570, 650, 21, 21))
        self.label_13.setStyleSheet("font: 30px;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(710, 650, 21, 21))
        self.label_14.setStyleSheet("font: 30px;")
        self.label_14.setObjectName("label_14")
        
        self.den7 = QtWidgets.QLineEdit(self.centralwidget)
        self.den7.setGeometry(QtCore.QRect(470, 640, 81, 41))
        self.den7.setStyleSheet("background-color: white; font: 25px; color: blue; font-family: times new roman;")
        self.den7.setObjectName("den7")
        
        self.num7 = QtWidgets.QLineEdit(self.centralwidget)
        self.num7.setGeometry(QtCore.QRect(610, 640, 81, 41))
        self.num7.setStyleSheet("background-color: white; font: 25px; color: green; font-family: times new roman;")
        self.num7.setObjectName("num7")
        
        self.currStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.currStatusLabel.setGeometry(QtCore.QRect(110, 30, 181, 41))
        self.currStatusLabel.setStyleSheet("font: 30px; font-family: Impact; background-color: #1bcc2f; color: yellow;")
        self.currStatusLabel.setObjectName("currStatusLabel")
        
        self.tot1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.tot1.setGeometry(QtCore.QRect(750, 160, 101, 41))
        self.tot1.setStyleSheet("background-color: white; color: red; ")
        self.tot1.setObjectName("tot1")
        
        self.tot2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.tot2.setGeometry(QtCore.QRect(750, 240, 101, 41))
        self.tot2.setStyleSheet("background-color: white; color: red; ")
        self.tot2.setObjectName("tot2")
        
        self.tot4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.tot4.setGeometry(QtCore.QRect(750, 400, 101, 41))
        self.tot4.setStyleSheet("background-color: white; color: red; ")
        self.tot4.setObjectName("tot4")
        
        self.tot3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.tot3.setGeometry(QtCore.QRect(750, 320, 101, 41))
        self.tot3.setStyleSheet("background-color: white; color: red; ")
        self.tot3.setObjectName("tot3")
        
        self.tot6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.tot6.setGeometry(QtCore.QRect(750, 560, 101, 41))
        self.tot6.setStyleSheet("background-color: white; color: red; ")
        self.tot6.setObjectName("tot6")
        
        self.tot5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.tot5.setGeometry(QtCore.QRect(750, 480, 101, 41))
        self.tot5.setStyleSheet("background-color: white; color: red; ")
        self.tot5.setObjectName("tot5")
        
        self.tot7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.tot7.setGeometry(QtCore.QRect(750, 640, 101, 41))
        self.tot7.setStyleSheet("background-color: white; color: red; ")
        self.tot7.setObjectName("tot7")
        
        self.curStatusTable = QtWidgets.QTableWidget(self.centralwidget)
        self.curStatusTable.setGeometry(QtCore.QRect(20, 120, 391, 411))
        self.curStatusTable.setStyleSheet("background-color: white; font: 20px; font-family: times new roman; color: #6b2c2c")
        self.curStatusTable.setObjectName("curStatusTable")
        self.curStatusTable.setColumnCount(3)
        self.curStatusTable.setRowCount(10)
        self.curStatusTable.horizontalHeader().setDefaultSectionSize(129)
        # For the horizontal labels to be visible
        self.curStatusTable.setHorizontalHeaderLabels(["Denominations", "Number", "Total (in ₹)"])
        self.curStatusTable.horizontalHeader().setStyleSheet("font-size: 16px; font-family: elephant; color: black;")
        self.curStatusTable.setRowCount(0)
        self.curStatusTable.verticalHeader().hide()
        self.curStatusTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.lastUpdatedLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastUpdatedLabel.setGeometry(QtCore.QRect(20, 550, 261, 41))
        self.lastUpdatedLabel.setStyleSheet("font: 30px; font-family: comic sans ms;")
        self.lastUpdatedLabel.setObjectName("lastUpdatedLabel")
        
        self.date = QtWidgets.QTextBrowser(self.centralwidget)
        self.date.setStyleSheet("background-color: white; font: 25px; font-family: times new roman;")
        self.date.setGeometry(QtCore.QRect(20, 610, 181, 41))
        self.date.setObjectName("date")
        
        self.time = QtWidgets.QTextBrowser(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(230, 610, 181, 41))
        self.time.setStyleSheet("background-color: white; font: 25px; font-family: times new roman;")
        self.time.setObjectName("time")
        
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(620, 720, 71, 41))
        self.label_18.setStyleSheet("font-family: Bodoni MT; font: 30px;")
        self.label_18.setObjectName("label_18")
        
        self.total = QtWidgets.QLCDNumber(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(750, 720, 101, 41))
        self.total.setStyleSheet("background-color: white; color: red; font: 10px")
        self.total.setObjectName("total")
        
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(710, 730, 21, 21))
        self.label_19.setStyleSheet("font: 30px;")
        self.label_19.setObjectName("label_19")
        
        self.calculatButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculatButton.setGeometry(QtCore.QRect(450, 720, 121, 41))
        self.calculatButton.setStyleSheet("font: 18px; font-family: Berlin Sans FB;")
        self.calculatButton.setObjectName("calculatButton")
        self.calculatButton.clicked.connect(self.calculate)
        
        self.denominationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.denominationsLabel.setGeometry(QtCore.QRect(450, 120, 121, 21))
        self.denominationsLabel.setStyleSheet("font-family: bodoni mt; font: 18px")
        self.denominationsLabel.setObjectName("denominationsLabel")
        
        self.numberLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberLabel.setGeometry(QtCore.QRect(620, 120, 81, 21))
        self.numberLabel.setStyleSheet("font-family: bodoni mt; font: 18px")
        self.numberLabel.setObjectName("numberLabel")
        
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(770, 120, 51, 21))
        self.totalLabel.setStyleSheet("font-family: bodoni mt; font: 18px")
        self.totalLabel.setObjectName("totalLabel")
        
        self.creditButton = QtWidgets.QPushButton(self.centralwidget)
        self.creditButton.setGeometry(QtCore.QRect(50, 690, 121, 41))
        self.creditButton.setStyleSheet("font: 18px; font-family: Berlin Sans FB;")
        self.creditButton.setObjectName("creditButton")
        self.creditButton.clicked.connect(self.credit)
        
        self.debitButton = QtWidgets.QPushButton(self.centralwidget)
        self.debitButton.setGeometry(QtCore.QRect(250, 690, 121, 41))
        self.debitButton.setStyleSheet("font: 18px; font-family: Berlin Sans FB;")
        self.debitButton.setObjectName("pushButton_3")
        self.debitButton.clicked.connect(self.debit)
        
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(60, 760, 311, 41))
        self.label_23.setStyleSheet("font-family: lucida handwriting; font: 15px; color: purple")
        self.label_23.setObjectName("label_23")

        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(590, 780, 121, 41))
        self.resetButton.setStyleSheet("font: 18px; font-family: Berlin Sans FB;")
        self.resetButton.setObjectName("resetButton")
        self.resetButton.clicked.connect(self.reset)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 879, 21))
        self.menuBar.setObjectName("menuBar")
        self.summary = self.menuBar.addMenu("Summary")
        self.currMonthAction = QAction("Current Month")
        self.bDatesAction = QAction("Between dates")
        self.summary.addAction(self.currMonthAction)  
        self.summary.addAction(self.bDatesAction) 
        self.summary.setStyleSheet("background-color:green;")     
        self.currMonthAction.triggered.connect(self.currMonth)
        self.bDatesAction.triggered.connect(self.bDates)

        # Initialisation
        self.tots = [self.tot1, self.tot2, self.tot3, self.tot4, self.tot5, self.tot6, self.tot7]
        self.totalden = [0,0,0,0,0,0,0]
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.creditDebitLabel.setText(_translate("MainWindow", "CREDIT / DEBIT"))
        self.den1.setText(_translate("MainWindow", "0"))
        self.num1.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "="))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "="))
        self.den2.setText(_translate("MainWindow", "0"))
        self.num2.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "X"))
        self.label_6.setText(_translate("MainWindow", "="))
        self.den3.setText(_translate("MainWindow", "0"))
        self.num3.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "X"))
        self.label_8.setText(_translate("MainWindow", "="))
        self.den4.setText(_translate("MainWindow", "0"))
        self.num4.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "X"))
        self.label_10.setText(_translate("MainWindow", "="))
        self.den5.setText(_translate("MainWindow", "0"))
        self.num5.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "X"))
        self.label_12.setText(_translate("MainWindow", "="))
        self.den6.setText(_translate("MainWindow", "0"))
        self.num6.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "X"))
        self.label_14.setText(_translate("MainWindow", "="))
        self.den7.setText(_translate("MainWindow", "0"))
        self.num7.setText(_translate("MainWindow", "0"))
        self.currStatusLabel.setText(_translate("MainWindow", "Current Status"))
        self.lastUpdatedLabel.setText(_translate("MainWindow", "Last Updated"))
        self.label_18.setText(_translate("MainWindow", "Total"))
        self.label_19.setText(_translate("MainWindow", "="))
        self.calculatButton.setText(_translate("MainWindow", "CALCULATE"))
        self.denominationsLabel.setText(_translate("MainWindow", "Denominations"))
        self.numberLabel.setText(_translate("MainWindow", "Number"))
        self.totalLabel.setText(_translate("MainWindow", "Total"))
        self.creditButton.setText(_translate("MainWindow", "CREDIT"))
        self.debitButton.setText(_translate("MainWindow", "DEBIT"))
        self.label_23.setText(_translate("MainWindow", "Developed by AKASH KUMAR SINGH"))
        self.resetButton.setText(_translate("MainWindow", "RESET"))
        
        self.display()

    def loginToDB(self):
        try:
            with open("recordsDB.key", "r") as f:
                temp = f.read()
            self.host, self.DBuser, self.DBpswd, self.DBname = temp.split()
            return
        except:
            self.host, ok1 = QtWidgets.QInputDialog.getText(MainWindow, "HOST", "Enter the hostname (localhost/IP address): ")
            if ok1:
                self.DBuser, ok2 = QtWidgets.QInputDialog.getText(MainWindow, "DB USER", "Enter the username of MySQL database: ")
                if ok2:
                    self.DBpswd, ok3 = QtWidgets.QInputDialog.getText(MainWindow, "PASSWORD", "Enter your password for database: ")
                    if ok3:
                        return
        sys.exit()

    def connectToDB(self):
        self.DBname, ok = QtWidgets.QInputDialog.getText(MainWindow, "DB NAME", "Enter the name of MySQL database: ")
        if ok:
            return

    def readFromDB(self):
        now = datetime.now()
        self.defaultDenominations = ["2000", "500", "200", "100", "50", "20", "10", "5", "2", "1"]
        try:
            self.cur.execute("SELECT * FROM records ORDER BY S_No DESC LIMIT 1")
            raw = self.cur.fetchall()
            for i in range(len(self.defaultDenominations)):
               self.data[self.defaultDenominations[i]] = raw[0][i+1]
            self.sno = raw[0][0]
            self.data["Date"] = raw[0][-4]
            self.data["Time"] = raw[0][-3]
        except:
            self.cur.execute("CREATE TABLE records (S_No int, `2000` int, `500` int, `200` int, `100` int, `50` int, `20` int, `10` int, `5` int, `2` int, `1` int, Date Date, Time varchar(255), Total int, C_D char)" )
            self.cur.execute("INSERT INTO records VALUES (0,0,0,0,0,0,0,0,0,0,0,\"{}\",\"{}\",0,'N')".format(now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")))
            self.mydb.commit()

    def messageBox(self, msg, flag):
        msgBox = QMessageBox()
        if flag == "i":
            msgBox.setIcon(QMessageBox.Information)
        else:
            msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(msg[0])
        msgBox.setWindowTitle(msg[1])
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return msgBox.exec()

    def calculate(self):
        self.denominations = [self.den1.text(), self.den2.text(), self.den3.text(), self.den4.text(), self.den5.text(), self.den6.text(), self.den7.text()]
        self.number = [self.num1.text(), self.num2.text(), self.num3.text(), self.num4.text(), self.num5.text(), self.num6.text(), self.num7.text()]
        for i in range(7):
            if self.denominations[i] == "" or self.number[i] == "":
                self.readFromDB()
                self.messageBox(["One or more fields are blank. Please fill 0 in blank fields.","INSUFFICIENT DATA"], "w")
                return
            elif (not self.denominations[i].isnumeric()) or (not self.number[i].isnumeric()):
                self.messageBox(["Enter only numbers","INCORRECT FORMAT"], "w")
                return
            self.totalden[i] = int(self.denominations[i]) * int(self.number[i])
            self.tots[i].display(self.totalden[i])
        self.total.display(sum(self.totalden))
        
    def credit(self):
        try:
            totalmon = 0
            for i in range(7):
                if self.denominations[i] == "0":
                    continue
                self.data[self.denominations[i]] += int(self.number[i])
        except:
            self.messageBox(["Press calculate first", "TRANSACTION FAILED"], "w")
            return

        for i in self.defaultDenominations:
            totalmon += int(i) * self.data[i]

        now = datetime.now()
        self.data["Date"] = now.strftime("%d-%m-%Y")
        self.data["Time"] = now.strftime("%H:%M:%S")
        self.sno += 1
        self.cur.execute("INSERT INTO records VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, \"{}\", \"{}\", {}, 'C')".format(self.sno, self.data["2000"], self.data["500"], self.data["200"], self.data["100"], self.data["50"], self.data["20"], self.data["10"], self.data["5"], self.data["2"], self.data["1"], now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), totalmon))
        self.mydb.commit()
        self.display()
        self.messageBox(["Amount credited.", "Transaction Complete"], "i")
        self.denominations = []

    def debit(self):
        try:
            totalmon = 0
            for i in range(7):
                if self.denominations[i] == "0":
                    continue
                if self.data[self.denominations[i]] < int(self.number[i]):
                    self.readFromDB()
                    self.messageBox(["Insufficient denomiantions.", "TRANSACTION FAILED"], "w")
                    return
                self.data[self.denominations[i]] -= int(self.number[i])
        except:
            self.messageBox(["Press calculate first", "TRANSACTION FAILED"], "w")
            return

        for i in self.defaultDenominations:
            totalmon += int(i) * self.data[i]

        now = datetime.now()
        self.data["Date"] = now.strftime("%d-%m-%Y")
        self.data["Time"] = now.strftime("%H:%M:%S")
        self.sno += 1
        self.cur.execute("INSERT INTO records VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, \"{}\", \"{}\", {}, 'D')".format(self.sno, self.data["2000"], self.data["500"], self.data["200"], self.data["100"], self.data["50"], self.data["20"], self.data["10"], self.data["5"], self.data["2"], self.data["1"], now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), totalmon))
        self.mydb.commit()
        self.display()
        self.messageBox(["Amount debited.", "Transaction Complete"], "i")
        self.denominations = []

    def display(self):
        self.curStatusTable.setRowCount(0)
        self.count = 0
        denTotal = 0
        total = 0
        for i in self.data.keys():
            if i == "S_No":
                continue
            if self.count == 10:
                break
            denTotal += self.data[i]
            total += int(i)*self.data[i]
            self.curStatusTable.insertRow(self.count)
            item1 = QTableWidgetItem(i)
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item2 = QTableWidgetItem(str(self.data[i]))
            item2.setTextAlignment(QtCore.Qt.AlignCenter)
            item3 = QTableWidgetItem(str(int(i)*(self.data[i])))
            item3.setTextAlignment(QtCore.Qt.AlignCenter)
            self.curStatusTable.setItem(self.count, 0, QTableWidgetItem(item1))
            self.curStatusTable.setItem(self.count, 1, QTableWidgetItem(item2))
            self.curStatusTable.setItem(self.count, 2, QTableWidgetItem(item3))
            self.count += 1
        self.curStatusTable.insertRow(self.count)
        item1 = QTableWidgetItem("SUM")
        item1.setTextAlignment(QtCore.Qt.AlignCenter)
        item2 = QTableWidgetItem(str(denTotal))
        item2.setTextAlignment(QtCore.Qt.AlignCenter)
        item3 = QTableWidgetItem(str(total))
        item3.setTextAlignment(QtCore.Qt.AlignCenter)
        self.curStatusTable.setItem(self.count, 0, QTableWidgetItem(item1))
        self.curStatusTable.setItem(self.count, 1, QTableWidgetItem(item2))
        self.curStatusTable.setItem(self.count, 2, QTableWidgetItem(item3))

        self.date.setText(str(self.data["Date"]))
        self.time.setText(self.data["Time"])

    def reset(self):
        fields = [self.den1, self.den2, self.den3, self.den4, self.den5, self.den6, self.den7, self.num1, self.num2, self.num3, self.num4, self.num5, self.num6, self.num7]
        for i in fields:
            i.setText("0")
        for i in self.tots:
            i.display(0)

    def bDates(self):
        now = datetime.now()
        Sdate, ok1 = QtWidgets.QInputDialog.getText(MainWindow, "Start Date", "Enter the start date (dd-mm-yyyy): ")
        if ok1:
            Edate, ok2 = QtWidgets.QInputDialog.getText(MainWindow, "End Date", "Enter the end date (dd-mm-yyyy): ")
            if ok2:
                self.cur.execute("SELECT * FROM records WHERE Date BETWEEN '{}' AND '{}'".format(Sdate, Edate))
                statement = self.cur.fetchall()
                statement.insert(0, ("Transaction id", "2000", "500", "200", "100", "50", "20", "10", "5", "2", "1", "Date", "Time", "Total", "Credit/Debit"))
                text = "Statement (" + Sdate + " to " + Edate + ")"
                pdf = SimpleDocTemplate(filename=text +".pdf", pagesize=A4)

                table = Table(statement)

                style = TableStyle([('BACKGROUND', (0,0),(-1,0),colors.black), 
                                    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                                    ('BOTTOMPADDING', (0,0),(-1,0),6),
                                    ('ALIGN',(0,0),(-1,0),'CENTER'),
                                    ('VALIGN',(0,0),(-1,0),'MIDDLE'),
                                    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                                    ('ALIGN', (-1,0),(-1,-1), 'CENTER'),
                                    ('ALIGN', (0,0),(0,-1), 'CENTER')])
                table.setStyle(style)

                ss = getSampleStyleSheet()
                s = (ParagraphStyle(name= "center", alignment=TA_CENTER, parent=ss['Heading2'], spaceAfter=14))
                text = Paragraph(text,style=s)
                elems = [text, table]
                pdf.build(elems)

                self.messageBox(["Monthly statement saved succefully", "SUCCESS"], "i")
            return
        return

    def currMonth(self):
        now = datetime.now()
        self.cur.execute("SELECT * FROM records WHERE MONTH(Date) = MONTH(CURRENT_DATE()) AND YEAR(Date) = YEAR(CURRENT_DATE())")
        statement = self.cur.fetchall()
        statement.insert(0, ("Transaction id", "2000", "500", "200", "100", "50", "20", "10", "5", "2", "1", "Date", "Time", "Total", "Credit/Debit"))
        text = "Monthly Statement " + str(now.strftime("%B-%Y"))
        pdf = SimpleDocTemplate(filename=text+".pdf", pagesize=A4)
        

        table = Table(statement)

        style = TableStyle([('BACKGROUND', (0,0),(-1,0),colors.black), 
                            ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                            ('BOTTOMPADDING', (0,0),(-1,0),6),
                            ('ALIGN',(0,0),(-1,0),'CENTER'),
                            ('VALIGN',(0,0),(-1,0),'MIDDLE'),
                            ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                            ('ALIGN', (-1,0),(-1,-1), 'CENTER'),
                            ('ALIGN', (0,0),(0,-1), 'CENTER')])
        table.setStyle(style)

        ss = getSampleStyleSheet()
        s = (ParagraphStyle(name= "center", alignment=TA_CENTER, parent=ss['Heading2'], spaceAfter=14))
        text = Paragraph(text,style=s)
        elems = [text, table]
        pdf.build(elems)

        self.messageBox(["Monthly statement saved succefully", "SUCCESS"], "i")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
