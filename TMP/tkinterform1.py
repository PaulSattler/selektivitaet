import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd
from array import array


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
    addNewLine(len(labelstack)+1)

def minusbutton_pressed(line):
    #todo ungrid all in line
    if line > 1:
        labelstack[line-1].destroy()
        dropdownstack[line-1].destroy()
        fileinputstack[0][line-1].destroy()
        fileinputstack[1][line-1].destroy()
        nameinputstack[0][line-1].destroy()
        nameinputstack[1][line-1].destroy()
        ininputstack[0][line-1].destroy()
        ininputstack[1][line-1].destroy()
        buttonplusstack[line-1].destroy()
        buttonminusstack[line-1].destroy()
    #print(str(line))
    #print("labelstack"+str(labelstack),    "dropdownstack"+str(dropdownstack),    "fileinputstack"+str(fileinputstack),    "nameinputstack"+str(nameinputstack),    "ininputstack"+str(ininputstack),    "buttonplusstack"+str(buttonplusstack),    "buttonminusstack"+str(buttonminusstack))
    return

def makenewform(masterrow, function):
    print(masterrow, function)
    return

def dropdownchanged(*args):
    #print("X {}".format(args))
    row = 0
    if len(args[0])==7: row = int(args[0][len(args[0]) - 1]) 
    else: row = int(str(args[0][len(args[0])-2]) +  str(args[0][len(args[0]) - 1]))
    #labelstack[row].destroy()
    #print(variablestack[row].get())
    makenewform(row, variablestack[row].get())
    return

def newPlusbutton():
    mybutton = tk.Button(root, width=5, height=2, text="+", command=lambda: plusbutton_pressed())
    buttonplusstack.append(mybutton)

def newMinusbutton(line):
    mybutton = tk.Button(root, width=5, height=2, text="-", command=lambda: minusbutton_pressed(line))
    buttonminusstack.append(mybutton)

def addNewLine(line):
    newLabel("Sicherung " + str(line) + ":")
    labelstack[len(labelstack)-1].grid(row=(line-1)*3, column=0)

    newDropdown(line)
    dropdownstack[len(dropdownstack)-1].grid(row=((line-1)*3)+1, column=0)

    newFileinput(0)
    fileinputstack[0][len(fileinputstack[0])-1].grid(row=(line-1)*3, column=1)
    fileinputstack[1][len(fileinputstack[1])-1].grid(row=((line-1)*3)+1, column=1)
    
    newName()
    nameinputstack[0][len(nameinputstack[0])-1].grid(row=(line-1)*3, column=2)
    nameinputstack[1][len(nameinputstack[1])-1].grid(row=((line-1)*3)+1, column=2)

    newIN()
    ininputstack[0][len(ininputstack[0])-1].grid(row=(line-1)*3, column=3)
    ininputstack[0][len(ininputstack[0])-1].insert(0, "I/A")
    ininputstack[1][len(ininputstack[1])-1].grid(row=((line-1)*3)+1, column=3)
    ininputstack[1][len(ininputstack[1])-1].insert(0, "I/A")
    
    newPlusbutton()
    buttonplusstack[line-1].grid(row=((line-1)*3)+2, column=3)

    newMinusbutton(line)
    buttonminusstack[line-1].grid(row=((line-1)*3)+2, column=2, sticky=tk.E)

    











addNewLine(1)
#Starte mainloop
root.mainloop()