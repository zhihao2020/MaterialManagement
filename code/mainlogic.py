from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSql, QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QThread,pyqtSignal
from PyQt5 import QtCore,QtGui
import sys
import webbrowser
import sqlite3
import time
import datetime
import os
import logging
import requests
import subprocess
import zipfile
from configparser import ConfigParser
from UI.main import Ui_FirstWindow

logging.basicConfig(filename='ProgramLog.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s: ')

class reload_mainWin(QMainWindow,Ui_FirstWindow):

    def __init__(self):
        super(reload_mainWin,self).__init__()
        self.setupUi(self)
        self.data_init()
        
        #初始化数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE',"db2")
        self.db.setDatabaseName('data/all.db')

        #从ini文件加载初始数据
        self.cfg = ConfigParser()
        self.cfg.read("config.ini")

    def action_init(self):
        """加载按钮等相关动作
        """
        self.action_10.triggered.connect(self.back_up) #连接备份功能
        self.action_3.triggered.connect(self.about)
        self.action_4.triggered.connect(self.update)
        self.action_15.triggered.connect(self.quit_app)
    
    def reFresh(self):
        pass

    def openDB(self):
        self.db.open()
        if self.db.open() is None:
            QMessageBox.critical(self,"警告","数据库连接失败，请查看数据库配置",QMessageBox.Yes)
            logging.error("数据库连接失败，请查看数据库配置")
        
        self.query = QSqlQuery(self.db)
    

    def regular_back_up(self):
        if datetime.datetime.now().weekday() == 4:
            self.back_up()

    def back_up(self):
        try:
            dir = ''
            file = ''
            if not os.path.exists(dir):
                os.makedirs(dir)
            newZip = zipfile.ZipFile(file,'w')
            newZip.write('data/all.db')
            
            newZip.write("ProgramLog.log")
        except:
            QMessageBox.warning(self,"警告","备份过程发生错误",QMessageBox)
        else:
            QMessageBox.information(self,"提示","备份完成，请定时备份数据库文件",QMessageBox.Yes)
            logging.info('备份数据文件')
            return True

    def output_csv(self):
        pass
    
    def update(self):
        #升级模块
        pass

    def quit_app(self):
        re = QMessageBox.question(self,"提示","退出系统",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if  re == QMessageBox.Yes:
            sys.exit(app.exec_)

    def showThings(self):
        self.openDB()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.showYaopin.setColumnWidth(0, 50)
        self.showYaopin.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.showYaopin.setHorizontalHeaderLabels([""])
        self.showYaopin.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格自适应

        pass

    def tryIcon(self):
        tuopan = QSystemTrayIcon(self)
        tuopan.setIcon(QtGui.QIcon(r"images/    .ico"))#加载托盘图片
        tuopan.setToolTip(u"欢迎使用医琦软件")
        a1 = QAction('&显示(Show)',self,triggered=self.showNormal)
        a2 = QAction('&退出(Exit)',self,triggered=self.quit_app)  # 直接退出可以用qApp.quit
        tpMenu = QMenu()
        tpMenu.addAction(a1)
        tpMenu.addAction(a2)
        tuopan.setContextMenu(tpMenu)
        tuopan.activated.connect(self.iconActivated)
        tuopan.show()

    def iconActivated(self,reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isMinimized() or not self.isVisible():
                self.showNormal()
                self.activateWindow()
            else:
                self.hide()
        elif reason == QSystemTrayIcon.Trigger:
            pass

    def about(self):
        webbrowser.open_new_tab("http://www.baidu.com")

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myMin = reload_mainWin()
    myMin.show()
    sys.exit(app.exec_)
