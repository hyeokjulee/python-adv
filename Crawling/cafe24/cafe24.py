import sys, pymysql
from PyQt5.QtWidgets import *
from PyQt5 import uic

conn = pymysql.connect(host='davidgeunhosting.cafe24.com', user='davidgeunhosting', password='', db='davidgeunhosting', charset='UTF8')
cur = conn.cursor()   

form_class = uic.loadUiType("cafe24.ui")[0]
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.userFunction)
        self.pushButton_2.clicked.connect(self.feedFunction)

    def userFunction(self):
        cur.execute("SELECT id FROM user ORDER BY ts")
        result0 = cur.fetchall()
        cur.execute("SELECT password FROM user ORDER BY ts")
        result1 = cur.fetchall()
        cur.execute("SELECT name FROM user ORDER BY ts")
        result2 = cur.fetchall()
        cur.execute("SELECT ts FROM user ORDER BY ts")
        result3 = cur.fetchall()
        cur.execute("SELECT approve FROM user ORDER BY ts")
        result4 = cur.fetchall()

        self.tableWidget.clear()

        self.tableWidget.setItem(0, 0, QTableWidgetItem('id'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem('password'))
        self.tableWidget.setItem(0, 2, QTableWidgetItem('name'))
        self.tableWidget.setItem(0, 3, QTableWidgetItem('ts'))
        self.tableWidget.setItem(0, 4, QTableWidgetItem('approve'))

        for i in range(0, len(result0)):
            self.tableWidget.setItem(i + 1, 0, QTableWidgetItem(str(result0[i][0]).split('\'')[1]))
            self.tableWidget.setItem(i + 1, 1, QTableWidgetItem(str(result1[i][0]).split('\'')[1]))
            self.tableWidget.setItem(i + 1, 2, QTableWidgetItem(str(result2[i][0]).split('\'')[1]))
            self.tableWidget.setItem(i + 1, 3, QTableWidgetItem(str(result3[i][0])))
            self.tableWidget.setItem(i + 1, 4, QTableWidgetItem(str(result4[i][0])))

    def feedFunction(self):
        cur.execute("SELECT no FROM feed ORDER BY ts")
        result0 = cur.fetchall()
        cur.execute("SELECT id FROM feed ORDER BY ts")
        result1 = cur.fetchall()
        cur.execute("SELECT content FROM feed ORDER BY ts")
        result2 = cur.fetchall()
        cur.execute("SELECT ts FROM feed ORDER BY ts")
        result3 = cur.fetchall()

        self.tableWidget.clear()

        self.tableWidget.setItem(0, 0, QTableWidgetItem('no'))
        self.tableWidget.setItem(0, 1, QTableWidgetItem('id'))
        self.tableWidget.setItem(0, 2, QTableWidgetItem('content'))
        self.tableWidget.setItem(0, 3, QTableWidgetItem('ts'))

        for i in range(0, len(result0)):
            self.tableWidget.setItem(i + 1, 0, QTableWidgetItem(str(result0[i][0])))
            self.tableWidget.setItem(i + 1, 1, QTableWidgetItem(str(result1[i][0]).split('\'')[1]))
            self.tableWidget.setItem(i + 1, 2, QTableWidgetItem(str(result2[i][0]).split('\'')[1]))
            self.tableWidget.setItem(i + 1, 3, QTableWidgetItem(str(result3[i][0])))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()