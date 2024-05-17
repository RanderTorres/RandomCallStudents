import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from MainWindow import Ui_MainWindow

import random
import pandas
import numpy as np

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ## 一些数据
        # 进度条
        self.prg = 0
        # 导入数据是否成功
        self.ifImport = False
        # 学生姓名列表
        self.name = []
        self.nameForNoRepeat = []
        # 学生总数
        self.num = 0
        # 已点学生
        self.hasCall = 0

        # 锁定窗口大小
        self.setFixedSize(self.width(),self.height())

        ## 按钮绑定槽函数
        # 导入文件
        self.pbtn_importStudentFile.clicked.connect(self.importStudentFile)
        # 点名按钮
        self.pbtn_Call.clicked.connect(self.callStudent)

        self.show()

    # 导入学生姓名文件按钮槽函数
    def importStudentFile(self):
        fileDir, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Excel Files (*.xls *.xlsx)")
        fileFormat = fileDir.split(".")[-1]
        try:
            if fileDir:
                self.progressBar.setValue(0)
                if fileFormat == "xls":
                    df = pandas.read_excel(fileDir, engine="xlrd")
                elif fileFormat == "xlsx":
                    df = pandas.read_excel(fileDir, engine="openpyxl")

                ## 读取学生姓名
                rows, cols = np.where(df == "姓名")
                studentNames = df.iloc[rows[0]+1:, cols[0]].values.flatten().tolist()
                prgS = len(studentNames) + 1
                t = 1
                for i in studentNames:
                    self.progressBar.setValue(int(t*100/prgS))
                    if type(i) == str:
                        pass
                    else:
                        studentNames.remove(i)  # 排除非字符串（有可能最后有平均分）
                    t += 1
                # 成功
                self.ifImport = True
                self.progressBar.setValue(100)
                self.name = studentNames.copy()    # 注意这两行用copy，否则所有列表指向一个存储位置，修改一个，另一个也会变！
                self.nameForNoRepeat = studentNames.copy()
                self.label_nowStudentsFile.setText(fileDir.split("/")[-1])
                self.num = len(self.name)
                self.perCallStudent.setMaximum(self.num)
                self.hasCall = 0
                self.samStudent.setText("学生总数：" + str(self.num))
                self.callAndUncall.setText("已点学生/未点学生："+ str(self.hasCall) + "/" + str(self.num-self.hasCall))
        except:
            self.ifImport = False
            self.progressBar.setValue(0)
            self.name = []
            self.nameForNoRepeat = []
            self.label_nowStudentsFile.setText("当前文件：*None*")
            self.num = 0
            self.perCallStudent.setMaximum(100)
            self.hasCall = 0
            self.samStudent.setText("学生总数：")
            self.callAndUncall.setText("已点学生/未点学生：")
            QMessageBox.warning(self, "错误", "导入文件失败！")

    # 随机点名按钮槽函数
    def callStudent(self):
        if self.ifImport:
            # 清空
            self.showResult.setText("")
            # 抽人
            if (len(self.nameForNoRepeat) >= self.perCallStudent.value()) and self.rb_ifReCall.isChecked():   # 不重复之下，可抽
                t = random.sample(self.nameForNoRepeat, self.perCallStudent.value())
            elif (len(self.nameForNoRepeat) < self.perCallStudent.value()) and self.rb_ifReCall.isChecked():    # 不重复之下，没人抽了
                QMessageBox.warning(self, "错误", "您已勾选“跳过已点过的学生”，现无可以点名的学生了！")
                return 1
            else:
                t = random.sample(self.name, self.perCallStudent.value())
            # 查重
            new = []
            old = []
            for i in t:
                # 之前未点过
                if i in self.nameForNoRepeat:
                    new.append(i)
                    self.hasCall += 1
                    self.nameForNoRepeat.remove(i)
                # 之前点过
                else:
                    old.append(i)
            # 不用管old/new、勾没勾选去重了，去重的话前面抽的时候是从nameForNoRepeat里抽的
            # 显示数据
            self.callAndUncall.setText("已点学生/未点学生："+ str(self.hasCall) + "/" + str(self.num-self.hasCall))
            if len(t) == 1:
                self.showResult.setText(t[0])
            else:
                r = ""
                for i in t:
                    r += i + "、"
                r = r[:-1]
                self.showResult.setText(r)

            del new,old


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())