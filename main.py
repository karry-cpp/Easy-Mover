# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    curr_path = os.getcwd()
    srcp = ''
    count, ind = 0, 0
    sep = '==============================='
    all_files = ''
    pics, vids, mp3, docs = '','','',''
    psrc, vsrc, msrc, dsrc = 'D:\\pyPhotos','D:\\pyVideos','D:\\pyMusic','D:\\pyDocuments'    

    for i in curr_path:
        if i == '\\':
            count += 1
            pass
        if count == 3:
            srcp = curr_path[0:ind] + '\\Downloads'
            break
        ind += 1

    file_loc = srcp[:-10] + '\\AppData\\Roaming\\One-Click-Mover\\move_log.txt'

    if os.path.exists(file_loc):
            with open(file_loc, 'r') as file:
                lines = file.readlines()
                psrc = lines[0][0:-1]
                vsrc = lines[1][0:-1]
                msrc = lines[2][0:-1]
                dsrc = lines[3][0:-1]
                srcp = lines[4]
                pass
    else:
        with open(file_loc, 'w') as file:                
            file.write(psrc + '\n')
            file.write(vsrc + '\n')
            file.write(msrc + '\n')
            file.write(dsrc + '\n')                
            file.write(srcp)
            pass

    srcp = srcp.strip()
        
    for file in os.listdir(srcp):
        if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
            pics += file + '\n\n'                    

        if file.endswith('.mp4') or file.endswith('.mkv'):
           vids += file + '\n\n'    

        if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.m4a'):
            mp3 += file + '\n\n'          
                     
        if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.pptx') or file.endswith('.doc') or file.endswith('.ppt'):
            docs += file + '\n\n'
    
    
    all_files += '\n\tPhotos\n\n' + pics + sep + '\n'        
    all_files += '\n\tVideos\n\n' + vids + sep + '\n'        
    all_files += '\n\tMusic\n\n' + mp3 + sep + '\n'        
    all_files += '\n\tDocuments\n\n' + docs + sep + '\n'
    
    del curr_path, count, ind

    def source_changed(self):
        self.all_files = ''
        lines = [self.psrc + '\n', self.vsrc + '\n', self.msrc + '\n', self.dsrc + '\n', self.srcp]
        self.docs, self.mp3, self.pics, self.vids = '','','',''
        txt = self.textEdit_2.toPlainText()
        lines = [self.psrc + '\n', self.vsrc + '\n', self.msrc + '\n', self.dsrc + '\n', self.srcp]
        if os.path.exists(self.file_loc):
            with open(self.file_loc, 'r') as file:
                line = file.readlines()
                if len(line) == 5:
                    lines = line
                lines[4] = self.textEdit_2.toPlainText() + '\n'
                pass
        else:
            with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])
        with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])
        
        try:
            for file in os.listdir(txt):
                if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                    self.pics += file + '\n\n'                    
                   

                if file.endswith('.mp4') or file.endswith('.mkv'):
                    self.vids += file + '\n\n'            
                    

                if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.m4a'):
                    self.mp3 += file + '\n\n'                    
                    
                            
                if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.pptx') or file.endswith('.doc'):
                    self.docs += file + '\n\n'
                    
        except:
            pass
        
        self.all_files += '\n\tPhotos\n\n' + self.pics + self.sep + '\n'        
        self.all_files += '\n\tVideos\n\n' + self.vids + self.sep + '\n'        
        self.all_files += '\n\tMusic\n\n' + self.mp3 + self.sep + '\n'        
        self.all_files += '\n\tDocuments\n\n' + self.docs + self.sep + '\n'

        self.textEdit.clear()
        self.textEdit.setPlainText(self.all_files)
    
    
    def clicked(self):
        pic_src = self.textEdit_3.toPlainText()
        vid_src = self.textEdit_4.toPlainText()
        mp3_src = self.textEdit_5.toPlainText()
        doc_src = self.textEdit_6.toPlainText()
        src = self.textEdit_2.toPlainText()
        if os.path.exists(pic_src) == False:
            os.mkdir(pic_src)
        if os.path.exists(vid_src) == False:
            os.mkdir(vid_src)
        if os.path.exists(mp3_src) == False:
            os.mkdir(mp3_src)
        if os.path.exists(doc_src) == False:
            os.mkdir(doc_src)
        
        
        for file in os.listdir(src):
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):                
                comm = 'move "' + src + '\\' + file + '" ' + '"' + pic_src + '"'
                os.system(comm)
                

            if file.endswith('.mp4') or file.endswith('.mkv'):
                comm = 'move "' + src + '\\' + file + '" ' + '"' + vid_src + '"'
                os.system(comm)
                

            if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.m4a'):
                comm = 'move "' + src + '\\' + file + '" ' + '"' + mp3_src + '"'
                os.system(comm)
               

            if file.endswith('.pdf') or file.endswith('.docx') or file.endswith('.pptx') or file.endswith('.doc'):
                comm = 'move "' + src + '\\' + file + '" ' + '"' + doc_src + '"'
                os.system(comm)
                

        self.textEdit.setPlainText('\n\n\n\t  Moved\n\n\n' + self.sep + '\n\n'+ self.all_files + self.sep + '\n\n')
        pass
    
    def pic_changed(self):
        lines = [self.psrc + '\n', self.vsrc + '\n', self.msrc + '\n', self.dsrc + '\n', self.srcp]
        if os.path.exists(self.file_loc):
            with open(self.file_loc, 'r') as file:
                line = file.readlines()
                if len(line) == 5:
                    lines = line
                lines[0] = self.textEdit_3.toPlainText() + '\n'
                pass
        else:
            with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])
        with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])

    def vid_changed(self):
        lines = [self.psrc + '\n', self.vsrc + '\n', self.msrc + '\n', self.dsrc + '\n', self.srcp]
        if os.path.exists(self.file_loc):
            with open(self.file_loc, 'r') as file:
                line = file.readlines()
                if len(line) == 5:
                    lines = line
                lines[1] = self.textEdit_4.toPlainText() + '\n'
                pass
        else:
            with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])
        with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])


    def mp3_changed(self):
        lines = [self.psrc + '\n', self.vsrc + '\n', self.msrc + '\n', self.dsrc + '\n', self.srcp]
        if os.path.exists(self.file_loc):
            with open(self.file_loc, 'r') as file:
                line = file.readlines()
                if len(line) == 5:
                    lines = line
                lines[2] = self.textEdit_5.toPlainText() + '\n'
                pass
        else:
            with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])
                pass
        with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])
        pass

    def doc_changed(self):
        lines = [self.psrc + '\n', self.vsrc + '\n', self.msrc + '\n', self.dsrc + '\n', self.srcp]
        if os.path.exists(self.file_loc):
            with open(self.file_loc, 'r') as file:
                line = file.readlines()
                if len(line) == 5:
                    lines = line
                lines[3] = self.textEdit_6.toPlainText() + '\n'
                pass
        else:
            with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])
        with open(self.file_loc, 'w') as file:
                file.write(lines[0])
                file.write(lines[1] )
                file.write(lines[2] )
                file.write(lines[3])
                file.write(lines[4])
        pass


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(13, 80, 321, 491))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlainText(self.all_files)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 100, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 170, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(340, 260, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 350, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(360, 440, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 510, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(490, 20, 291, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setPlainText(self.srcp)
        self.textEdit_2.textChanged.connect(self.source_changed)
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(500, 170, 291, 51))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setPlainText(self.psrc)
        self.textEdit_3.textChanged.connect(self.pic_changed)
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(500, 260, 291, 51))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setPlainText(self.vsrc)
        self.textEdit_4.textChanged.connect(self.vid_changed)
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(500, 350, 291, 51))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setPlainText(self.msrc)
        self.textEdit_5.textChanged.connect(self.mp3_changed)
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(500, 440, 291, 51))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_6.setPlainText(self.dsrc)
        self.textEdit_6.textChanged.connect(self.doc_changed)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "One Click Move"))
        self.label.setText(_translate("MainWindow", "Files 🗃️"))
        self.label_2.setText(_translate("MainWindow", "Source 📁"))
        self.label_3.setText(_translate("MainWindow", "Destination 📂"))
        self.label_4.setText(_translate("MainWindow", "Photos 📸"))
        self.label_5.setText(_translate("MainWindow", "Videos 🎬"))
        self.label_6.setText(_translate("MainWindow", "Music 🎶"))
        self.label_7.setText(_translate("MainWindow", "Docs 📄"))
        self.pushButton.setText(_translate("MainWindow", "Start Moving"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
