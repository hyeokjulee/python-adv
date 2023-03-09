# Bugs 음원 차트 조회 앱

import requests, sys, time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("musicChart.ui")[0]
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.bugsFunction)
        self.pushButton_2.clicked.connect(self.melonFunction)
        self.pushButton_3.clicked.connect(self.genieFunction)

    def bugsFunction(self):
        html = bs(requests.get("https://music.bugs.co.kr/chart").text)
        songs = html.select('table.byChart > tbody > tr')

        for i, song in enumerate(songs):
            self.tableWidget.setItem(i, 0, QTableWidgetItem('Bugs'))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(i + 1) + '위'))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(song.select('p.title > a')[0].text))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(song.select('p.artist > a')[0].text))

    def melonFunction(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://www.melon.com/chart/index.htm")
        html = bs(driver.page_source)

        songs = html.select('tbody > tr')

        for i, song in enumerate(songs):
            self.tableWidget.setItem(i, 0, QTableWidgetItem('Melon'))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(i + 1) + '위'))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(song.select('div.rank01 > span > a')[0].text))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(song.select('div.rank02 > a')[0].text))

    def genieFunction(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://www.genie.co.kr/chart/top200?ditc=D&ymd=20230227&hh=16&rtm=Y&pg=1")
        html = bs(driver.page_source)

        songs = html.select('tbody > tr')

        for i, song in enumerate(songs):
            self.tableWidget.setItem(i, 0, QTableWidgetItem('Genie'))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(i + 1) + '위'))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(song.select('a.ellipsis')[0].text.lstrip()))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(song.select('a.ellipsis')[1].text))

        time.sleep(1)

        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://www.genie.co.kr/chart/top200?ditc=D&ymd=20230227&hh=16&rtm=Y&pg=2")
        html = bs(driver.page_source)

        songs = html.select('tbody > tr')

        for i, song in enumerate(songs):
            self.tableWidget.setItem(i + 50, 0, QTableWidgetItem('Genie'))
            self.tableWidget.setItem(i + 50, 1, QTableWidgetItem(str(i + 51) + '위'))
            self.tableWidget.setItem(i + 50, 2, QTableWidgetItem(song.select('a.ellipsis')[0].text.lstrip()))
            self.tableWidget.setItem(i + 50, 3, QTableWidgetItem(song.select('a.ellipsis')[1].text))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()