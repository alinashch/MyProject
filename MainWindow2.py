# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 753)
        self.widget_central = QtWidgets.QWidget(MainWindow)
        self.widget_central.setObjectName("widget_central")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.widget_central)
        self.vertical_layout.setObjectName("vertical_layout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout.addLayout(self.verticalLayout_4, 9, 5, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout.addLayout(self.verticalLayout_5, 9, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_central)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 2, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout.addLayout(self.verticalLayout_6, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_central)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 2, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_3 = QtWidgets.QLabel(self.widget_central)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_16.addWidget(self.label_3)
        self.listWidget = QtWidgets.QListWidget(self.widget_central)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_16.addWidget(self.listWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_16)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_central)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_18.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_central)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_18.addWidget(self.pushButton_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_18)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_7, 6, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.widget_central)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_central)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_12.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.widget_central)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_12.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_central)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_12.addWidget(self.lineEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_central)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_central)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout.addLayout(self.verticalLayout, 6, 2, 1, 1)
        self.vertical_layout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.widget_central)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1014, 21))
        self.menu_bar.setObjectName("menu_bar")
        MainWindow.setMenuBar(self.menu_bar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Демонстрация Qt5"))
        self.pushButton_2.setText(_translate("MainWindow", "Загрузитьиз файла график"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить в файл график"))
        self.label_3.setText(_translate("MainWindow", "Города"))
        self.pushButton_3.setText(_translate("MainWindow", "Зaгрузить из файла города"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить в файл города"))
        self.label.setText(_translate("MainWindow", "Итерации"))
        self.label_2.setText(_translate("MainWindow", "Муравьи"))
        self.pushButton_6.setText(_translate("MainWindow", "Рассчет по обычному"))
        self.pushButton_5.setText(_translate("MainWindow", "Рассчет по усовершенствованному"))
