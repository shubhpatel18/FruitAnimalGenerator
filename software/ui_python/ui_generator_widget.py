# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_xml\ui_generator_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GeneratorWidget(object):
    def setupUi(self, GeneratorWidget):
        GeneratorWidget.setObjectName("GeneratorWidget")
        GeneratorWidget.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(GeneratorWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fruit_label = QtWidgets.QLabel(GeneratorWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.fruit_label.setFont(font)
        self.fruit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fruit_label.setObjectName("fruit_label")
        self.verticalLayout.addWidget(self.fruit_label)
        self.animal_label = QtWidgets.QLabel(GeneratorWidget)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.animal_label.setFont(font)
        self.animal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.animal_label.setObjectName("animal_label")
        self.verticalLayout.addWidget(self.animal_label)
        self.generate_button = QtWidgets.QPushButton(GeneratorWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.generate_button.setFont(font)
        self.generate_button.setObjectName("generate_button")
        self.verticalLayout.addWidget(self.generate_button)

        self.retranslateUi(GeneratorWidget)
        QtCore.QMetaObject.connectSlotsByName(GeneratorWidget)

    def retranslateUi(self, GeneratorWidget):
        _translate = QtCore.QCoreApplication.translate
        GeneratorWidget.setWindowTitle(_translate("GeneratorWidget", "Generate"))
        self.fruit_label.setText(_translate("GeneratorWidget", "Fruit"))
        self.animal_label.setText(_translate("GeneratorWidget", "Animal"))
        self.generate_button.setText(_translate("GeneratorWidget", "Generate"))
