import sys,json,time
import cPickle as pickle



from PySide import QtGui,QtCore





#Function to create required options directory for preference files

      
class frame(QtGui.QMainWindow):
      def __init__(self):
            super(frame,self).__init__()
            self.simple()
      def simple(self):
            new=QtGui.QAction(QtGui.QIcon('exit.png'),'&New',self)
            new.setShortcut('Ctrl+N')
            new.triggered.connect(newwindow)
            op=QtGui.QAction(QtGui.QIcon('exit.png'),'&Open',self)
            op.setShortcut('Ctrl+O')
            op.triggered.connect(self.openfile)
            exita=QtGui.QAction(QtGui.QIcon('exit.png'),'&Exit',self)
            exita.setShortcut('Shift+X')
            
            exita.triggered.connect(self.close)
            self.save=QtGui.QAction(QtGui.QIcon('exit.png'),'&Save As',self)
            self.save.setShortcut('Shift+S')
            self.save.triggered.connect(self.savefile)
            cut=QtGui.QAction(QtGui.QIcon('exit.png'),'&Cut',self)
            cut.setShortcut('Ctrl+X')
            cut.triggered.connect(self.cut)
            copy=QtGui.QAction(QtGui.QIcon('exit.png'),'&Copy',self)
            copy.setShortcut('Ctrl+C')
            copy.triggered.connect(self.copy)
            paste=QtGui.QAction(QtGui.QIcon('exit.png'),'&Paste',self)
            paste.setShortcut('Ctrl+V')
            paste.triggered.connect(self.pasteText)
            font=QtGui.QAction(QtGui.QIcon('exit.png'),'&Font',self)
            font.setShortcut('Shift+F')
            font.triggered.connect(self.fontEdit)
            self.textEdit=QtGui.QTextEdit()
            self.textEdit.setCurrentFont(QtGui.QFont('Arial',13))
            self.setCentralWidget(self.textEdit)
            save=QtGui.QAction(QtGui.QIcon('exit.png'),'&Save',self)
            save.setShortcut('Ctrl+S')
            save.triggered.connect(self.save2)
            select=QtGui.QAction(QtGui.QIcon('exit.png'),'&Select All',self)
            select.setShortcut('Ctrl+A')
            select.triggered.connect(self.select)
            undo=QtGui.QAction(QtGui.QIcon('exit.png'),'&Undo',self)
            undo.setShortcut('Ctrl+Z')
            undo.triggered.connect(self.undo)
            date=QtGui.QAction(QtGui.QIcon('exit.png'),'&Insert Date and Time',self)
            date.triggered.connect(self.addTime)
            redo=QtGui.QAction(QtGui.QIcon('exit.png'),'&Redo',self)
            redo.setShortcut('Ctrl+Y')
            redo.triggered.connect(self.redo)
            length=QtGui.QAction(QtGui.QIcon('exit.png'),'&Character Count',self)
            length.triggered.connect(self.count)
            printoption=QtGui.QAction(QtGui.QIcon('exit.png'),'&Print',self)
            printoption.setShortcut('Ctrl+P')
            printoption.triggered.connect(self.onPrint)
            printpreview=QtGui.QAction(QtGui.QIcon('exit.png'),'&Print Preview',self)
            printpreview.triggered.connect(self.onPrintPreview)
            about=QtGui.QAction(QtGui.QIcon('exit.png'),'&About',self)
            about.triggered.connect(self.showAbout)
            
            menu=self.menuBar()
            filemenu=menu.addMenu('&File')
            filemenu.addAction(new)
            filemenu.addAction(op)
            filemenu.addAction(save)
            filemenu.addAction(self.save)
            filemenu.addSeparator()
            filemenu.addAction(printoption)
            filemenu.addAction(printpreview)
            filemenu.addAction(exita)
            
            editmenu=menu.addMenu('&Edit')
            editmenu.addAction(undo)
            editmenu.addAction(redo)
            editmenu.addSeparator()
            editmenu.addAction(cut)
            editmenu.addAction(copy)
            editmenu.addAction(paste)
            editmenu.addAction(select)
            viewmenu=menu.addMenu('&View')
            viewmenu.addAction(font)
            toolsmenu=menu.addMenu('&Tools')
            toolsmenu.addAction(length)
            toolsmenu.addAction(date)
            helpmenu=menu.addMenu('&Help')
            helpmenu.addAction(about)
            
            self.setGeometry(200,200,550,450)
            self.setWindowIcon(QtGui.QIcon('icon.png')) 
            self.setWindowTitle("Notepad By Pradd")
            self.show()
            
      def showAbout(self):
            textstring='''<font size="5" family="Segoe UI" >Created By Pradipta using Python and Qt.<br>
Based on the PySide Qt Wrapper for Python.<br>
Running on Python {0} on Windows.<br><br><br><br>
Version 3.0 <br>
Copyright 2014 Pradipta and Akshat</font>'''.format(str(sys.version)[:5:])
            self.help=QtGui.QWidget()
            self.help.setGeometry(200,200,400,350)
            self.help.setWindowIcon(QtGui.QIcon('icon.png')) 
            self.help.setFixedSize(400,350)
            color = self.help.palette()
            color.setColor(self.help.backgroundRole(),QtCore.Qt.white)
            self.help.setPalette(color)
            self.help.setWindowTitle("Notepad By Pradd")
            heading=QtGui.QLabel('<font family="Segoe UI" size="28"  >Notepad By Pradd </font>',self.help)
            heading.move(100,20)
            text=QtGui.QLabel(textstring,self.help)
            text.move(30,100)
            self.help.show()
      def addTime(self):
        self.textEdit.insertPlainText(time.asctime())
      def count(self):
            x= json.dumps(self.textEdit.toPlainText())
            sub = "\\n";
            lines=int(x.count(sub, 4, 40)) +1
            x.replace('\n','')
            print json.loads(x)
            d=lines - 1
            characters=len(json.loads(x)) -  d
            doc="Your document has {0} characters in {1} lines".format(str(characters),str(lines))
            ret= QtGui.QMessageBox.information(self, 'Character Count',doc, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
      def onPrint(self):
        """
        Create and show the print dialog
        """
        dialog = QtGui.QPrintDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            doc = self.textEdit.document()
            doc.print_(dialog.printer())
      def undo(self):
            self.textEdit.undo()
      def redo(self):
            self.textEdit.redo()
      def select(self):
            self.textEdit.selectAll()
      def cut(self):
            self.textEdit.cut()
      def copy(self):
            self.textEdit.copy()
      def onPrintPreview(self):
            """
            Create and show a print preview window"""
            dialog = QtGui.QPrintPreviewDialog()
            dialog.paintRequested.connect(self.textEdit.print_)
            dialog.exec_()
      def save2(self):
            try:
                  with open(self.location,'w') as f:
                        f.write(self.textEdit.toPlainText())
            except:
                  self.savefile()
      def fontEdit(self):
            font = QtGui.QFontDialog.getFont()
            
            if font[1]:
                  
                  x= str(font[0]).split(')')[0].split('(')[-1]
                  
                  
                  self.textEdit.setCurrentFont(font[0])
      def openfile(self):
            try:
                  filename=QtGui.QFileDialog.getOpenFileName(self,"Open File",'C:/',"Text Files (*.txt)")
                  self.location=filename[0]
            
                  with open(filename[0],'r') as f:
                        data=f.read()
                  self.setWindowTitle("Notepad By Pradd- {0}".format(self.location))
                  self.textEdit.setText(data)
            except:
                  pass
      def savefile(self):
            try:
                  files_types = "Text File (*.txt);;HTML Files (*.html);;YAML (*.yml)"
                  file = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '', files_types)
                  self.location=file[0]
                  with open(file[0],'w') as f:
                        f.write(self.textEdit.toPlainText())
                  self.setWindowTitle("Notepad By Pradd- {0}".format(self.location))
            except:
                  pass
      def pasteText(self):
            self.textEdit.paste()
      def closeEvent(self,event):
            reply=QtGui.QMessageBox.question(self,'Quit','Are you sure you want to exit?',QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,QtGui.QMessageBox.No)
            if reply==QtGui.QMessageBox.Yes:
                  event.accept()
            else:
                  event.ignore()



    
def main():
      
      app=QtGui.QApplication(sys.argv)
      ex=frame()
      
      sys.exit(app.exec_())
def newwindow():
  pass
      
      
if __name__=='__main__':
      main()
