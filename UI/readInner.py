import pyttsx3, os, sys
import qtawesome
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QTextEdit, QFileDialog


class ReadInner(object):
    def __init__(self):
        pass

    def strReadInner(self, str):
        engine = pyttsx3.init()
        engine.say(str)
        engine.runAndWait()

    def fileReadInner(self, filename):
        engine = pyttsx3.init()

        # 设置发音速率，默认值为200
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate - 30)

        # 设置发音大小，范围为0.0-1.0
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 0.6)

        # 需要自己下载语音包安装
        # 0：汉语女声；1：英语男声；2：英语女声；3：日语女声；4：韩语女声；5：英语女声；6：粤语女声；7：台语女声
        voices = engine.getProperty('voices')
        voices = engine.setProperty('voice', voices[0].id)

        if os.path.exists(filename):
            with open(filename, 'r',encoding='utf-8') as file:
                line = file.readline()
                while line:
                    engine.say(line)
                    line = file.readline()
        else:
            with open(filename, 'w') as file:
                print('Create a new file named %s' % filename)
        engine.runAndWait()

    # 检查已有的语音包
    def checkExistedVoicePack(self):
        engine = pyttsx3.init()  # 初始化
        voices = engine.getProperty('voices')
        for voice in voices:
            print('id = {} \nname = {} \n'.format(voice.id, voice.name))


class ReadUi(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

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



        self.textEdit = QTextEdit()  # 创建文本框用于显示
        self.right_layout.addWidget(self.textEdit, 0, 0, 4, 8)

        self.button1 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "导入代码")  # 创建按钮1
        self.left_layout.addWidget(self.button1, 2, 0, 1, 3)
        self.button1.clicked.connect(self.open_code)
        self.button2 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "保存代码")  # 创建按钮2
        self.left_layout.addWidget(self.button2, 7, 0, 1, 3)
        self.button2.clicked.connect(self.save_code)
        self.button3 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "朗读代码")  # 创建按钮3
        self.left_layout.addWidget(self.button3, 12, 0, 1, 3)
        self.button3.clicked.connect(self.read_code)

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

    def open_code(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', '.')
            with open(fname[0], 'r',encoding='utf-8') as f:
                data = f.read()
                self.textEdit.setText(data)
        except Exception as e:
            print(e)

    def read_code(self):
        try:
            text=self.textEdit.toPlainText()
            read=ReadInner()
            read.strReadInner(text)
        except Exception as e:
            print(e)

    def save_code(self):
        data=self.textEdit.toPlainText()
        filename = QFileDialog.getSaveFileName(self, 'Open file', '.')[0]  # 舍去All Files (*)部分
        with open(filename, 'w') as f:
            f.write(data)

if __name__=='__main__':
    # file_name=(os.path.split(os.path.realpath(__file__))[0]+'\北岛诗集.txt')
    # # with open(file_name,encoding='utf-8') as f:
    # #     print(f.read())
    #
    # read=ReadInner()
    # read.fileReadInner(file_name)

    app = QtWidgets.QApplication(sys.argv)
    gui = ReadUi()
    gui.show()
    sys.exit(app.exec_())

