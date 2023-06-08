import sys

import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from matplotlib import pyplot as plt

from pyqtgraph import PlotWidget

from CommonAlg import CommonAlg
from UpgradeAlg import UpgradeAlg
from main import cal_total_distance,  findCorrectPath, column, cal_distance_matrix, read_all_lines


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 590)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, -10, 641, 571))
        self.label.setStyleSheet("background:none;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 491, 31))
        self.label_5.setStyleSheet("\n"
                                   "font: 20pt \"TypoUpright BT\";\n"
                                   "color:#ffb703;\n"
                                   "background-color:#000;")
        self.label_5.setObjectName("label_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 20, 350, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "color:#fff;\n"
                                      "background-color:#000;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "font: 20pt \"TypoUpright BT\";\n"
                                      "color:#ffb703;\n"
                                      "background-color:#35362d;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "font: 20pt \"TypoUpright BT\";\n"
                                      "color:#deb316;\n"
                                      "background-color:#8c897b;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "piqtgraph")
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(480, 20, 451, 41))
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
                                      "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                      "color:#fff;\n"
                                      "background-color:#000;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "font: 20pt \"TypoUpright BT\";\n"
                                      "color:#ffb703;\n"
                                      "background-color:#35362d;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "font: 20pt \"TypoUpright BT\";\n"
                                      "color:#deb316;\n"
                                      "background-color:#8c897b;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "piqtgraph")
        self.pushButton2.setObjectName("pushButton")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(10, 170, 361, 31))
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("QPushButton{\n"
                                      "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                      "color:#fff;\n"
                                      "background-color:#000;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "font: 20pt \"TypoUpright BT\";\n"
                                      "color:#ffb703;\n"
                                      "background-color:#35362d;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "font: 20pt \"TypoUpright BT\";\n"
                                      "color:#deb316;\n"
                                      "background-color:#8c897b;\n"
                                      "border- radius: 30;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "piqtgraph")
        self.pushButton3.setObjectName("pushButton")

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(10, 210, 361, 31))
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("QPushButton{\n"
                                       "font: 75 20pt \"MS Shell Dlg 2\";\n"
                                       "color:#fff;\n"
                                       "background-color:#000;\n"
                                       "border- radius: 30;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "font: 20pt \"TypoUpright BT\";\n"
                                       "color:#ffb703;\n"
                                       "background-color:#35362d;\n"
                                       "border- radius: 30;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "font: 20pt \"TypoUpright BT\";\n"
                                       "color:#deb316;\n"
                                       "background-color:#8c897b;\n"
                                       "border- radius: 30;\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "piqtgraph")
        self.pushButton4.setObjectName("pushButton")


        self.input_PRO = QtWidgets.QLineEdit(self.centralwidget)
        self.input_PRO.setGeometry(QtCore.QRect(590, 120, 131, 31))
        self.input_PRO.setStyleSheet("color:#ffb703;\n"
                                     "font: 20pt \"MS Shell Dlg 2\";\n"
                                     "background-color:#000;\n"
                                     "border- radius : 30;\n"
                                     "")
        self.input_PRO.setObjectName("input_PRO")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 361, 31))
        self.label_2.setStyleSheet("\n"
                                   "font: 20pt \"TypoUpright BT\";\n"
                                   "color:#ffb703;\n"
                                   "background-color:#000;")
        self.label_2.setObjectName("label_2")



        self.input_dp = QtWidgets.QLineEdit(self.centralwidget)
        self.input_dp.setGeometry(QtCore.QRect(590, 70, 131, 31))
        self.input_dp.setStyleSheet("color:#ffb703;\n"
                                    "font: 20pt \"MS Shell Dlg 2\";\n"
                                    "background-color:#000;\n"
                                    "border- radius : 30;\n"
                                    "")
        self.input_dp.setObjectName("input_dp")


        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(620, 270, 391, 241))
        self.graphicsView.setStyleSheet("Background:none")
        self.graphicsView.setObjectName("graphicsView")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 520, 261, 31))
        self.label_6.setStyleSheet("font: 15pt \"TypoUpright BT\";\n"
                                   "color:#fab505;\n"
                                   "background:none\n"
                                   "")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(610, 260, 411, 261))
        self.label_16.setStyleSheet("background:#ffb739")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.label_16.raise_()

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 520, 261, 31))
        self.label_7.setStyleSheet("font: 15pt \"TypoUpright BT\";\n"
                                   "color:#fab505;\n"
                                   "background:none\n"
                                   "")


        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(110, 260, 411, 261))
        self.label_17.setStyleSheet("background:#ffb739")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_17.raise_()

        self.graphicsView2 = PlotWidget(self.centralwidget)
        self.graphicsView2.setGeometry(QtCore.QRect(120, 270, 391, 241))
        self.graphicsView2.setStyleSheet("Background:none")
        self.graphicsView2.setObjectName("graphicsView2")

        self.label_5.raise_()
        self.pushButton.raise_()
        self.input_PRO.raise_()
        self.label_2.raise_()
        self.input_dp.raise_()
        self.graphicsView.raise_()
        self.graphicsView2.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Введите муравьев  :"))
        self.pushButton.setText(_translate("MainWindow", " по обычному алгоритму"))
        self.pushButton2.setText(_translate("MainWindow", " по  усовершенстванному алгоритму"))
        self.pushButton3.setText(_translate("MainWindow", " Выгрузить в файл"))
        self.pushButton4.setText(_translate("MainWindow", " Загрузить из файла"))

        self.label_2.setText(_translate("MainWindow", "Введите итерации  :"))
        self.label_6.setText(_translate("MainWindow", "График  "))
        self.label_7.setText(_translate("MainWindow", "График  "))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calcCommon)
        self.pushButton2.clicked.connect(self.calcMy)
        self.pushButton3.clicked.connect(self.Upload)
        self.pushButton4.clicked.connect(self.load)


    def load(self):
        result = []
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()

            if file_name[0].endswith('.txt'):
                with open(file_name[0], "a") as file:

                    lines = read_all_lines(file_name[0])
                    for line in lines:
                        result.append(list(map(lambda x: float(x), line.split())))
                    file.close()
            else:
                pass

        best_x = column(result, 0)
        best_y = column(result, 1)
        self.pg_calc(best_x, best_y)




    def calcMy(self):

        iter = int(self.input_dp.text())
        pop = int(self.input_PRO.text())
        distance_matrix = cal_distance_matrix()
        alg = UpgradeAlg(func=cal_total_distance, numCity=num_points(), size_pop=pop, max_iter=iter,
                        distance_matrix=distance_matrix)

        best_x, best_y = alg.run()
        best_points_ = np.concatenate([best_x, [best_x[0]]])
        best_points_coordinate = findCorrectPath(best_points_)

        self.pg_calc(best_points_)

        self.pg_calc2(alg.y_best_history)
        return best_points_coordinate

    def Upload(self):
        mas= self.calcMy()
        best_x = column(mas, 1)
        best_y = column(mas, 2)
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()

            if file_name[0].endswith('.txt'):
                with open(file_name[0], "a") as file:
                    file.truncate(0)
                    for i in range(len(best_x)):
                        file.writelines([repr(best_x[i]) + " "])
                        file.writelines([repr(best_y[i]) + "\n"])
                    file.close()
            else:
                pass

    def calcCommon(self):
        iter = int(self.input_dp.text())
        pop = int(self.input_PRO.text())

        distance_matrix = cal_distance_matrix()
        alg = CommonAlg(func=cal_total_distance, numCity=num_points(), size_pop=pop, max_iter=iter,
                         distance_matrix=distance_matrix)

        best_x, best_y = alg.run()
        best_points_ = np.concatenate([best_x, [best_x[0]]])
        best_points_coordinate = findCorrectPath(best_points_)

        self.pg_calc(best_points_)

        self.pg_calc2(alg.y_best_history)
        return best_points_coordinate



    def pg_calc(self, best_points_):
        best_points_coordinate = findCorrectPath(best_points_)

        best_x = column(best_points_coordinate, 1)
        best_y = column(best_points_coordinate, 2)
        fig, ax = plt.subplots()
        for index in range(0, len(best_points_)):
            ax.annotate(best_points_[index], (best_x[index], best_y[index]))

        self.graphicsView.clear()
        self.graphicsView.plot(best_x, best_y)



    def pg_calc2(self, x):
        self.graphicsView2.clear()
        df = pd.DataFrame(x).cummin()
        q = []

        for i in range(len(df)):
            q.append(df[0].loc[i])
        self.graphicsView2.plot(q)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
