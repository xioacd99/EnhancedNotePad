import os,sys
import base64

import qtawesome
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QHBoxLayout, QFileDialog, QPushButton, QTextEdit, \
    QGridLayout


class Editor(QWebEngineView):
    def __init__(self, par):
        super().__init__(par)
        self.editor_flag = []

        # 本地html路径
        self.editor_index = (os.path.split(os.path.realpath(__file__))[0]) + "/editor.html"
        self.load(QUrl.fromLocalFile(self.editor_index))

    def set_value(self, data):
        """设置编辑器内容"""
        data = base64.b64encode(data.encode())
        data = data.decode()
        self.page().runJavaScript(f"editor.getModels()[0].setValue(Base.decode('{data}'))")
        print('set',data)


    def change_language(self, lan):
        """切换智能提示语言"""
        self.page().runJavaScript("monaco.editor.setModelLanguage(monaco.editor.getModels()[0],'{lan}')")

    # 重写createeditor()
    def createEditor(self, QWebEnginePage_WebWindowType):
        new_editor = Editor(self.mainwindow)
        self.mainwindow.create_tab(new_editor)
        return new_editor



class VSCUi(QMainWindow):

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



        self.editor = Editor(self)   #self必须要有，是将主窗口作为参数，传给浏览器
        self.right_layout.addWidget(self.editor, 0, 0, 4, 8)

        self.button1 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "代码检测")  # 创建按钮1
        self.left_layout.addWidget(self.button1, 2, 0, 1, 3)
        self.button1.clicked.connect(self.open_code)
        self.button2 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "保存代码")  # 创建按钮2
        self.left_layout.addWidget(self.button2, 7, 0, 1, 3)
        self.button2.clicked.connect(self.save_code)
        self.button3 = QPushButton(qtawesome.icon('fa.sellsy', color='white'), "在线编译")  # 创建按钮3
        self.left_layout.addWidget(self.button3, 12, 0, 1, 3)
        self.button3.clicked.connect(self.compile_code)

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
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')
        with open(fname[0], 'r') as f:
            data = f.read()
            print(f'{data}')
            self.editor.set_value(data)
            #self.editor.page().runJavaScript(f'editor.getModel().setValue({data});')

    def compile_code(self):
        try:
            res = self.editor.page().runJavaScript('editor.getValue();', self.js_callback_compile)
        except Exception as e:
            print(e)

    def save_code(self):
        try:
            res = self.editor.page().runJavaScript('editor.getValue();', self.js_callback_save)
        except Exception as e:
            print(e)

    def js_callback_compile(self,result):
        filename='tmp_code.py'
        with open(filename,'w') as f:
            f.write(result)
        compile(filename)

    def js_callback_save(self,result):
        try:
            filename = QFileDialog.getSaveFileName(self,'Open file', '.')[0] #舍去All Files (*)部分
            with open(filename,'w') as f:
                f.write(result)
        except Exception as e:
            print(e)


def compile(filename):
    filepath=os.getcwd()
    os.system(f'start cmd /K python {filepath}\{filename}')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = VSCUi()
    gui.show()
    # w=Editor(None)
    # w.show()

    sys.exit(app.exec_())