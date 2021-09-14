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

from person_operationlogic import person_operation_class
from thing_managementlogic import thing_managementlogic_class
from depart_safeguardlogic import depart_safeguard_class
from materials_operationlogic import materials_operation_class

logging.basicConfig(filename='ProgramLog.log',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s: ')

class reload_mainWin(QMainWindow,Ui_FirstWindow):

    def __init__(self):
        super(reload_mainWin,self).__init__()
        self.setupUi(self)
        
        #load database
        self.db = QSqlDatabase.addDatabase('QSQLITE',"db2")
        self.db.setDatabaseName('data/all.db')

        #from ini file load init data
        self.cfg = ConfigParser()
        self.cfg.read("config.ini")

        QApplication.setQuitOnLastWindowClosed(False)

        #load action
        self.action_init()

        #load treeWidget
        self.draw_tree()

        #the click fun of treeWidget
        self.treeWidget.clicked.connect(self.treeView_Clicked)

        #show tableWidget
        self.init_showThings()

        #regular back up database
        self.regular_back_up()

        #tray
        self.trayIcon()

    def openDB(self):
        self.db.open()
        if self.db.open() is None:
            QMessageBox.critical(self,"警告","数据库连接失败，请查看数据库配置",QMessageBox.Yes)
            logging.error("数据库连接失败，请查看数据库配置")
        self.query = QSqlQuery(self.db)

    def action_init(self):
        """load action
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
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_3.clicked.connect(self.find_previous)#全局搜索查找上一个
        self.pushButton_4.clicked.connect(self.find_next)#全局搜索查找下一个
        self.pushButton_2.clicked.connect(self.get_expired)#得到当前tabwidgets中的过期物品

    def draw_tree(self):
        """build {key1:[],key2:[]} to produce tree struction.
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

                for y in len(person_list):
                    locals()['v'+str(y)] = QTreeWidgetItem(locals()['v'+str(x)])
                    locals()['v'+str(y)].setText(0,'%s'%person_list[y])
        self.treeWidget.addTopLevelItem(root)
        self.treeWidget.expandAll()
       
        self.db.close()

    def treeView_Clicked(self,index):
        """fun of click tree
        """
        print("左侧树点击的位置：%s"%index.text(0))
        self.openDB()
        item = self.treeWidget.currentItem()
        self.query.exec_("""SELECT laobao_person.name,laobao_card.name_things,
                        laobao_card.start_date,laobao_card.end_date,laobao_card.period 
                        from laobao_card,laobao_person 
                        where laobao_card.id_person=laobao_person.id_person 
                        and laobao_person.name = '%s'"""%(item.text(0)))
        if self.query.next():
            for n in range(5):
                newItem = QTableWidgetItem(str(self.query.value(n)))
                self.treeWidget.setCellWidget(i,n,newItem)
        else:
            self.query.exec_("""SELECT laobao_person.name,laobao_card.name_things,
                        laobao_card.start_date,laobao_card.end_date,laobao_card.period 
                        from laobao_card,laobao_person 
                        where laobao_card.id_person=laobao_person.id_person 
                        and laobao_person.depart = '%s'"""%(item.text(0)))
            i = 0 #row
            while (self.query.next()):
                for n in range(5):
                    newItem = QTableWidgetItem(str(self.query.value(n)))
                    self.treeWidget.setCellWidget(i,n,newItem)
                i += 1
        self.treeWidget.show()
        self.db.close()
    
    def reFresh(self):
        #用于再次刷新程序。
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
        #update software
        pass

    def find_thing(self):
        #glocal search in tablewidgets
        try:
            self.fined_item = self.treeWidget.findItems(self.lineEdit.text(),QtCore.Qt.MatchContains)#call glocal var to be used by find_thing find_previous and find_next
            item = self.fined_item[0]
            item.setSelected(True)
            row = item.row()
            self.treeWidget.verticalScrollBar().setSliderPosition(row)
        except:
            pass
    
    def find_previous(self):
        pass

    def find_next(self):
        pass

    def materials_operation(self):
        self.materials_operationForm = materials_operation_class()
        self.materials_operationForm.setWindowModality(Qt.ApplicationModal)
        self.materials_operationForm.show()

    def departs_operation(self):
        self.departs_operationForm = depart_safeguard_class()
        self.departs_operationForm.setWindowModality(Qt.ApplicationModal)
        self.departs_operationForm.show()

    def persons_operation(self):
        self.person_operationForm = person_operation_class()
        self.person_operationForm.setWindowModality(Qt.ApplicationModal)
        self.person_operationForm.show()

    def soft_setting(self):
        pass
   
    def materials_management(self):
        self.materials_managementForm = thing_managementlogic_class()
        self.materials_managementForm.setWindowModality(Qt.ApplicationModal)
        self.materials_managementForm.show()

    def operation_log(self):
        pass

    def get_expired(self):
        #get all people whose things are expired

        pass

    def quit_app(self):
        re = QMessageBox.question(self,"提示","退出系统",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if  re == QMessageBox.Yes:
            sys.exit(app.exec_)

    def init_showThings(self):
        self.openDB()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.showYaopin.setColumnWidth(0, 50)
        self.showYaopin.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.showYaopin.setHorizontalHeaderLabels(["姓名","物品名称","领用日期","过期日期","使用周期"])
        self.showYaopin.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置表格自适应
        self.query.exec_("""SELECT laobao_person.name,laobao_card.name_things,laobao_card.start_date,
                            laobao_card.end_date,laobao_card.period 
                        from laobao_card,laobao_person where laobao_card.id_person=laobao_person.id_person""")
        i = 0 #行数
        while (self.query.next()):
            for n in range(5):
                newItem = QTableWidgetItem(str(self.query.value(n)))
                self.treeWidget.setCellWidget(i,n,newItem)
            i += 1
        self.treeWidget.show()
        self.db.close()

    def trayIcon(self):
        tuopan = QSystemTrayIcon(self)
        tuopan.setIcon(QtGui.QIcon(r"images/cherry.ico"))#加载托盘图片
        tuopan.setToolTip(u"欢迎使用年限劳保管理软件")
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
