import matplotlib.pyplot as plt
import numpy as np
import csv
import tkinter as tk
import random
import math
import os
from tkinter import filedialog as fd
from tkinter import ttk
from os import X_OK
from numpy import Infinity

#Global Variables
globalfilename = "".strip()
globalprojectname = "Sicherungen"
#Erstellung der GUI
root = tk.Tk()
root.iconphoto(False, tk.PhotoImage(file='TMP\icon.ico'))
root.title("Selektivität")
root.geometry('')


#Auswahl an Funktionen
OptionList = ["Leitungsschutzschalter","Schmelzsicherung","Funktion"] 
#Auswahl an LS
#OptionListLS = ["B-Char","C-Char","D-Char","Z-Char","K-Char"] 
OptionListLS = ["---"] 
#Globaler speicher für Row's
rowstack = []


def readLS():
    global globalfilename
    path = globalfilename
    try:
        files = os.listdir(path)
        while files != []:
            for file in files:
                files.remove(file)
                for checkfile in files:
                    if (str(file)[:-6] == str(checkfile)[:-6]) and (str(file)[-4:] == '.txt') and (str(checkfile)[-4:] == '.txt'):
                        OptionListLS.append(str(file)[:-6])
                        files.remove(checkfile)
        OptionListLS.remove("---")
        OptionListLS.sort()
    except Exception:
        print("Fehler in Dateieinlesefunktion")
        print(Exception)

def colorgetter():
    r = lambda: random.randint(0,255)
    g = lambda: random.randint(0,255)
    b = lambda: random.randint(0,255)
    color = ('#%02X%02X%02X' % (r(),g(),b()))
    return color 
    #auf schöne farben begrenzen

def getDir():
    global globalfilename
    filename = fd.askdirectory()
    if len(filename)<2:
        filename = "Hier ist etwas schief gelaufen.."
    else:
        globalfilename = filename.strip()
        print(filename)
        readLS()

def setProjectName(name):
    global globalprojectname
    globalprojectname = name.strip()
    pass

def configOK(*args):
    setProjectName(args.get(args[0]))
    pass
def config_button_pressed():
    config = tk.Toplevel(root)
    config.iconphoto(False, tk.PhotoImage(file='TMP\icon.ico'))
    config.title("Einstellungen")
    config.geometry('600x600')
    configtext = tk.Label(config, text="Hier kann man sachen einstellen.").grid(row=0, column=1)
    configLSDirtext = tk.Label(config, text="Wo liegen die LS-Kennlienien").grid(row=1, column=0)
    configLSDir = tk.Button(config, width=5, height=2, text="Dir", command=lambda: getDir() ).grid(row=1, column=1)

    configProjectNametext = tk.Label(config, text="Projektnummer: ").grid(row=2, column=0)
    configProjectName = tk.Entry(config, width=40).grid(row=2, column=1)

    ok = tk.Button(config, width=5, height=2, text="OK", command=lambda: configOK(configProjectName.get(), "") ).grid(row=99, column=1)


    


    pass
    #TODO 
def showIt():
    global globalprojectname
    plt.xlabel('I in Ampere')
    plt.ylabel('t in s')
    if globalprojectname == "":
        globalprojectname = "Selektivität"
    plt.title(globalprojectname,fontsize=16)
    plt.semilogx(2) #loglog
    plt.semilogy(2) #loglog
    plt.grid(True, 'both', 'both') #grid für loglog mit (Visible, which, axis)
    plt.legend(loc='upper right')
    plt.show()
    #ruf mich auf um alles anzuzeigen 
def toFloatTimesX(a, x):
    r = []
    for w in a:
        r.append(float(w)*int(x))
    return r
    #blöde scheiße
def Replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")
    #Wandelt alle , in . um
def ReadDataSheet(file):
    x = []
    y = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='\\')
        for row in reader:
            x.append(Replace(row[0]))
            y.append(Replace(row[1]))
        return x, y
    #liest csv ein
