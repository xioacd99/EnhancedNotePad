from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import sys
import qtawesome


class Ui_MainWindow3(object):
    def setupUi(self, Ui_MainWindow3):
        Ui_MainWindow3.setObjectName("Ui_MainWindow3")
        Ui_MainWindow3.resize(511, 367)

        self.pushbutton_close = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushbutton_close.setGeometry(QtCore.QRect(30, 20, 30, 30))
        self.pushbutton_close.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 20, 30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushbutton_mini = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushbutton_mini.setGeometry(QtCore.QRect(130, 20, 30, 30))
        self.pushbutton_mini.setObjectName("pushbutton_mini")
        self.text_label = QtWidgets.QLabel(Ui_MainWindow3)
        self.text_label.setGeometry(QtCore.QRect(80, 130, 351, 91))
        self.text_label.setObjectName("text_label")
        self.pushButton = QtWidgets.QPushButton(Ui_MainWindow3)
        self.pushButton.setGeometry(QtCore.QRect(190, 250, 101, 71))
        self.pushButton.setObjectName("pushbutton_close")
        # self.pushbutton_close = QtWidgets.QPushButton(qtawesome.icon('fa5s.microphone',color='red'),"")
        self.label = QtWidgets.QLabel(Ui_MainWindow3)
        self.label.setGeometry(QtCore.QRect(80, 60, 351, 70))
        self.label.setObjectName("label")


    
        self.retranslateUi(Ui_MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(Ui_MainWindow3)

    def retranslateUi(self, Ui_MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        Ui_MainWindow3.setWindowTitle(_translate("Ui_MainWindow3", "Ui_MainWindow3"))
        self.pushbutton_close.setText(_translate("Ui_MainWindow3", ""))
        self.pushButton_2.setText(_translate("Ui_MainWindow3", ""))
        self.pushbutton_mini.setText(_translate("Ui_MainWindow3", ""))
        self.pushButton.setText(_translate("Ui_MainWindow3", ""))
        self.label.setText(_translate("Ui_MainWindow3", "语音识别"))
        self.text_label.setText("点击下面的按钮开始录制音频\n再次点击停止录音开始识别")

        Ui_MainWindow3.setWindowOpacity(0.9) # 设置窗口透明度
        #Ui_MainWindow3.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        Ui_MainWindow3.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        pe = QPalette()
        Ui_MainWindow3.setAutoFillBackground(True)
        pe.setColor(QPalette.Window,Qt.lightGray)  #设置背景色
        #pe.setColor(QPalette.Background,Qt.blue)
        Ui_MainWindow3.setPalette(pe)

        Ui_MainWindow3.setWindowTitle("语音识别")
        Ui_MainWindow3.setWindowIcon(QtGui.QIcon('A.jpg'))  # 设置图标

        spin_icon = qtawesome.icon('fa5s.microphone-alt', color='black')
        #self.pushButton.setIcon(spin_icon)#设置图标
        Ui_MainWindow3.setWindowIcon(spin_icon)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(widgets)
    widgets.show()
    sys.exit(app.exec_())
