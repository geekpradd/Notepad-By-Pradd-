#
#   Notepad By Pradd is a Python Based Text and Code Editor .Created By Pradd AKA Pradipta . (C) 2014.
#
#Code To Import Modules
from Tkinter import *
from tkFileDialog import *
from tkMessageBox import *
from idlelib import textView
import tkFont ,os ,time,sys ,tkFont
#Function to create required options directory for preference files
def ensureStorage(f ,need):
    if need==1:
        d=os.path.join(os.path.abspath(os.path.dirname(f)) , f)
    else:
        d = os.path.join(os.path.dirname(f) ,f)

    if not os.path.exists(d):

        os.makedirs(d)
    else:
        pass
#Housekeeping Code for Variables that reflect control flow
fil = ""
encoding ='iso-8859-1'
ensureStorage('options' , 1)
open('options/wrap.bxz' ,'a').close()
val = open('options/wrap.bxz' ,'r')
imp =val.read()
val.close()
open('options/batchsign.bxz' ,'a').close()
val2 = open('options/batchsign.bxz' ,'r')
imp2=val2.read()
val2.close()
open('options/sethc.bxz' ,'a').close()
val3 =open('options/sethc.bxz' ,'r')
imp3 =val3.read()
val3.close()
if len(imp3)>1:
    signPre = True
else:
    signPre = False

if  not len(imp2)<=1:
    bool_for = True
else:
    bool_for =False
if len(imp2)<=1:
    use_custom = False
else:
    use_custom= True
class StickyNote(Toplevel):

    def create_widgets(self,
                      ):
        self.font = tkFont.Font(family="Arial" ,  size=15)
        self.stickynote = Text(self,
                               bg="yellow",
                               font=self.font,
                               relief="sunken",
                               width=40,
                               height=15,
                               wrap="word")
        self.stickynote.pack(side="top",expand=1,fill="both")

        self.stickynote.focus_set()

    def create_menu(self,
                    ):
        self.font = tkFont.Font(family="Arial" , weight="bold" , size=13)
        self.menu = Menu(self,
                         font=self.font,
                         relief="raised")

        self.filemenu = Menu(self.menu,
                             font=self.font,
                             relief="raised",
                             tearoff=0)

        self.filemenu.add_command(label="New Window",
                                  accelerator="Ctrl-N",
                                  command=self.newwindow,
                                  underline=4)

        self.filemenu.add_command(label="Exit",
                                  accelerator="Ctrl-Q",
                                  command=self.destruct,
                                  underline=1)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="About",
                                  accelerator="",
                                  command=self.aboutbox,
                                  underline=0)

        self.menu.add_cascade(label="File",
                              menu=self.filemenu,
                              underline=0)

        self.bind("<Control-N>",self.newwindow)
        self.bind("<Control-n>",self.newwindow)

        self.bind("<Control-Q>",self.destruct)
        self.bind("<Control-q>",self.destruct)
        self.bind("<Escape>",self.closewindow)

        self.bind("<3>",self.show_menu)

    def show_menu(self,event):
        self.menu.tk_popup(event.x_root,event.y_root)

    def newwindow(self,whatever=None):
        newwindow = Application()
        newwindow.mainloop()

    def destruct(self,whatever=None):
        self.destroy()

    def closewindow(self,whatever=None):
        self.destroy()

    def aboutbox(self,whatever=None):
        tkMessageBox.showinfo("About","""\
Sticky Note
Version 1.0\n
By Martin Ultima""")

    def __init__(self,master=None):
        Toplevel.__init__(self,master)
        try:
            self.iconbitmap(r'icon.ico')
        except:
            pass
        self.font = tkFont.Font(family="Arial" , weight="bold" , size=13)
        vc = self.font
        self.title("Sticky Note")
        self.geometry("200x200")
        self.maxsize(width=200 , height=200)
        self.minsize(width=200 , height=200)
        self.create_widgets()
        self.create_menu()