def drawLS(type, In, Name, thermik):
    global globalfilename
    xl, yl = ReadDataSheet(globalfilename+"/"+str(type)+"_L.txt")
    xr, yr = ReadDataSheet(globalfilename+"/"+str(type)+"_R.txt")
    xl = toFloatTimesX(xl, In)
    yl = toFloatTimesX(yl, 1)
    xr = toFloatTimesX(xr, In)
    yr = toFloatTimesX(yr, 1)
    label = str(Name) + "|"+str(type) + " " + str(In) + "A"
    color = colorgetter()
    plt.plot(xl, yl,color=color, label = label)
    plt.plot(xr, yr, color=color)
    if thermik == 1:
        try:
            thermikx, thermiky = ReadDataSheet(globalfilename+"/"+str(type)+"_T.txt")
            thermikx = toFloatTimesX(thermikx, In)
            thermiky = toFloatTimesX(thermiky, 1)
            plt.plot(thermikx, thermiky, color=color)
        except Exception:
            print("Die Sicherung: " + str(type) + " hat keine abgelegten daten für THERMIK")
            print(Exception)
            pass
    #OK
def drawS(path, Name):
    x, y = ReadDataSheet(path)
    color = colorgetter()
    x = toFloatTimesX(x, 1)
    y = toFloatTimesX(y, 1)
    label = Name
    plt.plot(x, y,color = color, label = label)
    #OK

def drawf(f, name):
    #print(f)
    ff = '''
xlist = range(0, 100, 1)
ylist = []
for x in xlist:
    ylist.append(''' + str(f) + ''')    

    '''
    loc = {}
    exec(ff,globals(), loc)
    x = loc['xlist']
    y = loc['ylist']
    color = colorgetter()
    x = toFloatTimesX(x, 1)
    y = toFloatTimesX(y, 1)
    label = name
    plt.plot(x, y,color = color, label = label)
    #work

def doit_button_pressed(*args):
    for r in rowstack:
        menue = r.ddinner 
        if menue == OptionList[0]:
            type = r.ddLSinner.strip()
            In = r.ininput.strip()
            Name = r.nameinput.strip()
            thermik = r.checkboxvar
            drawLS(type, In, Name, thermik)
        elif menue == OptionList[1]:
            Name = r.nameinput.strip()
            path = r.fileinput_get.strip()
            drawS(path, Name)
        elif menue == OptionList[2]:
            f = r.f.strip()
            Name = r.nameinput.strip()
            drawf(f, Name)
        else:
            print("Error 1")
    showIt()    


def question_button_pressed(*args):
    help= tk.Toplevel(root)
    help.iconphoto(False, tk.PhotoImage(file='TMP\icon.ico'))
    help.title("Hilfe")
    help.geometry('600x600')
    helptext = tk.Label(help, text="Das ist der Hilfetext. ").pack()
    pass
    #HIER MUSS IRGENDWI EIN HILFE FENSTER AUFGEHEN, ZUR NOT WEB
def dropdownchangedLS(*args):
    return
    tmp = ".!optionmenu"+str(int(str(args[0])[6:])+1)
    #print(tmp)
    for r in rowstack:
        if (str(r.dropdownLS).strip() == tmp.strip()):
            #print("Gefunden: " + tmp)
            autoType = r.ddLSinner 
            #print(autoType)
            return
    #kann eig weg?
def plusbutton_pressed(*args): 
    ir = list(range(0, 100))
    for r in rowstack:
        ir.remove(int(str(r.label)[-2:].strip()))
    first_free_place = ir[0]
    addNewLine(first_free_place)
    #OK                           #print("Neue Sicherung erstellt. Nr:" + str(x))
def minusbutton_pressed(*args):
    #if str(args[0]) == "0":
    #    return 
    for r in rowstack:
        if (str(r.label)[-2:].strip() == str(args[0])):
            r.delRow()
            rowstack.remove(r)
            #print("Sicherung Nr. " + str(args[0]) + " gelöscht. ROW_ID:")
            #print(r)
            del r
    #OK
