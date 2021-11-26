import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from array import array
import os


OptionList = [
"Leitungsschutzschalter",
"Schmelzsicherung",
"Funktion"
] 

def getFilepath(a, b):
    filename = fd.askopenfilename()
    if len(filename)<2:
        filename = "Hier ist etwas schief gelaufen.."
    fileinputstack[a][b].config(text=filename)
    #return filename

def getFilepathSchmelz(a):
    filename = fd.askopenfilename()
    if len(filename)<2:
        filename = "Hier ist etwas schief gelaufen.."
    schmelzsicherungstack[a].config(text=filename)
    #return filename

#root = Hauptfenster
root = tk.Tk()
root.geometry('550x800')

labelstack = []
dropdownstack = []
fileinputstack = [[],[]]
nameinputstack = [[],[]]
ininputstack = [[],[]]
buttonplusstack = []
buttonminusstack = []
variablestack = []

schmelzsicherungstack = [] 
schmelzsicherungnamestack = []

konstantstackx = []
konstantstacky = []
konstantstackf = []


def destroyLinePart(line):
    #line = line + 1
    print(line)
    fileinputstack[0][line-1].grid_remove()
    fileinputstack[1][line-1].grid_remove()
    nameinputstack[0][line-1].grid_remove()
    nameinputstack[1][line-1].grid_remove()
    ininputstack[0][line-1].grid_remove()
    ininputstack[1][line-1].grid_remove()
    schmelzsicherungnamestack[line-1].grid_remove()
    schmelzsicherungstack[line-1].grid_remove()
    konstantstackx[line-1].grid_remove()
    konstantstacky[line-1].grid_remove()
    konstantstackf[line-1].grid_remove()

def Schmelzsicherung(line):
    print("Schmelzsicherung Line: {}".format(line))
    destroyLinePart(line)
    print(schmelzsicherungnamestack)
    schmelzsicherungnamestack[line-1].grid(row=((line-1)*3)+1, column=2)
    schmelzsicherungstack[line-1].grid(row=((line-1)*3), column=1)

def Konstante(line):
    print("Konstante Line: {}".format(line))
    destroyLinePart(line)
    konstantstackx[line-1].grid(row=((line-1)*3), column=1)
    konstantstacky[line-1].grid(row=((line-1)*3)+1, column=1)
    konstantstackf[line-1].grid(row=((line-1)*3), column=2)
    konstantstackx[line-1].insert(0, "X")
    konstantstacky[line-1].insert(0, "Y")
    konstantstackf[line-1].insert(0, "Function")
    return 

def newFileinputSchmelzsicherung(n):
    n = int(n)
    label = tk.Label(root, text="Geth file path")
    label.bind("<Button-1>", lambda e:getFilepathSchmelz(n))
    schmelzsicherungstack.append(label)

def newFileinputSchmelzsicherungName():
    myInput = tk.Entry(root, width=40)
    schmelzsicherungnamestack.append(myInput)

def newKonstantx():
    myInput = tk.Entry(root, width=5)
    konstantstackx.append(myInput)

def newKonstanty():
    myInput = tk.Entry(root, width=5)
    konstantstacky.append(myInput)

def newKonstantf():
    myInput = tk.Entry(root, width=20)
    konstantstackf.append(myInput)

def newLabel(name):
    global labelstack
    label_tmp =  tk.Label(root, text=name)
    labelstack.append(label_tmp)

def newDropdown(line):
    variablestack.append(tk.StringVar(root))
    variablestack[line-1].set(OptionList[0])
    opt = tk.OptionMenu(root, variablestack[line-1], *OptionList)
    #opt.config(width=90, font=('Helvetica', 12))
    dropdownstack.append(opt)
    variablestack[line-1].trace("w", dropdownchanged)

def newFileinput(n):
    n = int(n)
    labelLinks = tk.Label(root, text="Geth file path")
    labelLinks.bind("<Button-1>", lambda e:getFilepath(0, n))
    fileinputstack[0].append(labelLinks)
    labelrechts = tk.Label(root, text="Geth file path")
    labelrechts.bind("<Button-1>", lambda e:getFilepath(1, n))  
    fileinputstack[1].append(labelrechts)

def newName():
    myInput0 = tk.Entry(root, width=40)
    nameinputstack[0].append(myInput0)
    myInput1 = tk.Entry(root, width=40)
    nameinputstack[1].append(myInput1)

