# 로또 당첨번호 조회 앱

import requests, sys
from bs4 import BeautifulSoup as bs
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("lotto.ui")[0]
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.dhlotteryFunction)

    def dhlotteryFunction(self):
        html = bs(requests.get("https://dhlottery.co.kr/common.do?method=main").text)
        nums = html.select('span.ball_645')

        self.lineEdit_1.setText(nums[0].text)
        self.lineEdit_2.setText(nums[1].text)
        self.lineEdit_3.setText(nums[2].text)
        self.lineEdit_4.setText(nums[3].text)
        self.lineEdit_5.setText(nums[4].text)
        self.lineEdit_6.setText(nums[5].text)
        self.lineEdit_7.setText(nums[6].text)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()