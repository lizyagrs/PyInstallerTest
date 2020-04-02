import sys
#导入界面类的Ui_Form
from PyQt5 import sip
from os import *
from GDALTest import ReadVectorFile
from RasterBand import Ui_Form
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import *
import RasterIO_TIFProcess

#C:\Users\lenove\Desktop\PyInstallerTest目录中
# #执行pyinstaller -F -w RasterBandDo.py命令
# pyinstaller -w RasterBandDo.py
#新建RasterBandForm类，继承Ui_Form，继承了窗体类，可以继承界面上的所有控件
class RasterBandForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        #继承Ui_Form
        super(RasterBandForm, self).__init__()  #初始化父类
        self.setupUi(self)

        #绑定确定按钮事件
        self.btn_ok.clicked.connect( self.func_btn_ok)
        #绑定输入数据路径选择按钮事件
        self.btn_DataInput.clicked.connect(self.func_btn_datainput)

    #输入目录选择按钮事件
    def func_btn_datainput(self):
        get_filename_path, ok = \
            QFileDialog.getOpenFileName(self,"选取单个文件",
                                        "D:\GitHub\PyGeoSpatialStudy\RasterData",
                                        "All Files (*);;TIF Files (*.tif)")
        if ok:
            self.txt_DataInput.setText(str(get_filename_path))


    def closeEvent(self, QCloseEvent):
        #两个按钮是否， 默认No则关闭这个提示框
        res=QMessageBox.question(self,'消息','是否关闭这个窗口？',
                                 QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if res==QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

            #确定按钮事件函数实现
    def func_btn_ok(self):
        print('ok')
        Input_path = self.txt_DataInput.toPlainText()
        print("Input_path:::"+Input_path)
        #判断输入路径不为空
        if Input_path:
            #获取界面上的输入路径参数
            print("to do:::")
            #plotTest()
            #ReadVectorFile(Input_path)
            RasterIO_TIFProcess.showTiFF(Input_path)
            msg_box = QMessageBox(QMessageBox.Warning, "Alert", Input_path+"打开成功!")
            msg_box.exec_()

        else:
            msg_box = QMessageBox(QMessageBox.Warning, "Alert", "请选择输入路径!")
            msg_box.exec_()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    #指定弹出窗体
    RBshow=RasterBandForm()
    RBshow.show()
    sys.exit(app.exec_())