def getFilepath(*args):
    for r in rowstack:
        if (str(r.label)[-2:].strip() == str(args[0])):
            filename = fd.askopenfilename()
            if len(filename)<2:
                filename = "Hier ist etwas schief gelaufen.."
            (r.fileinput).config(text=filename)
    #OK        
def dropdownchanged(*args):
    erfolg = False
    print("Dropdown changed wurde aufgerufen")
    print(args)
    if str(args[0])[6:] == "0":
        tmp = ".!optionmenu"
    else:
        tmp = ".!optionmenu"+str(int(str(args[0])[6:])+1)
    #print(tmp)
    for r in rowstack:
        if (str(r.dropdown).strip() == tmp.strip()):
            erfolg = True
            print("Gefunden: " + tmp)
            newMenue = r.ddinner 
            print(newMenue)
            if newMenue == OptionList[0]:
                r.delRow()
                r.gridLS()
            elif newMenue == OptionList[1]:
                r.delRow()
                r.gridSchmelz()
            elif newMenue == OptionList[2]:
                r.delRow()
                r.gridf()
            else: 
                print("Ein Neueartiger Fehler wurde enteckt. :) Evenbtuel entstanden durch umbennung im dropdown menue 1?")
            return
    if not erfolg:
        dropdownchanged("PY_VAR"+str(int(str(args[0])[6:])-1),args[1],args[2])
        pass 
    #OK


class Row:
    def __init__(self, label, dropdown, ddinner, fileinput, nameinput, ininput, x, y, f, buttonminus, row, dropdownLS, ddLSinner, thermikcheckbox, checkboxvar):
        self._label = label
        self._dropdown = dropdown
        self._ddinner = ddinner
        self._fileinput = fileinput
        self._nameinput = nameinput
        self._ininput = ininput
        self._x = x
        self._y = y
        self._f = f
        self._buttonminus = buttonminus
        self._row = row
        self._dropdownLS = dropdownLS
        self._ddLSinner = ddLSinner
        self._thermikcheckbox = thermikcheckbox
        self._checkboxvar = checkboxvar
    def gridLS(self):
        self._label.grid(row=self._row, column=0)
        self._dropdown.grid(row=self._row+1, column=0)
        self._dropdownLS.grid(row=self._row, column=1)
        self._nameinput.grid(row=self._row, column=2)
        self._ininput.grid(row=self._row, column=3)
        self._thermikcheckbox.grid(row=self._row, column=4)
        self._buttonminus.grid(row=self._row+2, column=3, sticky=tk.E)
    def gridSchmelz(self):
        self._label.grid(row=self._row, column=0)
        self._dropdown.grid(row=self._row+1, column=0)
        self._fileinput.grid(row=self._row, column=1)
        self._nameinput.grid(row=self._row, column=2)
        self._buttonminus.grid(row=self._row+2, column=3, sticky=tk.E)
    def gridf(self):
        self._label.grid(row=self._row, column=0)
        self._dropdown.grid(row=self._row+1, column=0)
        self._f.grid(row=self._row, column=1)
        self._nameinput.grid(row=self._row, column=2)
        self._buttonminus.grid(row=self._row+2, column=3, sticky=tk.E)
    def delRow(self):
        self._label.grid_remove()
        self._dropdown.grid_remove()
        self._dropdownLS.grid_remove()
        self._fileinput.grid_remove()
        self._nameinput.grid_remove()
        self._ininput.grid_remove()
        self._buttonminus.grid_remove()
        self._f.grid_remove()
        self._thermikcheckbox.grid_remove()
    @property
    def fileinput_get(self):
        return self._fileinput.cget("text")
    @property
    def label(self):
        return self._label.cget("text")
    @label.setter
    def label(self, label):
        self._label = label
    @property
    def dropdown(self):
        return self._dropdown
    @dropdown.setter
    def dropdown(self, dropdown):
        self._dropdown = dropdown
    @property
    def fileinput(self):
        return self._fileinput
    @fileinput.setter
    def fileinput(self, fileinput):
        self._fileinput = fileinput
    @property
    def nameinput(self):
        return self._nameinput.get()
    @nameinput.setter
    def nameinput(self, nameinput):
        self._nameinput = nameinput
    @property
    def ininput(self):
        return self._ininput.get()
    @ininput.setter
    def ininput(self, ininput):
        self._ininput = ininput
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, x):
        self._x = x
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, y):
        self._y = y
    @property
    def f(self):
        return self._f.get()
    @f.setter
    def f(self, f):
        self._f = f
    @property
    def buttonminus(self):
        return self._buttonminus
    @buttonminus.setter
    def buttonminus(self, buttonminus):
        self._buttonminus = buttonminus
    @property
    def row(self):
        return self._row
    @property
    def dropdownLS(self):
        return self._dropdownLS
    @dropdownLS.setter
    def dropdownLS(self, dropdownLS):
        self._dropdownLS = dropdownLS
    @property
    def ddinner(self):
        return self._ddinner.get()
    @ddinner.setter
    def ddinner(self, ddinner):
        self._ddinner = ddinner
    @property
    def ddLSinner(self):
        return self._ddLSinner.get()
    @ddLSinner.setter
    def ddLSinner(self, ddLSinner):
        self._ddLSinner = ddLSinner
    @property
    def checkboxvar(self):
        return self._checkboxvar.get()
    #WORK

