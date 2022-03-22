import matplotlib.pyplot as plt
import numpy as np
import csv
import tkinter as tk
import random
import math

from tkinter import filedialog as fd
from tkinter import ttk
from os import X_OK
from numpy import Infinity

def toFloatTimesX(a, x):
    r = []
    for w in a:
        r.append(float(w)*int(x))
    return r
    #blöde scheiße
def isInRange(a):
    print(int(a))
    if a > 255:
        isInRange((a / 2))
    else: 
        return int(a)

def colorgetter():
    
    r = random.randint(0,510)
    g = random.randint(0,510)
    b = random.randint(0,510)

    r = isInRange(r)  
    g = isInRange(g)
    b = isInRange(b)

    print (r)

    color = ('#%02X%02X%02X' % (r, g, b))
    print(color)
    return color 
    


def draw_f(n):
    xlist = range(-100, 100, 1)
    ylist = []
    for x in xlist:
        ylist.append(pow(x, n))    
    color = colorgetter()
    plt.plot(xlist, ylist,color=color)

for x in range(0,100):
    draw_f(x)

plt.semilogx(2) #loglog
plt.semilogy(2) #loglog
plt.xlabel('I in Ampere')
plt.ylabel('t in s')
plt.grid(True, 'both', 'both') #grid für loglog mit (Visible, which, axis)
plt.legend(loc='upper right')
plt.show()