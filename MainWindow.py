# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(578, 195)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QRect(10, 70, 191, 23))
        self.progressBar.setValue(0)
        self.pbtn_importStudentFile = QPushButton(self.centralwidget)
        self.pbtn_importStudentFile.setObjectName(u"pbtn_importStudentFile")
        self.pbtn_importStudentFile.setGeometry(QRect(10, 30, 151, 31))
        font = QFont()
        font.setFamilies([u"\u7b49\u7ebf"])
        font.setPointSize(13)
        self.pbtn_importStudentFile.setFont(font)
        self.label_nowStudentsFile = QLabel(self.centralwidget)
        self.label_nowStudentsFile.setObjectName(u"label_nowStudentsFile")
        self.label_nowStudentsFile.setGeometry(QRect(10, 100, 191, 61))
        font1 = QFont()
        font1.setFamilies([u"\u7b49\u7ebf"])
        font1.setPointSize(12)
        self.label_nowStudentsFile.setFont(font1)
        self.label_nowStudentsFile.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_nowStudentsFile.setWordWrap(True)
        self.rb_ifReCall = QRadioButton(self.centralwidget)
        self.rb_ifReCall.setObjectName(u"rb_ifReCall")
        self.rb_ifReCall.setGeometry(QRect(230, 80, 161, 31))
        self.rb_ifReCall.setFont(font)
        self.pbtn_Call = QPushButton(self.centralwidget)
        self.pbtn_Call.setObjectName(u"pbtn_Call")
        self.pbtn_Call.setGeometry(QRect(220, 10, 81, 61))
        font2 = QFont()
        font2.setFamilies([u"\u7b49\u7ebf"])
        font2.setPointSize(14)
        self.pbtn_Call.setFont(font2)
        self.showResult = QTextEdit(self.centralwidget)
        self.showResult.setObjectName(u"showResult")
        self.showResult.setGeometry(QRect(320, 10, 231, 61))
        font3 = QFont()
        font3.setFamilies([u"\u534e\u6587\u6977\u4f53"])
        font3.setPointSize(15)
        self.showResult.setFont(font3)
        self.label_total = QLabel(self.centralwidget)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setGeometry(QRect(220, 110, 51, 31))
        self.label_total.setFont(font1)
        self.samStudent = QLabel(self.centralwidget)
        self.samStudent.setObjectName(u"samStudent")
        self.samStudent.setGeometry(QRect(230, 140, 111, 21))
        font4 = QFont()
        font4.setFamilies([u"\u7b49\u7ebf Light"])
        font4.setPointSize(11)
        self.samStudent.setFont(font4)
        self.callAndUncall = QLabel(self.centralwidget)
        self.callAndUncall.setObjectName(u"callAndUncall")
        self.callAndUncall.setGeometry(QRect(350, 140, 211, 21))
        self.callAndUncall.setFont(font4)
        self.perCallStudent = QSpinBox(self.centralwidget)
        self.perCallStudent.setObjectName(u"perCallStudent")
        self.perCallStudent.setGeometry(QRect(510, 85, 42, 22))
        font5 = QFont()
        font5.setFamilies([u"Symbol"])
        font5.setPointSize(11)
        self.perCallStudent.setFont(font5)
        self.perCallStudent.setMinimum(1)
        self.perCallStudent.setMaximum(100)
        self.label_perCallStu = QLabel(self.centralwidget)
        self.label_perCallStu.setObjectName(u"label_perCallStu")
        self.label_perCallStu.setGeometry(QRect(390, 80, 111, 31))
        self.label_perCallStu.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 172, 401, 20))
        font6 = QFont()
        font6.setFamilies([u"Nirmala UI"])
        font6.setPointSize(10)
        self.label.setFont(font6)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(210, 105, 361, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(193, 10, 20, 151))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RandomCallStudents", None))
        self.pbtn_importStudentFile.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u5b66\u751f\u6587\u4ef6", None))
        self.label_nowStudentsFile.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6587\u4ef6\uff1a*None*", None))
        self.rb_ifReCall.setText(QCoreApplication.translate("MainWindow", u"\u8df3\u8fc7\u5df2\u70b9\u8fc7\u7684\u5b66\u751f", None))
        self.pbtn_Call.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u540d", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"\u7edf\u8ba1\uff1a", None))
        self.samStudent.setText(QCoreApplication.translate("MainWindow", u"\u603b\u5b66\u751f\u6570\uff1a", None))
        self.callAndUncall.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u70b9\u5b66\u751f/\u672a\u70b9\u5b66\u751f\uff1a", None))
        self.label_perCallStu.setText(QCoreApplication.translate("MainWindow", u"\u5355\u6b21\u70b9\u540d\u4eba\u6570\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Developed by Rander Torres (2024) | Contact: randertorres@qq.com", None))
    # retranslateUi

