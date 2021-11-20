from os import X_OK
from numpy import Infinity
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math 
from scipy.ndimage.filters import gaussian_filter1d
import csv


Sigma = 1

def toFloatTimesX(a, x):
    r = []
    for w in a:
        r.append(float(w)*int(x))
    return r

def Replace(str1):
    maketrans = str1.maketrans
    final = str1.translate(maketrans(',.', '.,', ' '))
    return final.replace(',', ", ")

def ReadDataSheet(file):
    x = []
    y = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='\\')
        for row in reader:
            x.append(Replace(row[0]))
            y.append(Replace(row[1]))
        return x, y

def Schmelzsicherung(Karakteristik, In, Name, x_in, y_in):
    x = toFloatTimesX(x_in, 1)
    y = toFloatTimesX(y_in, 1)
    labelL = Name
    plt.plot(x, y, label = labelL)

def Automat(Karakteristik, In, Name, xL_in, xR_in, yL_in, yR_in):
    xL = toFloatTimesX(xL_in, In)
    xR = toFloatTimesX(xR_in, In)
    yL = toFloatTimesX(yL_in, 1)
    yR = toFloatTimesX(yR_in, 1)
    labelL = str(Karakteristik) + " Automat mit " + str(In) + "A, Min"
    labelR = str(Karakteristik) + " Automat mit " + str(In) + "A, Max"
    plt.plot(xL, yL, label = labelL)
    plt.plot(xR, yR, label = labelR)

def Thermik(In, Name, x, y):
    xT = toFloatTimesX(x, In)
    yT = toFloatTimesX(y, 1)
    labelT = "Thermik " +str(In) + "A" + "; "+ str(Name)
    plt.plot(xT, yT, label = labelT)




xL, yL = ReadDataSheet("CSV00001_B_Links.txt")
xR, yR = ReadDataSheet("CSV00001_B_Rechts.txt")
Automat("B", 16, "Erster Automat", xL, xR, yL, yR)
xT, yT = ReadDataSheet("Thermik.txt")
Thermik(16, "Thermik 1", xT, yT)



plt.xlabel('I in Ampere')
plt.ylabel('T in s')
plt.title("Selektivität",fontsize=16)

plt.semilogx(2) #loglog
plt.semilogy(2) #loglog

plt.grid(True, 'both', 'both') #grid für loglog mit (Visible, which, axis)

plt.legend(loc='upper right')
plt.show()