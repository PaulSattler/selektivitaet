import tkinter as tk
import matplotlib as plt
import numpy as np
from matplotlib.pyplot import Figure
plt.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  

class Plotwindow():
    def __init__(self, masterframe, size): 
        
        (w,h)=size    
        inchsize=(w/25.4, h/25.4)
        self.figure = Figure(inchsize)
        self.axes = self.figure.add_subplot(111)
        
        # create canvas as matplotlib drawing area
        self.canvas = FigureCanvasTkAgg(self.figure, master=masterframe)
        self.canvas.get_tk_widget().pack()
        
    def plotxy(self, x, y):
        self.axes.plot(x,y)
        self.canvas.draw()    
        
    def clearplot(self):
        self.axes.cla()
        self.canvas.draw()

class Generatetestdata():
    def __init__(self):
        self.index=0        # index of function call
        self.xmin=0.0
        self.xmax=10.0
        self.nbvalues=500
    def getxy(self):
        n=self.index
        x=np.linspace(self.xmin, self.xmax, self.nbvalues)
        y=np.sin(4*x)*np.exp(-n*x/10)
        self.index+=1   
        self.xmax+=5.0 
        return x,y

def plotdata():
    x,y=datgen.getxy()
    pw.plotxy(x,y)
    
def clear():
    pw.clearplot()

print(__name__)
if __name__ == "__main__":  
   
    datgen = Generatetestdata()
    
    root = tk.Tk()
    
    mf= tk.Frame()
    pw=Plotwindow(mf,(200,150))
    mf.pack()
      
    
    bf=tk.Frame()
    b1=tk.Button(bf,text="Plot", command=plotdata)
    b1.pack(side=tk.LEFT)
    b2=tk.Button(bf,text="Clear", command=clear)
    b2.pack(side=tk.LEFT)
    bf.pack()
    
    root.mainloop()