#Main Program Class for UI . Contains functions for Program Events
class AppUI(Frame):

    def __init__(self, master=None):

        #Intialize the Frame widget On Top of the master widget
        Frame.__init__(self, master, relief=SUNKEN, bd=2)
        #Function to associate check function when program is quit
        master.protocol('WM_DELETE_WINDOW',self.quitcheck)
        #Define saveName for future purposes
        self.saveName=""
        self.lth = master
        self.fil = fil
        #Bindings for Shortcut keys In The Program . Note that both Upper and Lower Case buttons are used.
        master.bind('<Control-O>' , self.openBind)
        master.bind('<Control-N>' , self.newBind)
        master.bind('<Control-o>' , self.openBind)
        master.bind('<Control-n>' , self.newBind)
        master.bind('<Shift-S>' , self.saveBind)
        master.bind('<Shift-s>' , self.saveBind)
        master.bind('<Control-s>' , self.saveBindex)
        master.bind('<Control-S>' , self.saveBindex)
        master.bind('<Shift-X>' , self.exitBind2x)
        master.bind('<Shift-x>' , self.exitBind2x)
        master.bind('<Shift-F6>' , self.dateBind)
        master.bind('<Shift-F5>' , self.charBind)
        master.bind('<F1>' , showAboutbin)
        master.bind('<F2>' , self.showOptions)
        master.bind('<F7>' , self.insBind)
        master.bind('<Control-s>' , self.saveExisting2b)
        master.bind('<Control-S>' , self.saveExisting2b)
        master.bind('<Alt-R>' , self.runbind)
        master.bind('<Alt-r>' , self.runbind)
        master.bind('<Control-m>' , self.mini2)
        master.bind('<Control-M>' , self.mini2)
        master.bind('<Control-D>' , self.delBind)
        master.bind('<Control-d>' , self.delBind)
        master.bind('<Alt-n>' , self.stickynotex)
        master.bind('<Alt-N>' , self.stickynotex)
        master.bind("<3>",self.show_right_menu)
        master.bind("<Control-1>",self.show_right_menu)
        #Initalize The Menu Bar
        self.menubar = Menu(self ,tearoff=0)
        self.menu1 = Menu(self.menubar , tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.menu1 )
        self.menu1.add_command(label="New               Ctrl + N" , command=createNew )
        self.menu1.add_command(label='Open              Ctrl + O' ,command=self.openFile)
        self.menu1.add_command(label='Save               Ctrl +  S' ,command=self.saveExisting2)
        self.menu1.add_command(label='Save As          Shift + S' ,command=self.saveText)
        self.menu1.add_command(label='Minimize         Ctrl +  M' , command = self.mini)
        self.menu1.add_command(label='Quit                Shift +  X' , command = exitBind)
        menu2 = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=menu2)
        menu2.add_command(label="Cut               Ctrl + X" , command=self.cut)
        menu2.add_command(label="Copy            Ctrl + C" ,command=self.copy)
        menu2.add_command(label="Paste            Ctrl + V" ,command=self.paste)
        menu2.add_command(label="Delete          Ctrl + D" ,command=self.delete)
        menu2.add_separator()
        menu2.add_command(label="Select All            " ,command=self.select_all)
        menu2.add_separator()
        menu2.add_command(label="Highlighter On         " ,command=self.highlighter_on)
        menu2.add_command(label="Highlighter Off         " ,command=self.highlighter_off)

        #HTML Add On
        html_menubutton = Menubutton(self.menubar,

                                     relief="flat",
                                     text="HTML",
                                     underline=None,
                                     direction="below")
        html_menubutton.pack(side="left")

        html_menu = Menu(html_menubutton,

                         relief="raised",
                         tearoff=0)
        html_menubutton["menu"] = html_menu

        block_menu = Menu(html_menu,

                          relief="raised",
                          tearoff=0)

        heading_menu = Menu(html_menu,

                            relief="raised",
                            tearoff=0)

        format_menu = Menu(html_menu,

                           relief="raised",
                           tearoff=0)

        list_menu = Menu(html_menu,

                         relief="raised",
                         tearoff=0)

        misc_menu = Menu(html_menu,

                         relief="raised",
                         tearoff=0)

        jsblog_menu = Menu(html_menu,

                           relief="raised",
                           tearoff=0)

        html_menu.add_command(label="New Webpage",
                              accelerator="",
                              command=lambda whatever=None: self.new_webpage(self),
                              underline=None)

        html_menu.add_separator()

        html_menu.add_cascade(label="Text Blocks",
                              menu=block_menu,
                              underline=None)

        block_menu.add_command(label="Paragraph",
                               accelerator="",
                               command=lambda whatever=None: self.insert_p(self),
                               underline=None)

        block_menu.add_command(label="Line Break",
                               accelerator="",
                               command=lambda whatever=None: self.insert_br(self),
                               underline=None)

        html_menu.add_cascade(label="Headings",
                              menu=heading_menu,
                              underline=None)

        heading_menu.add_command(label="Heading #1",
                                 accelerator="",
                                 command=lambda whatever=None: self.insert_h1(self),
                                 underline=None)

        heading_menu.add_command(label="Heading #2",
                                 accelerator="",
                                 command=lambda whatever=None: self.insert_h2(self),
                                 underline=None)

        heading_menu.add_command(label="Heading #3",
                                 accelerator="",
                                 command=lambda whatever=None: self.insert_h3(self),
                                 underline=None)

        heading_menu.add_command(label="Heading #4",
                                 accelerator="",
                                 command=lambda whatever=None: self.insert_h4(self),
                                 underline=None)

        heading_menu.add_command(label="Heading #5",
                                 accelerator="",
                                 command=lambda whatever=None: self.insert_h5(self),
                                 underline=None)

        heading_menu.add_command(label="Heading #6",
                                 accelerator="",
                                 command=lambda whatever=None: self.insert_h6(self),
                                 underline=None)

        html_menu.add_cascade(label="Formatting",
                              menu=format_menu,
                              underline=None)

        format_menu.add_command(label="Bold",
                                accelerator="",
                                command=lambda whatever=None: self.insert_b(self),
                                underline=None)

        format_menu.add_command(label="Italics",
                                accelerator="",
                                command=lambda whatever=None: self.insert_i(self),
                                underline=None)

        format_menu.add_command(label="Code",
                                accelerator="",
                                command=lambda whatever=None: self.insert_code(self),
                                underline=None)

        html_menu.add_cascade(label="Lists",
                              menu=list_menu,
                              underline=None)

        list_menu.add_command(label="Numbered List",
                              accelerator="",
                              command=lambda whatever=None: self.insert_ol(self),
                              underline=None)

        list_menu.add_command(label="Bulletted List",
                              accelerator="",
                              command=lambda whatever=None: self.insert_ul(self),
                              underline=None)

        list_menu.add_separator()

        list_menu.add_command(label="List Item",
                              accelerator="",
                              command=lambda whatever=None: self.insert_li(self),
                              underline=None)

        html_menu.add_cascade(label="Miscellaneous",
                              menu=misc_menu,
                              underline=None)

        misc_menu.add_command(label="Horizonal Rule",
                              accelerator="",
                              command=lambda whatever=None: self.insert_hr(self),
                              underline=None)

        misc_menu.add_command(label="Image",
                              accelerator="",
                              command=lambda whatever=None: self.insert_img(self),
                              underline=None)

        misc_menu.add_separator()

        misc_menu.add_command(label="Inline Script",
                              accelerator="",
                              command=lambda whatever=None: self.insert_script(self),
                              underline=None)

        misc_menu.add_command(label="External Script",
                              accelerator="",
                              command=lambda whatever=None: self.insert_external_script(self),
                              underline=None)

        html_menu.add_command(label="Link",
                              accelerator="",
                              command=lambda whatever=None: self.insert_a(self),
                              underline=None)

        html_menu.add_separator()

        html_menu.add_command(label="Preview",
                              accelerator="",
                              command=lambda whatever=None: self.webpreview(self),
                              underline=None)

        self.menubar.add_cascade(label="HTML",
                                 menu=html_menu,
                                 underline=None)



        menu3 = Menu(self.menubar , tearoff=0)
        self.menubar.add_cascade(label='Insert' ,menu=menu3)
        menu3.add_command(label="Date & Time         Shift + F6" ,command=self.insertDate)
        menu3.add_command(label="Signature                        F7" ,command=self.insertSignature)
        menu4 =Menu(self.menubar , tearoff=0)
        self.menubar.add_cascade(label="Tools" , menu=menu4)
        menu4.add_command(label="Character Count                 Shift + F5" , command=self.showCharCount)
        self.cChange = menu4.add_command(label="Launch in Default Program   Alt+R" , command=self.run)
        menu4.add_command(label="Options                                       F2" , command=self.showOptions)
        menu4.add_command(label="Sticky Note                                Alt + N",
                                    accelerator="",
                                    command=self.stickynote,
                                    underline=None)
        menu5=Menu(self.menubar ,tearoff=0)
        self.menubar.add_cascade(label='Help' ,menu=menu5)
        menu5.add_command(label='About      F1' ,command=showAbout)
        self.master.config(menu=self.menubar)
        #Add on HTML

        #Control Flow for The Text Widget to set up Word Wrap
        if bool_for:
            self.canvas = Text(self, wrap=NONE,bg="white", width=200, height=200,
                                 bd=0, highlightthickness=0 , font=xyz)
        else:
            self.canvas = Text(self, wrap=WORD,bg="white", width=200, height=200,
                                 bd=0, highlightthickness=0 , font=xyz)

        #Code to Insert Scrollbars in x and y co-ordinates
        self.yscrollbar=Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.yscrollbar.pack(side=RIGHT, fill=Y)
        self.canvas["yscrollcommand"]=self.yscrollbar.set
        self.insi = Label(self ,text="(C) 2014 Designed By Pradipta")
        self.insi.pack(side=BOTTOM, fill=X)
        self.xscrollbar=Scrollbar(self, orient=HORIZONTAL, command=self.canvas.xview)
        self.xscrollbar.pack(side=BOTTOM, fill=X)
        self.canvas["xscrollcommand"]=self.xscrollbar.set

        #Pack Text Widget to the Frame
        self.canvas.pack()
    #Quit Function
    def quitcheck(self):
        if self.saveName=="":
            if len(self.canvas.get(1.0 ,END)) >1:
                tru =askyesnocancel('Notepad By Pradd' , 'Do You Want To Save The File Before Closing?')
                if tru:
                    self.saveExisting2()
                    self.lth.destroy()
                elif tru==None:
                    pass
                else:
                    self.lth.destroy()
            else:
                self.lth.destroy()
        else:
            with open(self.saveName , 'r') as file:
                reader = file.read()

            v =  self.canvas.get(1.0 ,END).rstrip()

            if v != reader:

                variable = 'Do You Want To Save %s Before Closing ?' %self.saveName
                cd = askyesnocancel('Notepad By Pradd' , variable)
                if cd:

                    self.saveExisting2()
                    self.lth.destroy()
                elif cd==None:
                    pass
                else:

                    self.lth.destroy()
            else:

                self.lth.destroy()


    #Select All Function
    def select_all(self):
        try:
            self.canvas.tag_add("sel","1.0","end")
        except:
            pass
    #Function To Activate Highlighter
    def highlighter_on(self):
        try:
            self.canvas.tag_add("highlighter","sel.first","sel.last")
            self.canvas.tag_configure("highlighter",background="#ffff00",foreground="#000000")
        except:
            pass
    #Function To De-Activate Highlighter
    def highlighter_off(self):
        try:
            self.canvas.tag_remove("highlighter","sel.first","sel.last")
        except:
            pass
    #Sticky Note Function inside main class
    def stickynotex(self ,x):
        self.stickynote()
    def stickynote(self):
        stickynote = StickyNote(self)
        stickynote.mainloop()
    #Function To Bind The Save Method to Shortcut Key
    def saveBindex(self , whatever=None):
        self.saveExisting2()

     #Function To Bind The Delete Method to Shortcut Key
    def delBind(self , whatever=None):
         try:
            self.canvas.delete("sel.first","sel.last")
         except:
            pass
    #Deletes Selected Text from the Widget . Note that sel means selection
    def delete(self):
        try:
            self.canvas.delete("sel.first","sel.last")
        except:
            pass
    #Function Binding
    def saveExisting2b(self ,x):
        self.saveExisting2()


    #Binding For Minimize Function
    def mini2(self ,dc):
        lineNo= str(int(self.canvas.index('end-1c').split('.')[0]))
        xc =  len(self.canvas.get(float(lineNo) ,END).rstrip()) -1
        self.canvas.delete(float(lineNo) + float(xc)/10,END)
        self.lth.iconify()

    #Function To Minimize Program to App Tray
    def mini(self):
        self.lth.iconify()

    def runbind(self,x):
        self.run()

    #Method To Launch File In Default Program . Uses Exception Handling
    def run(self):
        try:
            os.startfile(self.openLocation)
            showinfo("Launch File" , "File Launched In Default Program")
        except:
            try:
                os.startfile(self.nil)
                showinfo("Launch File" , "File Launched In Default Program")
            except:
                showerror("Operation Failed" , "File not Saved . Save file first and then launch the file .")

    #Shows The Option Dialog to Change Preferences.
    def showOptions(self):
        self.open1 = open('options/wrap.bxz' , 'r')
        self.read1= self.open1.read()
        self.open1.close()
        self.open2 = open('options/batchsign.bxz' , 'r')
        self.read2= self.open2.read()
        self.open2.close()
        self.sc = Tk()
        try:
            self.sc.iconbitmap(r'icon.ico')
        except:
            pass
        self.sc.geometry("400x400")
        self.sc.title("Options ")
        self.sc.minsize(width=370 ,height=270)
        self.sc.maxsize(width=370 ,height=270)
        dre = Label(self.sc ,text="Options For Notepad",font=xyz)
        dre.place(relx=.5 , rely=.105,anchor='c')
        drw = Label(self.sc ,text="Word Wrap (Enabled) :")
        drw.place(relx=.27 , rely=.335,anchor='c')
        butt = Button(self.sc,text='Disable Word Wrap :' ,command=self.appendDes)
        butt.place(relx=.7 , rely=.335  , anchor='c')
        vfr = Label(self.sc , text="Signature       :")
        vfr.place(relx=.26 ,rely=.51 , anchor='c')
        self.edr = Entry(self.sc)
        if use_custom:
            self.edr.insert(INSERT ,imp2)
            if not signPre:
                lmf = Label(self.sc , text="Insert Signature At Saving :" )
                lmf.place(relx=.27 , rely=.85 , anchor='c')
                bfr = Button(self.sc , text="Activate" , command=self.imp)
                bfr.place(relx=.7 , rely=.85 , anchor='c')
            else:
                lmf = Label(self.sc , text="Insert Signature At Saving :" )
                lmf.place(relx=.27 , rely=.85 , anchor='c')
                bfr = Button(self.sc , text="Deactivate" , command=self.impx)
                bfr.place(relx=.7 , rely=.85 , anchor='c')
        self.edr.place(relx=.7 , rely=.51 , anchor='c')
        xcj=Button(self.sc , text='Submit Signature' ,command=self.submitSign)
        xcj.place(relx=.5 ,rely=.67,anchor='c')
        if not len(self.read1)<=2:
            drw.config(text="Word Wrap (Disabled) :")
            butt.config(text="Enable Word Wrap:" , command=self.appendDes2)

    #Dialogs For Signature Adding
    def imp(self):
        op =open('options/sethc.bxz' ,'w')
        op.write("Yeyeye")
        op.close()
        showinfo("Success!" , "Auto Signature Adding at the end Activated . Please restart the program for the changes to take place.")

        self.sc.destroy()
    def impx(self):
        op =open('options/sethc.bxz' ,'w')
        op.write("Y")
        op.close()
        showinfo("Success!" , "Auto Signature Adding at the end Deactivated . Please restart the program for the changes to take place.")
        self.sc.destroy()

    #Dialog For Submitting Signature
    def submitSign(self):
        storeVal =self.edr.get()
        if not len(storeVal):
            showerror("Operation Failed" , "Please Enter a Signature in the Box.")
        else:
            thr = open('options/batchsign.bxz' ,'w')
            thr.write(storeVal)
            thr.close()
            showinfo("Success!" , "Signature Edited . Please restart the Program for the changes to take place.")
            self.sc.destroy()
    #Dialogs for Word Wrap
    def appendDes(self):
        xc = open('options/wrap.bxz' , 'w')
        xc.write("edfgvrtrgt4rgtrgtgr")
        xc.close()
        showinfo("Word Wrap" , "Word Wrap Has Been Disabled . Restart The Program For The Changes To Take Place")
        self.sc.destroy()
    def appendDes2(self):
        xc = open('options/wrap.bxz' , 'w')
        xc.write("1")
        xc.close()
        showinfo("Word Wrap" , "Word Wrap Has Been Enabled .Restart The Program For The Changes To Take Place")
        self.sc.destroy()

    #Function To Insert Signature To Text Widget
    def insertSignature(self):
        if not use_custom:
            x = "Designed By Pradipta"
        else:
            x = imp2
        self.canvas.insert("insert" , x)

    #Bindings for Functions
    def insBind(self,x):
        self.insertSignature()
    def charBind(self,x):
        self.showCharCount()
    def dateBind(self,x):
        self.insertDate()

    #Function To Display No Of Characters and Lines
    def showCharCount(self):
        #Variable holding no of lines using Tkinter's index method
        lineNo= str(int(self.canvas.index('end-1c').split('.')[0]))

        #Variable holding number of charcters in a line
        xc =  len(self.canvas.get(float(lineNo) ,END).rstrip()) -1
        vv = int(lineNo) -1

        #Length of Characters
        lengthText = len(self.canvas.get(1.0 ,END).rstrip()) -vv

        #Message Variable Control Flow
        if lengthText  <=1:
            if lineNo:
                variable = 'Your Document has %s character in %s line.'%(str(lengthText) ,lineNo )
            else:
                variable = 'Your Document has %s character in %s lines.'%(str(lengthText) ,lineNo )
        else:
            if lineNo:
                variable = 'Your Document has %s characters in %s line.' %(str(lengthText),lineNo)
            else:
                variable = 'Your Document has %s characters in %s lines.' %(str(lengthText),lineNo)
        #Tk Message Box To Show Characters
        showinfo('Character Count' , variable)

    #Inserts Date to Text Widget
    def insertDate(self):
        self.canvas.insert("insert" , time.asctime())

    #Function to Cut Text Into System Clipboard
    def cut(self):
        try:
            text = self.canvas.get("sel.first" , "sel.last")
            if len(text)==0:
                pass
            else:
                self.clipboard_clear()
                self.clipboard_append(text)
                self.canvas.delete("sel.first" ,"sel.last")
        except:
            pass

    #Function To Copy Text Into System Clipboard:
    def copy(self):
        try:
             text = self.canvas.get("sel.first" , "sel.last")
             if len(text)==0:
                 pass
             else:
                 self.clipboard_clear()
                 self.clipboard_append(text)
        except:
            showerror("Select Text" , "Select Text To Copy ")
    #Paste Function
    def paste(self):
        try:
            inst =self.clipboard_get()
            self.canvas.insert("insert" , inst)
        except:
            pass

    #Bindings
    def newBind(self ,x):
        lineNo= str(int(self.canvas.index('end-1c').split('.')[0]))
        xc =  len(self.canvas.get(float(lineNo) ,END).rstrip()) -1
        self.canvas.delete(float(lineNo) + float(xc)/10,END)
        createNew()
    def openBind(self,x):
        lineNo= str(int(self.canvas.index('end-1c').split('.')[0]))
        xc =  len(self.canvas.get(float(lineNo) ,END).rstrip()) -1
        self.canvas.delete(float(lineNo) + float(xc)/10,END)
        self.openFile()
    def saveBind(self,x):
        lineNo= str(int(self.canvas.index('end-1c').split('.')[0]))
        xc =  len(self.canvas.get(float(lineNo) ,END).rstrip()) -1
        self.canvas.delete(float(lineNo) + float(xc)/10,END)
        self.saveText()

    #Quit Function To Exit Program
    def qu(self , master):
        if askyesno('Quit Notepad' , "Do You Really Want To Quit ?"):
            master.destroy()

        else:
            pass

    #Function To Ask User for Location Of Current File . Then File is opened using File I/O
    def openFile(self):

        if len(self.canvas.get(1.0 ,END).rstrip())>1:
            if self.saveName =="":
                v = askyesnocancel("Notepad" , "Do You Want To Save Before Opening A File?")
                if v:
                    self.saveExisting2()
                    self.openit()
                elif v==None:
                    pass
                else:
                    self.openit()
            else:
                with open(self.saveName ,'r') as file:
                    xc = file.read()
                dc = self.canvas.get(1.0 ,END).rstrip()
                if xc!=dc:
                    v = askyesnocancel("Notepad" , "Do You Want To Save" + self.saveName + " Before Opening A File?")
                    if v:
                        self.saveExisting2()
                        self.openit()
                    elif v==None:
                        pass
                    else:
                        self.openit()
                else:
                    self.openit()
        else:
            self.openit()
    def openit(self):
        try:
            self.saveName =askopenfilename(title='Open File', initialdir = 'D:/' , filetypes = (("All Files" , "*.*"),("Text Files" , "*.txt"),("HTML Files" , '*.html') ))
            x = self.fileExtension = self.saveName.split('.')[-1]
            self.openLocation = self.saveName
            self.val = open(self.saveName , 'r')
            self.rf = self.val.read()
            self.rf = self.rf.rstrip()
            self.val.close()
            self.master.title('Notepad By Pradd  ' + self.saveName )
            self.canvas.delete(1.0 ,END)
            self.canvas.insert(INSERT , self.rf)
        except:
            pass
    def open_cmd(self):
      try:
        self.saveName = self.fil
        self.openLocation = self.saveName

        self.val = open(self.fil , 'r')
        self.rf = self.val.read()
        self.rf = self.rf.rstrip()
        self.val.close()
        self.master.title('Notepad By Pradd  ' + self.saveName )
        self.canvas.delete(1.0 ,END)
        self.canvas.insert(INSERT , self.rf)
      except:
        pass
    #Bindings and Bindings......
    def exitBind2x(self,x):
        lineNo= str(int(self.canvas.index('end-1c').split('.')[0]))
        xc =  len(self.canvas.get(float(lineNo) ,END).rstrip()) -1
        self.canvas.delete(float(lineNo) + float(xc)/10,END)
        exitBind2(x)

    #Function used only in specific save scenarios . Not used anymore though supplied for source reading :) (200 Bytes don't mater :D )
    def saveExisting(self):
        self.saveTextExist = self.canvas.get(1.0 , END)
        self.saveTextExist = self.saveTextExist.rstrip()
        with open(self.openLocation , 'w') as file:
            if signPre:
                file.write(self.saveTextExist + "\n" + imp2)
            else:
                file.write(self.saveTextExist)

    #Save Function that redirects to Save As function if file not saved . Used for saving already saved files
    def saveExisting2(self):
        if self.saveName == "":
            self.saveText()
        else:
            self.saveTextExist = self.canvas.get(1.0 , END)
            self.saveTextExist = self.saveTextExist.rstrip()
            with open(self.saveName, 'w') as file:
                if signPre:
                     file.write(self.saveTextExist+ "\n" + imp2)
                else:
                    file.write(self.saveTextExist)
    #Save As function
    def saveText(self):
        self.saveTextNew = self.canvas.get(1.0 , END)
        self.saveTextNew = self.saveTextNew.rstrip()
        self.saveName = asksaveasfilename(title='Save File' ,   filetypes = (("Text Files" , "*.txt*"),("HTML Files" , '*.html*') ) , defaultextension='.txt')
        self.nil = self.saveName
        self.fileExtension = self.saveName.split('.')[-1]

        try:
            with open(self.saveName ,'w') as file:
                if signPre:
                    file.write(self.saveTextNew + "\n" + imp2)
                else:
                    file.write(self.saveTextNew)
            self.master.title( 'Notepad By Pradd  '  +self.saveName )

        except:
            pass
    #External HTML functions
    def new_webpage(self,x):
        self.canvas.delete("0.0","end")
        self.canvas.insert("end","""\
    <html>



    <head>
      <title>Webpage Title</title>
      <link rel="stylesheet" type="text/css" href="style.css" />
      <meta name="generator" content="Notepad" />
      <meta http-equiv="content-type" content="text/xml; encoding=UTF-8" />
    </head>

    <body>

    <!-- Start inserting stuff at the end of this line. -->

    <!-- Don't insert anything else after this!! -->

    <hr />

    <p><i>This page was created with Notepad By Pradd  </i></p>

    </body>

    </html>
    """)

    def insert_p(self ,x):
        self.canvas.insert("insert","\n\n<p>Insert paragraph here</p>")

    def insert_br(self ,x):
        self.canvas.insert("insert","\n  <br />Insert line break here")

    def insert_h1(self ,x):
        self.canvas.insert("insert","\n\n<h1>Insert Heading Here</h1>")

    def insert_h2(self ,x):
        self.canvas.insert("insert","\n\n<h2>Insert Heading Here</h2>")

    def insert_h3(self ,x):
        self.canvas.insert("insert","\n\n<h3>Insert Heading Here</h3>")

    def insert_h4(self ,x):
        self.canvas.insert("insert","\n\n<h4>Insert Heading Here</h4>")

    def insert_h5(self ,x):
        self.canvas.insert("insert","\n\n<h5>Insert Heading Here</h5>")

    def insert_h6(self ,x):
        self.canvas.insert("insert","\n\n<h6>Insert Heading Here</h6>")

    def insert_b(self ,x):
        self.canvas.insert("insert","<b>Insert Bold Text Here</b>")

    def insert_i(self ,x):
        self.canvas.insert("insert","<i>Insert Italicized Text Here</i>")

    def insert_code(self ,x):
        self.canvas.insert("insert","<code>Insert Code Here</code>")

    def insert_hr(self ,x):
        self.canvas.insert("insert","\n\n<hr />")

    def insert_a(self ,x):
        self.canvas.insert("insert","<a href=\"Insert Filename or URL Here\">Insert Link Text Here</a>")

    def insert_img(self ,x):
        self.canvas.insert("insert","<img src=\"Insert Filename or URL Here\" alt=\"Insert Alternate Text Here\" title=\"Insert Tooltip Here\" />")

    def insert_script(self ,x):
        self.canvas.insert("insert","<script type=\"text/javascript\"><!--  Insert JavaScript code here --></script>")

    def insert_external_script(self ,x):
        self.canvas.insert("insert","<script type=\"text/javascript\" src=\"Insert Filename or URL Here\"> </script>")

    def insert_ol(self ,x):
        self.canvas.insert("insert","\n\n<ol>\n\n</ol>")

    def insert_ul(self ,x):
        self.canvas.insert("insert","\n\n<ul>\n\n</ul>")

    def insert_li(self ,x):
        self.canvas.insert("insert","\n  <li>Insert item text here.</li>")

    #Future Function to display HTML code.
    def webpreview(self,whatever=None):
        pass

    #Right Click Mneu Function .Right Click!
    def show_right_menu(self,event):
        self.newmenu= Menu(self , tearoff=0)
        self.newmenu.add_command(label="Cut",command=self.cut)
        self.newmenu.add_command(label="Copy",command=self.copy)
        self.newmenu.add_command(label="Paste",command=self.paste)
        self.newmenu.add_command(label="Delete",command=self.delete)
        self.newmenu.add_separator()
        self.newmenu.add_command(label="Select All            " ,command=self.select_all)
        self.newmenu.add_separator()
        self.newmenu.add_command(label="Highlighter On         " ,command=self.highlighter_on)
        self.newmenu.add_command(label="Highlighter Off         " ,command=self.highlighter_off)
        self.newmenu.tk_popup(event.x_root,event.y_root)
