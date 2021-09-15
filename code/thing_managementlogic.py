from PyQt5.QtWidgets import *

import sqlite3
import sys

from UI.thing_management import Ui_MainWindow

class thing_managementlogic_class(QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(thing_managementlogic_class,self).__init__()
        self.setupUi(self)
    
