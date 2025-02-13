# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1195, 822)
        MainWindow.setMaximumSize(QtCore.QSize(1666665, 166666))
        self.gridLayout_2 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.openx_vtd_change = QtWidgets.QPushButton(MainWindow)
        self.openx_vtd_change.setMinimumSize(QtCore.QSize(251, 41))
        self.openx_vtd_change.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(190, 221, 255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(170, 200, 230);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(138, 164, 193);\n"
"border-radius:10px;\n"
"}")
        self.openx_vtd_change.setDefault(False)
        self.openx_vtd_change.setFlat(False)
        self.openx_vtd_change.setObjectName("openx_vtd_change")
        self.verticalLayout.addWidget(self.openx_vtd_change)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.openx_carmaker_change = QtWidgets.QPushButton(MainWindow)
        self.openx_carmaker_change.setMinimumSize(QtCore.QSize(251, 41))
        self.openx_carmaker_change.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(190, 221, 255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(170, 200, 230);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(138, 164, 193);\n"
"border-radius:10px;\n"
"}")
        self.openx_carmaker_change.setObjectName("openx_carmaker_change")
        self.verticalLayout.addWidget(self.openx_carmaker_change)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        self.openx_prescan_change = QtWidgets.QPushButton(MainWindow)
        self.openx_prescan_change.setMinimumSize(QtCore.QSize(251, 41))
        self.openx_prescan_change.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(190, 221, 255);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(170, 200, 230);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(138, 164, 193);\n"
"border-radius:10px;\n"
"}")
        self.openx_prescan_change.setObjectName("openx_prescan_change")
        self.verticalLayout.addWidget(self.openx_prescan_change)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem12)
        self.select_software_dir = QtWidgets.QPushButton(MainWindow)
        self.select_software_dir.setMinimumSize(QtCore.QSize(241, 41))
        self.select_software_dir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_software_dir.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(255, 199, 125);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(230, 175, 80);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(193, 125, 17);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.select_software_dir.setObjectName("select_software_dir")
        self.verticalLayout_2.addWidget(self.select_software_dir)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem14)
        self.open_software = QtWidgets.QPushButton(MainWindow)
        self.open_software.setMinimumSize(QtCore.QSize(241, 41))
        self.open_software.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.open_software.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(255, 199, 125);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(230, 175, 80);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(85, 87, 83);\n"
"background-color: rgb(193, 125, 17);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.open_software.setObjectName("open_software")
        self.verticalLayout_2.addWidget(self.open_software)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem16)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem18)
        self.frame_3 = QtWidgets.QFrame(MainWindow)
        self.frame_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(341, 211))
        self.frame_3.setMaximumSize(QtCore.QSize(341, 211))
        self.frame_3.setSizeIncrement(QtCore.QSize(8, 5))
        self.frame_3.setBaseSize(QtCore.QSize(8, 5))
        self.frame_3.setStyleSheet("border-image: url(:/DSXW/DSXW.png);\n"
"border-image: url(:/DSXW/DSXW.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem19)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 2, 1, 2)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem20, 2, 1, 2, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem21, 2, 2, 2, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.case_down = QtWidgets.QPushButton(MainWindow)
        self.case_down.setMinimumSize(QtCore.QSize(281, 41))
        self.case_down.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(250,250,250);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(211, 215, 207);\n"
"border-radius:10px;\n"
"}")
        self.case_down.setObjectName("case_down")
        self.gridLayout.addWidget(self.case_down, 0, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem22, 0, 1, 1, 1)
        self.report = QtWidgets.QPushButton(MainWindow)
        self.report.setMinimumSize(QtCore.QSize(281, 41))
        self.report.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(250,250,250);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(211, 215, 207);\n"
"border-radius:10px;\n"
"}")
        self.report.setObjectName("report")
        self.gridLayout.addWidget(self.report, 0, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem23, 0, 3, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.range = QtWidgets.QPushButton(MainWindow)
        self.range.setMinimumSize(QtCore.QSize(281, 41))
        self.range.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(250,250,250);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(211, 215, 207);\n"
"border-radius:10px;\n"
"}")
        self.range.setObjectName("range")
        self.verticalLayout_3.addWidget(self.range)
        self.range_zero = QtWidgets.QPushButton(MainWindow)
        self.range_zero.setMinimumSize(QtCore.QSize(281, 41))
        self.range_zero.setStyleSheet("QPushButton{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(250,250,250);\n"
"border-radius:10px\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;}\n"
"QPushButton:pressed{\n"
"border:2px solid rgb(186,186,186);\n"
"background-color: rgb(211, 215, 207);\n"
"border-radius:10px;\n"
"}")
        self.range_zero.setObjectName("range_zero")
        self.verticalLayout_3.addWidget(self.range_zero)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 4, 1, 1)
        self.case_download_show = QtWidgets.QListWidget(MainWindow)
        self.case_download_show.setMinimumSize(QtCore.QSize(0, 331))
        self.case_download_show.setObjectName("case_download_show")
        self.gridLayout.addWidget(self.case_download_show, 1, 0, 1, 1)
        self.report_show = QtWidgets.QListWidget(MainWindow)
        self.report_show.setObjectName("report_show")
        self.gridLayout.addWidget(self.report_show, 1, 2, 1, 1)
        self.range_show = QtWidgets.QListWidget(MainWindow)
        self.range_show.setObjectName("range_show")
        self.gridLayout.addWidget(self.range_show, 1, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 3, 2, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem24, 4, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem25, 4, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem26, 4, 4, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem27, 4, 5, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem28, 5, 2, 1, 2)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem29, 6, 2, 1, 2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenX"))
        self.openx_vtd_change.setText(_translate("MainWindow", "OpenX-VTD格式转换"))
        self.openx_carmaker_change.setText(_translate("MainWindow", "OpenX-CarMaker格式转换"))
        self.openx_prescan_change.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.openx_prescan_change.setText(_translate("MainWindow", "OpenX-Prescan格式转换"))
        self.select_software_dir.setText(_translate("MainWindow", "选择Roadrunner软件目录"))
        self.open_software.setText(_translate("MainWindow", "打开Roadrunner软件"))
        self.case_down.setText(_translate("MainWindow", "案例下载次数统计"))
        self.report.setText(_translate("MainWindow", "测试报告获取"))
        self.range.setText(_translate("MainWindow", "测试里程"))
        self.range_zero.setText(_translate("MainWindow", "总里程清零"))
from window import DSXW_rc
