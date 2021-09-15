from PyQt5.QtWidgets import *

import sqlite3
import sys

from UI.thing_safeguard import Ui_Form
class materials_operation_class(QMainWindow,Ui_Form):

    def __init__(self):
        super(materials_operation_class,self).__init__()
        self.setupUi(self)
    
    