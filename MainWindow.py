import numpy as np
import pandas as pd
from PyQt5.QtCore import pyqtSlot, QDir
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel
from pyqtgraph import PlotWidget

from CommonAlg import CommonAlg
from MainWindow2 import Ui_MainWindow
from UpgradeAlg import UpgradeAlg
from main import cal_distance_matrix, findCorrectPath, column, num_point, read_all_lines, cal_total_distance

bestG_x = []
bestG_y = []


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.graphicsView = PlotWidget(self.widget_central)
        self.verticalLayout_9.addWidget(self.graphicsView)

        self.graphicsView2 = PlotWidget(self.widget_central)
        self.verticalLayout_10.addWidget(self.graphicsView2)

    def cal_view_Common(self):
        pop = int(self.lineEdit.text())
        iter = int(self.lineEdit_2.text())
        print(pop, iter)

        result = []
        for i in range(self.listWidget.count()):
            items = self.listWidget.item(i)
            result.append(items.text())
        a = len(result)
        res = [0] * a
        for i in range(a):
            res[i] = [0] * 2
        for i in range(len(result)):
            a, b = result[i].split(" ")
            res[i][0] = float(a)
            res[i][1] = float(b)
        print(res)
        distance_matrix = cal_distance_matrix(res)
        print(distance_matrix)
        alg = CommonAlg(func=cal_total_distance, numCity=num_point(res), size_pop=pop, max_iter=iter,
                        distance_matrix=distance_matrix)

        best_x, best_y = alg.run()
        best_points_ = np.concatenate([best_x, [best_x[0]]])
        best_points_coordinate = findCorrectPath(best_points_)

        best_x = column(best_points_coordinate, 1)
        best_y = column(best_points_coordinate, 2)

        self.pg_calc(best_x, best_y)

        self.pg_calc2(alg.y_best_history)
        global bestG_x
        bestG_x = best_x
        global bestG_y
        bestG_y = best_y

    def cal_view_Upg(self):
        pop = int(self.lineEdit.text())
        iter = int(self.lineEdit_2.text())

        result = []
        for i in range(self.listWidget.count()):
            items = self.listWidget.item(i)
            result.append(items.text())
        a = len(result)
        res = [0] * a
        for i in range(a):
            res[i] = [0] * 2
        for i in range(len(result)):
            a, b = result[i].split(" ")
            res[i][0] = float(a)
            res[i][1] = float(b)
        distance_matrix = cal_distance_matrix(res)

        alg = UpgradeAlg(func=cal_total_distance, numCity=num_point(res), size_pop=pop, max_iter=iter,
                         distance_matrix=distance_matrix)

        best_x, best_y = alg.run()
        best_points_ = np.concatenate([best_x, [best_x[0]]])
        best_points_coordinate = findCorrectPath(best_points_)

        best_x = column(best_points_coordinate, 1)
        best_y = column(best_points_coordinate, 2)

        self.pg_calc(best_x, best_y)

        self.pg_calc2(alg.y_best_history)
        global bestG_x
        bestG_x = best_x
        global bestG_y
        bestG_y = best_y

    def Upload(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        global bestG_x
        global bestG_y
        if dialog.exec_():
            file_name = dialog.selectedFiles()

            if file_name[0].endswith('.txt'):
                with open(file_name[0], "a") as file:
                    file.truncate(0)
                    for i in range(len(bestG_x)):
                        file.writelines([repr(bestG_x[i]) + " "])
                        file.writelines([repr(bestG_y[i]) + "\n"])
                    file.close()
            else:
                pass

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

    def loadCity(self):
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
            for i in range(len(result)):
                k = result[i][0]
                n = result[i][1]
                v = str(k) + "   " + str(n)
                self.listWidget.addItem(str(k) + " " + str(n))

    def getCoord(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()

            if file_name[0].endswith('.txt'):
                with open(file_name[0], "a") as file:
                    file.truncate(0)
                    for i in range(self.listWidget.count()):
                        items = self.listWidget.item(i)
                        file.writelines((str(items.text())) + " \n")
                    file.close()
            else:
                pass

    def pg_calc(self, best_x, best_y):
        self.graphicsView.clear()
        self.graphicsView.plot(best_x, best_y)

    def pg_calc2(self, x):
        self.graphicsView2.clear()
        df = pd.DataFrame(x).cummin()
        q = []

        for i in range(len(df)):
            q.append(df[0].loc[i])
        self.graphicsView2.plot(q)

    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        self.cal_view_Common()

    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        self.cal_view_Upg()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.load()

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.Upload()

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.loadCity()

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        self.getCoord()
