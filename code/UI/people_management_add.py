# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '人员基本信息维护-新增人员.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 486)
        Form.setMinimumSize(QtCore.QSize(537, 486))
        Form.setMaximumSize(QtCore.QSize(537, 486))
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(80, 0))
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.add_people_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.add_people_name_lineEdit.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.add_people_name_lineEdit.setFont(font)
        self.add_people_name_lineEdit.setObjectName("add_people_name_lineEdit")
        self.horizontalLayout.addWidget(self.add_people_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.add_people_depart_comboBox = QtWidgets.QComboBox(Form)
        self.add_people_depart_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.add_people_depart_comboBox.setFont(font)
        self.add_people_depart_comboBox.setObjectName("add_people_depart_comboBox")
        self.horizontalLayout_2.addWidget(self.add_people_depart_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.add_people_sex_comboBox = QtWidgets.QComboBox(Form)
        self.add_people_sex_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.add_people_sex_comboBox.setFont(font)
        self.add_people_sex_comboBox.setObjectName("add_people_sex_comboBox")
        self.add_people_sex_comboBox.addItem("")
        self.add_people_sex_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.add_people_sex_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.add_people_standard_comboBox = QtWidgets.QComboBox(Form)
        self.add_people_standard_comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.add_people_standard_comboBox.setFont(font)
        self.add_people_standard_comboBox.setObjectName("add_people_standard_comboBox")
        self.horizontalLayout_4.addWidget(self.add_people_standard_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.add_people_ok_pushButton = QtWidgets.QPushButton(Form)
        self.add_people_ok_pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.add_people_ok_pushButton.setFont(font)
        self.add_people_ok_pushButton.setObjectName("add_people_ok_pushButton")
        self.horizontalLayout_5.addWidget(self.add_people_ok_pushButton)
        self.add_people_no_pushButton = QtWidgets.QPushButton(Form)
        self.add_people_no_pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(12)
        self.add_people_no_pushButton.setFont(font)
        self.add_people_no_pushButton.setObjectName("add_people_no_pushButton")
        self.horizontalLayout_5.addWidget(self.add_people_no_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "新增人员"))
        self.label.setText(_translate("Form", "姓名"))
        self.label_2.setText(_translate("Form", "部门"))
        self.label_3.setText(_translate("Form", "性别"))
        self.add_people_sex_comboBox.setItemText(0, _translate("Form", "男"))
        self.add_people_sex_comboBox.setItemText(1, _translate("Form", "女"))
        self.label_4.setText(_translate("Form", "劳保标准"))
        self.add_people_ok_pushButton.setText(_translate("Form", "确认"))
        self.add_people_no_pushButton.setText(_translate("Form", "取消"))
