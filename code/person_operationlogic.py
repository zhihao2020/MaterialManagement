from PyQt5.QtWidgets import *
import sqlite3
import sys

from UI.people_management import Ui_MainWindow

class person_operation_class(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(person_operation_class,self).__init__()
        self.setupUi(self)
        self.action_init()

        self.draw_tree()

        #the click fun of treeWidget
        self.treeWidget.clicked.connect(self.show_get_history)

    def action_init(self):
        self.add_people.triggered.connect(self.add_peoplefun)
        self.delete_people.triggered.connect(self.delete_peoplefun)
        self.refresh_action.triggered.connect(self.refresh_actionfun)
        
        self.pushButton.clicked.connect(self.change_people)
        self.pushButton_2.clicked.connect(self.publish)

    def draw_tree(self):
        """build {key1:[],key2:[]} to produce tree struction.
        """
        tree_dict = { }
        self.treeWidget.setHeaderLabels(['部门'])
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0,'华电龙口发电股份有限公司')
        try:
            conn = sqlite3.connect("data/all.db")
            cursor = conn.cursor()
            cursor.execute("SELECT depart,name from laobao_person")
            tempContainer = cursor.fetchall()
            for temp in tempContainer:
                if temp[0] in tree_dict.keys():
                    tree_dict['%s'%temp[0]] = [temp[1]]
                else:
                    tree_dict['%s'%temp[0]].append(temp[1])
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
        except:
            QMessageBox.critical(self,"警告","错误代码101",QMessageBox.Yes)
        finally:
            conn.close()
            
    def show_get_history(self,index):
        print("左侧树点击的位置：%s"%index.text(0))
        pass

    def publish(self):
        pass
    
    def change_people(self):
        #tempdata.execute("update 顾客 set 药品可用金额=%s where 姓名='%s'" % (shangpin, lis[0]))
        
        
        pass
    
    def add_peoplefun(self):
        pass
    
    def delete_peoplefun(self):
        self.treeWidget.currentItem().text(0)
        pass

    def refresh_actionfun(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myMin = person_operation_class()
    myMin.show()
    sys.exit(app.exec_)
