import sys,json,time,mistune,os
from pypdflite import PDFLite
from PySide import QtGui,QtCore
from syntaxclasses import *
import cPickle as pickle
#Function to create required options directory for preference files

setup="C:/Notepad By Pradd/"
class frame(QtGui.QMainWindow):
      def __init__(self):
            super(frame,self).__init__()
            self.setGUI()
      def FileMenu(self):
        new=QtGui.QAction(QtGui.QIcon('exit.png'),'&New',self)
        new.setShortcut('Ctrl+N')
        new.triggered.connect(self.newwindow)

        op=QtGui.QAction(QtGui.QIcon('exit.png'),'&Open',self)
        op.setShortcut('Ctrl+O')
        op.triggered.connect(self.openfile)

        exita=QtGui.QAction(QtGui.QIcon('exit.png'),'&Exit',self)
        exita.setShortcut('Shift+X')
        exita.triggered.connect(self.close)

        self.save=QtGui.QAction(QtGui.QIcon('exit.png'),'&Save As',self)
        self.save.setShortcut('Shift+S')
        self.save.triggered.connect(self.savefile)

        save=QtGui.QAction(QtGui.QIcon('exit.png'),'&Save',self)
        save.setShortcut('Ctrl+S')
        save.triggered.connect(self.save2)

        printoption=QtGui.QAction(QtGui.QIcon('exit.png'),'&Print',self)
        printoption.setShortcut('Ctrl+P')
        printoption.triggered.connect(self.onPrint)

        printpreview=QtGui.QAction(QtGui.QIcon('exit.png'),'&Print Preview',self)
        printpreview.triggered.connect(self.onPrintPreview)

        filemenu=self.menu.addMenu('&File')
        filemenu.addAction(new)
        filemenu.addAction(op)
        filemenu.addAction(save)
        filemenu.addAction(self.save)
        filemenu.addSeparator()
        filemenu.addAction(printoption)
        filemenu.addAction(printpreview)
        filemenu.addAction(exita)
      
                        
      def EditMenu(self):
        undo=QtGui.QAction(QtGui.QIcon('exit.png'),'&Undo',self)
        undo.setShortcut('Ctrl+Z')
        undo.triggered.connect(self.undo)

        redo=QtGui.QAction(QtGui.QIcon('exit.png'),'&Redo',self)
        redo.setShortcut('Ctrl+Y')
        redo.triggered.connect(self.redo)

        cut=QtGui.QAction(QtGui.QIcon('exit.png'),'&Cut',self)
        cut.setShortcut('Ctrl+X')
        cut.triggered.connect(self.cut)

        copy=QtGui.QAction(QtGui.QIcon('exit.png'),'&Copy',self)
        copy.setShortcut('Ctrl+C')
        copy.triggered.connect(self.copy)

        paste=QtGui.QAction(QtGui.QIcon('exit.png'),'&Paste',self)
        paste.setShortcut('Ctrl+V')
        paste.triggered.connect(self.pasteText)

        select=QtGui.QAction(QtGui.QIcon('exit.png'),'&Select All',self)
        select.setShortcut('Ctrl+A')
        select.triggered.connect(self.select)

        editmenu=self.menu.addMenu('&Edit')
        editmenu.addAction(undo)
        editmenu.addAction(redo)
        editmenu.addSeparator()
        editmenu.addAction(cut)
        editmenu.addAction(copy)
        editmenu.addAction(paste)
        editmenu.addAction(select)

      def ViewMenu(self):
        font=QtGui.QAction(QtGui.QIcon('exit.png'),'&Font',self)
        font.setShortcut('Shift+F')
        font.triggered.connect(self.fontEdit)

        viewmenu=self.menu.addMenu('&View')
        viewmenu.addAction(font)

        syntaxMenu=viewmenu.addMenu('&Syntax Highlighting')
        self.group=QtGui.QActionGroup(self,exclusive=True)
        self.checkdefault=self.group.addAction(QtGui.QAction('&None',self,checkable=True))
        self.checkdefault.setChecked(True)
        syntaxMenu.addAction(self.checkdefault)
        self.checkpython=self.group.addAction(QtGui.QAction('&Python',self,checkable=True))
        syntaxMenu.addAction(self.checkpython)
        self.checkc=self.group.addAction(QtGui.QAction('&C/C++',self,checkable=True))
        syntaxMenu.addAction(self.checkc)
        self.checkhtml=self.group.addAction(QtGui.QAction('&HTML',self,checkable=True))
        syntaxMenu.addAction(self.checkhtml)
        self.checkmkd=self.group.addAction(QtGui.QAction('&Markdown',self,checkable=True))
        syntaxMenu.addAction(self.checkmkd)
        self.checkc.triggered.connect(self.changeHighlightToC)
        self.checkpython.triggered.connect(self.changeHighlightToPython)
        self.checkhtml.triggered.connect(self.changeHighlightToHtml)
        self.checkmkd.triggered.connect(self.changeHighlightToMkd)
        self.checkdefault.triggered.connect(self.removeHighlight)
      def removeHighlight(self):
            self.highlighter=None
      def changeHighlightToHtml(self):
          self.highlighter = HtmlHighlighter(self.textEdit.document())
      def changeHighlightToMkd(self):
          self.highlighter = MarkdownHighlighter(self.textEdit.document())
      def changeHighlightToC(self):
          self.highlighter = CHighlighter(self.textEdit.document())
      def changeHighlightToPython(self):
          self.highlighter = PythonHighlighter(self.textEdit.document())
      def ToolsMenu(self):
        date=QtGui.QAction(QtGui.QIcon('exit.png'),'&Insert Date and Time',self)
        date.triggered.connect(self.addTime)

        default=QtGui.QAction(QtGui.QIcon('exit.png'),'&Launch File',self)
        default.triggered.connect(self.launch)

        length=QtGui.QAction(QtGui.QIcon('exit.png'),'&Character Count',self)
        length.triggered.connect(self.count)
        comp = QtGui.QAction(QtGui.QIcon('exit.png'),'&Compile Markdown To HTML',self)
        comp.triggered.connect(self.comp)
        pdf=QtGui.QAction(QtGui.QIcon('exit.png'),'&PDF',self)
        pdf.triggered.connect(self.savePDF)

        toolsmenu=self.menu.addMenu('&Tools')
        toolsmenu.addAction(length)
        toolsmenu.addAction(date)
        toolsmenu.addAction(comp)
        exportMen=toolsmenu.addMenu('&Export As')
        exportMen.addAction(pdf)
        toolsmenu.addAction(default)

      def AboutMenu(self):
        about=QtGui.QAction(QtGui.QIcon('exit.png'),'&About',self)
        about.triggered.connect(self.showAbout)

        helpmenu=self.menu.addMenu('&Help')
        helpmenu.addAction(about)
      def setGUI(self):

            self.textEdit=QtGui.QTextEdit()
            self.document=QtGui.QTextDocument()
            self.document.setDefaultFont(QtGui.QFont('Segoe UI',13))
            self.textEdit.setDocument(self.document)
            self.setCentralWidget(self.textEdit)
            self.textEdit.setTabStopWidth(20)
            

            self.menu=self.menuBar()
            self.FileMenu()
            self.EditMenu()
            self.ViewMenu()
            self.ToolsMenu()
            self.AboutMenu()

            self.setGeometry(200,200,550,450)
            self.setWindowIcon(QtGui.QIcon('{0}icon.png'.format(setup)))
            self.setWindowTitle("Notepad By Pradd")
            self.show()
      def launch(self):
            try:
                  os.startfile(self.location)
            except:
                  self.savefile()
                  self.launch()
      def showAbout(self):
            textstring='''<font size="5" family="Segoe UI" >Created By Pradipta using Python and Qt.<br>
Based on the PySide Qt Toolkit for Python.<br>
Running on Python {0} on Windows.<br><br><br><br>
Version 3.1 <br>
Copyright 2014 Pradipta and Akshat</font>'''.format(str(sys.version)[:5:])
            self.help=QtGui.QWidget()
            self.help.setGeometry(200,200,400,350)
            self.help.setWindowIcon(QtGui.QIcon('{0}icon.png'.format(setup)))
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
      def comp(self):
            text=self.document.toPlainText()
            text=mistune.markdown(text)
            text="<html>\n<head>\n</head>\n<body>\n {0} \n </body>\n</html>".format(text)
            self.document.setPlainText(text)
            
            self.changeHighlightToHtml()
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

                 
                  print font[0]
                  self.document.setDefaultFont(font[0])
                  
                  
      def opencmd(self):
            self.location=path
            with open(self.location,'r') as f:
                  data=f.read()
            self.setWindowTitle("Notepad By Pradd- {0}".format(self.location))
            self.textEdit.setText(data)
      def newwindow(self):
            try:
                  if self.location:
                        self.textEdit.setText('')
                        self.setWindowTitle("Notepad By Pradd")
            except:
                  if len(str(self.textEdit.toPlainText())) > 2:
                        print 'sc'
                        ret = QtGui.QMessageBox.warning(self, self.tr("New File"),
                               self.tr("The document has been modified.\n" + \
                                  "Do you want to save your changes?"),
                               QtGui.QMessageBox.Save | QtGui.QMessageBox.Discard
                               | QtGui.QMessageBox.Cancel,
                               QtGui.QMessageBox.Save)
                        
                        if ret==QtGui.QMessageBox.Save:
                              self.savefile()
                              self.textEdit.setText('')
                              self.setWindowTitle("Notepad By Pradd")
                        elif ret==QtGui.QMessageBox.Discard:
                              self.textEdit.setText('')
                              self.setWindowTitle("Notepad By Pradd")
      def openfile(self):
            try:
                  files_types = "Text File (*.txt);;HTML Files (*.html);;Python File (*.py);;Markdown File (*.md);;C++ File (*.cpp);;All Files(*)"
                  filename=QtGui.QFileDialog.getOpenFileName(self,"Open File",'C:/',files_types)
                  self.location=filename[0]
                  self.fileExt=self.location.split('.')[-1]
                  python=["py","pyw","pyo"]
                  html= ["html","htm","php","xhtml"]
                  cpp=["cpp","c"]
                  mkd=["md"]
                  if self.fileExt in python:
                        self.changeHighlightToPython()
                        self.checkpython.setChecked(True)
                  elif self.fileExt in html:
                        self.changeHighlightToHtml()
                        self.checkhtml.setChecked(True)
                  elif self.fileExt in cpp:
                        self.changeHighlightToC()
                        self.checkc.setChecked(True)
                  elif self.fileExt in mkd:
                        self.changeHighlightToMkd()
                        self.checkmkd.setChecked(True)
        
                  with open(filename[0],'r') as f:
                        data=f.read()
                  self.setWindowTitle("Notepad By Pradd- {0}".format(self.location))
                  self.textEdit.setText(data)
            except:
                  pass
      def savePDF(self):
            try:
                  print self.location.split('.')[-1]
                  if not self.location.split('.')[-1]=="pdf":
                        self.locs=self.location.replace(self.location.split('.')[-1],"pdf")
                  else:
                        self.locs=self.location
                  self.saveAsPDF(self.locs,self.textEdit.toPlainText())
                  self.ns=self.locs
            except:
                  text = QtGui.QInputDialog.getText(self, self.tr("PDF Export"),
                                     self.tr("Name of Exported File:"), QtGui.QLineEdit.Normal,
                                     QtCore.QDir().home().dirName())
                  if  text:
                        string=text[0]+'.pdf'
                        self.saveAsPDF(string,self.textEdit.toPlainText())
                        self.ns=string
            self.msBox=QtGui.QMessageBox.information(self,'Export Successful',"PDF has been exported in the location {0}".format(self.ns))
      def saveAsPDF(self,argv,data):
            writer = PDFLite(argv)
            writer.set_information(title="Hello World!")
            document = writer.get_document()
            document.set_font('arial', '', 11)
            document.add_text(data)
            writer.close()


      def savefile(self):
            try:
                  files_types = "Text File (*.txt);;HTML Files (*.html);;Python File (*.py);;Markdown File (*.md);;C++ File (*.cpp);;PDF File(*.pdf);;YAML (*.yml)"
                  file = QtGui.QFileDialog.getSaveFileName(self, 'Save file', '', files_types)
                  self.location=file[0]
                  print self.location.split('.')
                  if self.location.split('.')[1]=='pdf':
                        print "yay"
                        self.saveAsPDF(self.location,self.textEdit.toPlainText())
                  else:
                        if self.location.split('.')[1]=='html':
                              with open(file[0],'w') as f:
                                    f.write(mistune.markdown(str(self.textEdit.toPlainText())))
                              self.setWindowTitle("Notepad By Pradd- {0}".format(self.location))
                        else:
                              
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

def runcmd():
      global path
      path=sys.argv[1]
      app=QtGui.QApplication(sys.argv)
      ex=frame()
      ex.opencmd()
      sys.exit(app.exec_())

def main():

      app=QtGui.QApplication(sys.argv)
      ex=frame()

      sys.exit(app.exec_())
def newwindow():
  os.system("{0}notepad-by-pradd.exe".format(setup))


if __name__=='__main__':
      if len(sys.argv)>1:
            runcmd()
      else:

            main()
