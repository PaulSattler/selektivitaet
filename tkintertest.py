import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog as fd



def button_click():
    filename = fd.askopenfilename()
    print(filename)

def callback(*args):
    #labelTest.configure(text="The selected item is {}".format(variable.get()))
    #print(variable.get())
    if variable.get() == "Leitungsschutzschalter":
        drawAutomat(False)
    elif variable.get() == "Schmelzsicherung Neozed":
        drawAutomat(True)

def drawAutomat(delete):
    if delete == False:
        labelLinks.place(x=100, y=100)
    else:
        labelLinks.place_forget()

OptionList = [
"Leitungsschutzschalter",
"Schmelzsicherung Neozed",
"Schmelzsicherung Diazed",
"Thermik",
"Funktion",
"Konstante"
] 

root = tk.Tk()
root.title("Selektivität")
root.geometry("800x500")
root.resizable(width=False, height=False)
#label1 = tk.Label(root, text="Test", bg="green")
#label1.place(x=0, y=0, width=100)


labelLinks = tk.Label(root, text="Geth file path")
labelLinks.bind("<Button-1>", lambda e:button_click())

button1 = tk.ttk.Button(root, text="TEst", command=button_click)
button1.place(x=0, y=100, width=100)


label1 = tk.ttk.Label(root, text="Fuse 1:")
label1.place(x=0, y=30)


variable = tk.StringVar(root)
variable.set(OptionList[0])
opt = tk.OptionMenu(root, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.place(x=60, y=20, width=300)





variable.trace("w", callback)
#drawAutomat(False)

root.mainloop()
