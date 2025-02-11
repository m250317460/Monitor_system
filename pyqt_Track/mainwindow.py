# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 764)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.video_panel = QtWidgets.QLabel(self.centralwidget)
        self.video_panel.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);\n"
"")
        self.video_panel.setAlignment(QtCore.Qt.AlignCenter)
        self.video_panel.setObjectName("video_panel")
        self.verticalLayout.addWidget(self.video_panel)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttons = QtWidgets.QWidget(self.centralwidget)
        self.buttons.setStyleSheet("#buttons{\n"
"background-color: rgb(221, 221, 221);\n"
"}")
        self.buttons.setObjectName("buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open = QtWidgets.QPushButton(self.buttons)
        self.open.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.open.setFont(font)
        self.open.setStyleSheet("")
        self.open.setObjectName("open")
        self.horizontalLayout.addWidget(self.open)
        self.play_pause = QtWidgets.QPushButton(self.buttons)
        self.play_pause.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.play_pause.setFont(font)
        self.play_pause.setObjectName("play_pause")
        self.horizontalLayout.addWidget(self.play_pause)
        self.setroi = QtWidgets.QPushButton(self.buttons)
        self.setroi.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.setroi.setFont(font)
        self.setroi.setObjectName("setroi")
        self.horizontalLayout.addWidget(self.setroi)
        self.isdetect = QtWidgets.QCheckBox(self.buttons)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.isdetect.setFont(font)
        self.isdetect.setStyleSheet("background: transparent;")
        self.isdetect.setTristate(False)
        self.isdetect.setObjectName("isdetect")
        self.horizontalLayout.addWidget(self.isdetect)
        self.istrack = QtWidgets.QCheckBox(self.buttons)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.istrack.setFont(font)
        self.istrack.setStyleSheet("background: transparent;")
        self.istrack.setObjectName("istrack")
        self.horizontalLayout.addWidget(self.istrack)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.buttons)
        self.verticalLayout_2.setStretch(0, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.open.clicked.connect(MainWindow.SelectVideo)
        self.play_pause.clicked.connect(MainWindow.PlayorPause)
        self.isdetect.stateChanged['int'].connect(lambda :MainWindow.Detect(self.isdetect.isChecked()))
        self.istrack.stateChanged['int'].connect(lambda :MainWindow.Track(self.istrack.isChecked()))
        # self.isdetect.stateChanged['int'].connect(MainWindow.Detect)
        # self.istrack.stateChanged['int'].connect(MainWindow.Detect)
        self.setroi.clicked.connect(MainWindow.SetROIArea)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.video_panel.setText(_translate("MainWindow", "视频播放区域"))
        self.open.setText(_translate("MainWindow", "选择文件"))
        self.play_pause.setText(_translate("MainWindow", "暂停"))
        self.setroi.setText(_translate("MainWindow", "设置区域"))
        self.isdetect.setText(_translate("MainWindow", "目标检测"))
        self.istrack.setText(_translate("MainWindow", "目标跟踪"))