#External Bindings...
def exitBind():
    app.qu(root)
def exitBind2(x):
    app.qu(root)
def showAboutbin(y):
    showAbout()

#About Box Widget . Doesn't use a class for (un)simplicity.
def showAbout():
    aboutDialog =Tk()
    aboutDialog.geometry("300x300")
    aboutDialog.minsize(width=300,height=300)
    aboutDialog.maxsize(width=300 , height=300)
    needFont =tkFont.Font(family='Arial' ,size=12)
    aboutText='Licensed Under a Propetairy License .\nRunning in Python %s on %s using py2exe. \nCopyright 2014 \n\n Notepad By Pradd is a Text Editor/Code Editor \ncreated in Python \n Created using Tk and Tkinter.\n' % (sys.version[0:3],sys.platform)
    try:
        aboutDialog.iconbitmap(r'icon.ico')
    except:
        pass
    aboutDialog.title("Notepad By Pradd (Pradipta)")
    header = Label(aboutDialog , text='Notepad By Pradd' ,fg='DeepSkyBlue2' ,font=needFont)
    header.place(relx=.5 , rely=.1 ,anchor='c')
    bam =Label(aboutDialog ,text=aboutText)
    bam.place(relx=.5 ,rely=.45 ,anchor='c' )
    lef = Label(aboutDialog,text='Credits To Akshat and Pradipta' ,fg='red2' , font=needFont)
    lef.place(relx=.5 , rely=.8,anchor='c')
    nef = Label(aboutDialog ,text="Version 2.3" ,font=needFont ,fg='navy')
    nef.place(relx=.5 , rely=.88,anchor='c')
    aboutDialog.mainloop()