def newIN():
    myInput0 = tk.Entry(root, width=5)
    ininputstack[0].append(myInput0)
    myInput1 = tk.Entry(root, width=5)
    ininputstack[1].append(myInput1)

def plusbutton_pressed():
    print(labelstack)
    addNewLine(len(labelstack))

def minusbutton_pressed(line):
    #todo ungrid all in line
    if line > 1:
        labelstack[line-1].grid_remove()
        dropdownstack[line-1].grid_remove()
        buttonplusstack[line-1].grid_remove()
        buttonminusstack[line-1].grid_remove()
        fileinputstack[0][line-1].grid_remove()
        fileinputstack[1][line-1].grid_remove()
        nameinputstack[0][line-1].grid_remove()
        nameinputstack[1][line-1].grid_remove()
        ininputstack[0][line-1].grid_remove()
        ininputstack[1][line-1].grid_remove()
        schmelzsicherungnamestack[line-1].grid_remove()
        schmelzsicherungstack[line-1].grid_remove()
        konstantstackx[line-1].grid_remove()
        konstantstacky[line-1].grid_remove()
        konstantstackf[line-1].grid_remove()


    #print(str(line))
    #print("labelstack"+str(labelstack),    "dropdownstack"+str(dropdownstack),    "fileinputstack"+str(fileinputstack),    "nameinputstack"+str(nameinputstack),    "ininputstack"+str(ininputstack),    "buttonplusstack"+str(buttonplusstack),    "buttonminusstack"+str(buttonminusstack))
    return

def makenewform(masterrow, function):
    if function == "Schmelzsicherung":
        Schmelzsicherung(masterrow)
    elif function == "Leitungsschutzschalter":
        Sicherungsautomat(masterrow, True)           ###############################
    elif function == "Funktion":
        Konstante(masterrow)
    print(masterrow, function)
    return

def dropdownchanged(*args):
    #print("X {}".format(args))
    row = 0
    if len(args[0])==7: row = int(args[0][len(args[0]) - 1]) 
    else: row = int(str(args[0][len(args[0])-2]) +  str(args[0][len(args[0]) - 1]))
    #labelstack[row].destroy()
    #print(variablestack[row].get())
    makenewform(row+1, variablestack[row].get())
    return

def newPlusbutton():
    mybutton = tk.Button(root, width=5, height=2, text="+", command=lambda: plusbutton_pressed())
    buttonplusstack.append(mybutton)

def newMinusbutton(line):
    mybutton = tk.Button(root, width=5, height=2, text="-", command=lambda: minusbutton_pressed(line))
    buttonminusstack.append(mybutton)

def addNewLine(line):
    line = line + 1
    newLabel("Sicherung " + str(line) + ":")
    newDropdown(line)   
    newFileinput(line-1)       # line-1 OR 0 #######################################################################################################
    newName()
    newIN()
    newPlusbutton()
    newMinusbutton(line)
    newFileinputSchmelzsicherungName()
    newFileinputSchmelzsicherung(line-1)
    newKonstantx()
    newKonstanty()
    newKonstantf()
    buttonminusstack[line-1].grid(row=((line-1)*3)+2, column=2, sticky=tk.E)
    buttonplusstack[line-1].grid(row=((line-1)*3)+2, column=3)
    dropdownstack[line-1].grid(row=((line-1)*3)+1, column=0)
    Sicherungsautomat(line, False)

def Sicherungsautomat(line, change):
    if change == True:
        destroyLinePart(line)
    print("Sicherungsautomat Line: {}".format(line))
    linerow = line #################################################
    labelstack[line-1].grid(row=(linerow-1)*3, column=0)
    fileinputstack[0][line-1].grid(row=(linerow-1)*3, column=1)
    fileinputstack[1][line-1].grid(row=((linerow-1)*3)+1, column=1)
    nameinputstack[0][line-1].grid(row=(linerow-1)*3, column=2)
    nameinputstack[1][line-1].grid(row=((linerow-1)*3)+1, column=2)
    ininputstack[0][line-1].grid(row=(linerow-1)*3, column=3)
    ininputstack[1][line-1].grid(row=((linerow-1)*3)+1, column=3)
    if change == False:
        ininputstack[0][line-1].insert(0, "I/A")
        ininputstack[1][line-1].insert(0, "I/A")

    return

    






addNewLine(0)
addNewLine(1)
#Starte mainloop
root.mainloop()