def addNewLine(line):
    
    #Button minus
    minusbutton = tk.Button(root, width=5, height=2, text="-", command=lambda: minusbutton_pressed(line))
    #label 
    type = tk.Label(root, text="Geth file path")
    type.bind("<Button-1>", lambda e:getFilepath(line))
    #name
    name = tk.Entry(root, width=40)
    #in
    inin = tk.Entry(root, width=5)
    #dropdown
    dropdown = tk.StringVar(root)
    dropdown.set(OptionList[0])
    opt = tk.OptionMenu(root, dropdown, *OptionList)
    dropdown.trace_add("write", dropdownchanged)
    print("Neues Dropdown wurde erstellt: " + dropdown.get())
    #label                                              +line darf nicht entfernt werden, da ERKENNUNG über diesen INT entsteht
    label_tmp =  tk.Label(root, text="Sicherung: " + str(line))
    #Automatenauswahl
    dropdownls = tk.StringVar(root)
    dropdownls.set(OptionListLS[0])
    optls = tk.OptionMenu(root, dropdownls, *OptionListLS)
    dropdownls.trace("w", dropdownchangedLS)
    #f
    checkboxvar = tk.IntVar()
    thermikcheckbox = tk.Checkbutton(root, text="Thermik", variable=checkboxvar)
    f = tk.Entry(root, width=40)
    r = Row(
        label = label_tmp,
        dropdown = opt,
        ddinner = dropdown,
        fileinput = type,
        nameinput = name,
        ininput = inin,
        x = 0, 
        y = 0,
        f = f, 
        buttonminus = minusbutton,
        row = 10 * line,
        dropdownLS = optls,
        ddLSinner = dropdownls,
        thermikcheckbox = thermikcheckbox,
        checkboxvar = checkboxvar
    )
    rowstack.append(r)
    #showRow(line)
    r.gridLS()
    print(r.dropdown)
    #OK




#INIT
plusbutton = tk.Button(root, width=5, height=2, text="+", command=lambda: plusbutton_pressed()).grid(row=999, column=3, sticky=tk.E)
questionbutton = tk.Button(root, width=5, height=2, text="?", command=lambda: question_button_pressed()).grid(row=999, column=0, sticky=tk.E)
questiconfigbutton = tk.Button(root, width=5, height=2, text="⚙", command=lambda: config_button_pressed()).grid(row=999, column=1, sticky=tk.E)
mybutton = tk.Button(root, width=5, height=2, text="Erstellen", command=lambda: doit_button_pressed()).grid(row=999, column=4,  sticky=tk.E)

config_button_pressed()
addNewLine(0)


#MAINLOOP
root.mainloop()