#External Function To Create a New Window
def createNew():
    global root ,xyz
    root = Tk()
    root.geometry("550x500")
    xyz = tkFont.Font(family="Microsoft Sans Serif" , size=12)
    try:
        root.iconbitmap(r'icon.ico')
    except:
        pass
    root.title("Notepad By Pradd")
    app= AppUI(root)
    app.pack()
    root.mainloop()

#Main Startup Function That Initializes the Class
def main():
    global xyz ,root
    root = Tk()
    xyz = tkFont.Font(family="Microsoft Sans Serif" , size=12)
    root.geometry("550x500")
    try:
        root.iconbitmap(r'icon.ico')
    except:
        pass
    root.title("Notepad By Pradd")
    app = AppUI(root)
    app.pack()

    root.mainloop()
def open_direct(argv):
  global xyz ,root,fil
  fil = argv

  root = Tk()
  xyz = tkFont.Font(family="Microsoft Sans Serif" , size=12)
  root.geometry("550x500")
  try:
      root.iconbitmap(r'icon.ico')
  except:
      pass
  root.title("Notepad By Pradd")
  app = AppUI(root)
  app.open_cmd()
  app.pack()

  root.mainloop()
#Starter Function To Avoid Problems during Module Importing
if __name__ == '__main__':
    if len(sys.argv) >=2:
      print "Test"
      open_direct(sys.argv[1])
    else:
      main()


