import sys

import qtawesome
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QGridLayout, QMainWindow, QPushButton, QFileDialog, QLabel, QTextEdit
from lxml import etree
import time
from MyQR import myqr

def download_img(url,username):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }
    img = requests.get(url, headers=head)
    with open(f'{username}.jpg','wb') as f:
        f.write(img.content)

def get_blog(url):
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }
    response = requests.get(url , headers=head)
    if response.status_code >= 200 or response.status_code < 300:
        html = etree.HTML(response.text)
        img = html.xpath('//div/div[1]/div[2]/div[1]/div[1]/img')
        username = html.xpath('//div/div[1]/div[2]/div[2]/div[1]/div[1]')
        content = html.xpath('//div/div[2]/div/div[2]/div/div[2]/div/div/div/article/a')
        img_url=img[0].attrib["src"]
        print(f'头像地址:{img_url}')
        download_img(img_url,username[0].text)

        #写之前先清空一下
        with open(f'{username[0].text}.txt', "a+", encoding='utf-8') as f:
            f.truncate(0)

        for x,i in enumerate(content[:5]):
            title = i.xpath('./div[1]/h4')
            with open(f'{username[0].text}.txt', "a", encoding='utf-8') as f:
                f.write(f'第: {x+1} 篇文章标题：{title[0].text}\n')
                print(f'正在写入第: {x+1} 篇文章，标题为：{title[0].text} ')
                time.sleep(0.5)
            time.sleep(1)
    return username[0].text

def create_QRcode(username,url):
    myqr.run(words=url,
             picture=f'{username}.jpg',
             colorized=True,    # True：彩色，False：黑白
             save_name=f'{username}_qrcode.png')

class QRcodeUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.username=None
        self.url=None
    def initUI(self):
        self.setFixedSize(960, 700)
        self.main_widget = QWidget()  # 创建窗口主部件
        self.main_layout = QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QGridLayout()  # 创建左侧部件的网格布局
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格布局

        self.right_widget = QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()  # 创建右侧部件的网格布局
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格布局

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件


        self.button1 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "获取用户文章")  # 创建按钮1
        self.left_layout.addWidget(self.button1, 2, 0, 1, 3)
        self.button1.clicked.connect(self.get_content)
        self.button2 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "获取用户头像")  # 创建按钮2
        self.left_layout.addWidget(self.button2, 7, 0, 1, 3)
        self.button2.clicked.connect(self.get_img)
        self.button3 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "生成二维码")  # 创建按钮3
        self.left_layout.addWidget(self.button3, 12, 0, 1, 3)
        self.button3.clicked.connect(self.get_qrcode)

        #搜索部分
        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索 ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入要搜索的网址")
        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        #美化
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        #按钮绑定相应事件
        self.left_close.clicked.connect(self.close)
        self.left_visit.clicked.connect(self.showMaximized)
        self.left_mini.clicked.connect(self.showMinimized)
        #分配位置
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        #QSS
        self.left_widget.setStyleSheet('''
          QPushButton{border:none;color:white;}
          QPushButton#left_label{
            border:none;
            border-bottom:1px solid white;
            font-size:18px;
            font-weight:700;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
          }
          QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_close.setFixedSize(15,15) # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15) # 设置按钮大小
        self.left_mini.setFixedSize(15, 15) # 设置最小化按钮大小
        self.main_widget.setStyleSheet('''
        QWidget#left_widget{
        background:gray;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-left:1px solid white;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
        }
        ''')
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0) #空隙
    #3个函数实现窗口移动
    def mousePressEvent(self, event):
        try:
            if event.button() == QtCore.Qt.LeftButton:
                self.m_flag = True
                self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
                event.accept()
                self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标
        except Exception as e:
            print(e)
    def mouseMoveEvent(self, QMouseEvent):
        try:
            if QtCore.Qt.LeftButton and self.m_flag:
                self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
                QMouseEvent.accept()
        except Exception as e:
            print(e)
    def mouseReleaseEvent(self, QMouseEvent):
        try:
            self.m_flag = False
            self.setCursor(QCursor(QtCore.Qt.ArrowCursor))
        except Exception as e:
            print(e)

    def get_img(self):
        try:
            if not self.username:
                self.url=self.right_bar_widget_search_input.text()
                self.username=get_blog(self.url)
            self.label_image = QLabel(self)
            self.right_layout.addWidget(self.label_image, 1, 0, 10, 10)
            self.image = QtGui.QPixmap(f'{self.username}.jpg')
            self.label_image.setPixmap(self.image)
        except Exception as e:
            print(e)


    def get_content(self):
        try:
            if not self.username:
                self.url = self.right_bar_widget_search_input.text()
                self.username = get_blog(self.url)
            self.textEdit = QTextEdit()  # 创建文本框用于显示
            self.right_layout.addWidget(self.textEdit, 1, 0, 10, 10)
            with open(f'{self.username}.txt', 'r',encoding='utf-8') as f:
                data = f.read()
                self.textEdit.setText(data)
        except Exception as e:
            print(e)

    def get_qrcode(self):
        try:
            self.label_image = QLabel(self)
            self.right_layout.addWidget(self.label_image, 1, 0, 10, 10)
            # self.url = self.right_bar_widget_search_input.text()
            create_QRcode(self.username,self.url)
            self.image = QtGui.QPixmap(f'{self.username}_qrcode.png')
            self.label_image.setPixmap(self.image)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    # url = input('请输入CSDN链接：')
    # download_img(url, 'xia')
    # username,img_url=get_blog(url)
    # create_QRcode('JeronZhou','https://blog.csdn.net/JeronZhou?spm=1001.2014.3001.5509')
    app = QtWidgets.QApplication(sys.argv)
    gui = QRcodeUI()
    gui.show()

    sys.exit(app.exec_())
