


########################################################################




def Schmelzsicherungplot(Karakteristik, In, Name, x_in, y_in):
    x = toFloatTimesX(x_in, 1)
    y = toFloatTimesX(y_in, 1)
    labelL = Name
    plt.plot(x, y, label = labelL)



def functionplot(Name, f):
    x = np.linspace(0, 10000, 10000)
    y = exec(f)
    #exec
    plt.plot(x, y, label = str(Name))






##TKINTER

def doit_button_pressed():
    #Finde, welche aktiv sind
    for dropdown in dropdownstack:
        if dropdown.winfo_ismapped() == True:
            x = dropdownstack.index(dropdown)
            if variablestack[x].get() == "Leitungsschutzschalter":
                file0 = fileinputstack[0][x].cget("text")
                file1 = fileinputstack[1][x].cget("text")
                name0 = nameinputstack[0][x].get()
                name1 = nameinputstack[1][x].get()
                in0 = ininputstack[0][x].get()
                in1 = ininputstack[1][x].get()
                xL, yL = ReadDataSheet(file0)
                xR, yR = ReadDataSheet(file1)
                Automatplot("Karaktaristik", in0, name0, name1, xL, xR, yL, yR)
            elif variablestack[x].get() == "Schmelzsicherung":
                file = schmelzsicherungstack[x].cget("text")
                xL, yL = ReadDataSheet(file)
                name = schmelzsicherungnamestack[x].get()
                Schmelzsicherungplot("", 1, name, xL, yL)
                #schmelzsicherung
            elif variablestack[x].get() == "Funktion":
                x1 = konstantstackx[x].get()
                y1 =konstantstacky[x].get()
                f1 = konstantstackf[x].get()
                if f1 != "":
                    functionplot(str(f1), str(f1))

    showIt()



#Wandelt jeden a in einen float(a) um und mutlipliziert mit x


def Automatplot(Karakteristik, In, Name1, Name2, xL_in, xR_in, yL_in, yR_in):
    xL = toFloatTimesX(xL_in, In)
    xR = toFloatTimesX(xR_in, In)
    yL = toFloatTimesX(yL_in, 1)
    yR = toFloatTimesX(yR_in, 1)
    labelL = str(Name1) + "  mit " + str(In) + "A, Min"
    labelR = str(Name2) + "  mit "  + str(In) + "A, Max"
    plt.plot(xL, yL, label = labelL)
    plt.plot(xR, yR, label = labelR)

def Replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")
#kann eine txt oder csv datei einlesen, format x;y \n x;y \n ...
def ReadDataSheet(file):
    x = []
    y = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='\\')
        for row in reader:
            x.append(Replace(row[0]))
            y.append(Replace(row[1]))
        return x, y


def addNewLine(line):
    line = line + 1
    newLabel("Sicherung " + str(line) + ":")
    newDropdown(line)   
    newFileinput(line-1)
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

    def newPlusbutton():
    mybutton = tk.Button(root, width=5, height=2, text="+", command=lambda: plusbutton_pressed())
    buttonplusstack.append(mybutton)

def newMinusbutton(line):
    mybutton = tk.Button(root, width=5, height=2, text="-", command=lambda: minusbutton_pressed(line))
    buttonminusstack.append(mybutton)
def Sicherungsautomat(line, change):
    if change == True:
        destroyLinePart(line)
    linerow = line
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


def newFileinput(n):
    n = int(n)
    labelLinks = tk.Label(root, text="Geth file path")
    labelLinks.bind("<Button-1>", lambda e:getFilepath(0, n))
    fileinputstack[0].append(labelLinks)
    labelrechts = tk.Label(root, text="Geth file path")
    labelrechts.bind("<Button-1>", lambda e:getFilepath(1, n))  
    fileinputstack[1].append(labelrechts)


    def makenewform(masterrow, function):
    if function == "Schmelzsicherung":
        Schmelzsicherung(masterrow)
    elif function == "Leitungsschutzschalter":
        Sicherungsautomat(masterrow, True)
    elif function == "Funktion":
        Konstante(masterrow, True)

def dropdownchanged(*args):
    row = 0
    if len(args[0])==7: row = int(args[0][len(args[0]) - 1]) 
    else: row = int(str(args[0][len(args[0])-2]) +  str(args[0][len(args[0]) - 1]))
    #print(row)
    makenewform(row+1, variablestack[row].get())


def plusbutton_pressed():
    addNewLine(len(labelstack))

def minusbutton_pressed(line):
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

def destroyLinePart(line):
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
    destroyLinePart(line)
    schmelzsicherungnamestack[line-1].grid(row=((line-1)*3)+1, column=2)
    schmelzsicherungstack[line-1].grid(row=((line-1)*3), column=1)

def Konstante(line, change):
    destroyLinePart(line)
    konstantstackx[line-1].grid(row=((line-1)*3), column=1)
    konstantstacky[line-1].grid(row=((line-1)*3)+1, column=1)
    konstantstackf[line-1].grid(row=((line-1)*3), column=2)
    if change == True:
        konstantstackx[line-1].insert(0, "X")
        konstantstacky[line-1].insert(0, "Y")
        konstantstackf[line-1].insert(0, "Function")

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
    dropdownstack.append(opt)
    variablestack[line-1].trace("w", dropdownchanged)



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




def getFilepath(a, b):
    filename = fd.askopenfilename()
    if len(filename)<2:
        filename = "Hier ist etwas schief gelaufen.."
    fileinputstack[a][b].config(text=filename)

def getFilepathSchmelz(a):
    filename = fd.askopenfilename()
    if len(filename)<2:
        filename = "Hier ist etwas schief gelaufen.."
    schmelzsicherungstack[a].config(text=filename)




