from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSql, QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QThread,pyqtSignal
from PyQt5 import QtCore
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
        
        #初始化数据库
        self.db = QSqlDatabase.addDatabase('QSQLITE',"db2")
        self.db.setDatabaseName('data/all.db')

        #从ini文件加载初始数据
        self.cfg = ConfigParser()
        self.cfg.read("config.ini")

        #加载按钮动作
        self.action_init()

        #初始化treeWidget和tableWidget
        self.draw_tree()

        #定期备份数据文件
        self.regular_back_up()

    def openDB(self):
        self.db.open()
        if self.db.open() is None:
            QMessageBox.critical(self,"警告","数据库连接失败，请查看数据库配置",QMessageBox.Yes)
            logging.error("数据库连接失败，请查看数据库配置")
        self.query = QSqlQuery(self.db)

    def action_init(self):
        """加载按钮等相关动作
        """
        self.action_10.triggered.connect(self.back_up) #连接备份功能
        self.action_3.triggered.connect(self.about)#软件简介
        self.action_4.triggered.connect(self.update)#软件升级
        self.action_5.triggered.connect(self.materials_operation)#物资信息维护
        self.action_6.triggered.connect(self.departs_operation)#部门信息维护
        self.action_8.triggered.connect(self.persons_operation)#人员基本信息维护
        self.action_9.triggered.connect(self.soft_setting)#设置
        self.action_2.triggered.connect(self.materials_management)#劳保物品管理
        self.action_16.triggered.connect(self.operation_log)#查询操作记录
        self.action_10.triggered.connect(self.back_up)#备份数据库
        self.action_11.triggered.connect(self.reFresh)#刷新
        self.action_15.triggered.connect(self.quit_app)#离开功能
    
        self.pushButton.clicked.connect(self.find_thing)#全局搜索
        self.pushButton_2.clicked.connect(self.get_expired)#得到当前tabwidgets中的过期物品

    def get_tree_node(self):
        self.openDB()

        self.db.close()
        pass

    def draw_tree(self):
        """通过构建{key1:[],key2:[]}的结构，生成树的结构。
        """
        self.openDB()
        tree_dict = { }
        self.treeWidget.setHeaderLabels(['部门'])
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0,'华电龙口发电股份有限公司')
        self.query.exec_("SELECT depart,name from laobao_person")
        while (self.query.next()):
            if not self.query.value(0) in tree_dict.keys():
                tree_dict['%s'%self.query.value(0)] = [self.query.value(1)]
            else:
                tree_dict['%s'%self.query.value(0)].append(self.query.value(1))
        #此处动态生产节点
        for depart_node,person_list in tree_dict.items():
            for x in len(tree_dict.keys()):
                locals()['v'+str(x)] = QTreeWidgetItem(root)
                locals()['v'+str(x)].setText(0,"%s"%depart_node)

                for person_node in person_list:
                    for y in len(person_list):
                        locals()['v'+str(y)] = QTreeWidgetItem(locals()['v'+str(x)])
                        locals()['v'+str(y)].setText(0,'%s'%person_list[y])
        self.treeWidget.addTopLevelItem(root)
        self.treeWidget.expandAll()
       
        self.db.close()

    def treeView_Clicked(self,qmodelindex):
        """点击树，产生一些动作。
        """
        item = self.treeWidget().currentItem()
        print("%s"%item.text(0))


    def reFresh(self):
        pass



    def regular_back_up(self):
        if datetime.datetime.now().weekday() == 4:
            self.back_up()

    def back_up(self):
        try:
            dir = r'C:\wuzi'
            file = r'C:\wuzi\%s.zip'%time.strftime("%Y-%m-%d",time.localtime())
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

    def find_thing(self):
        #当前tablewidgets中全局搜索
        text = self.lineEdit.text()

        pass

    def materials_operation(self):
        pass

    def departs_operation(self):
        pass

    def persons_operation(self):
        pass

    def soft_setting(self):
        pass
   
    def materials_management(self):
        pass
    
    def operation_log(self):
        pass

    def get_expired(self):
        pass

    def quit_app(self):
        re = QMessageBox.question(self,"提示","退出系统",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if  re == QMessageBox.Yes:
            sys.exit(app.exec_)

    def showThings(self):
        self.openDB()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.showYaopin.setColumnWidth(0, 50)
        self.showYaopin.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.showYaopin.setHorizontalHeaderLabels(["姓名","物品名称","领用日期","过期日期","使用周期"])
        self.showYaopin.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格自适应

        pass

    def tryIcon(self):
        tuopan = QSystemTrayIcon(self)
        tuopan.setIcon(QtGui.QIcon(r"images/    .ico"))#加载托盘图片
        tuopan.setToolTip(u"欢迎使用劳保管理软件")
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
