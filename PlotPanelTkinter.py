from tkinter import *
from tkinter import filedialog
import tkinter
import numpy as np 
import TxtHelper

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure 
 
# Metody
def wczytaj_sygnal(): 
    
    path = filedialog.askopenfilename(initialdir="Sygnały", title="Wybierz plik")
    signal = TxtHelper.readSignalFromTxt(path)
    time = np.linspace(0, signal.measurmentTime, num= len(signal.samples))

    warning.set(signal.warning)

    ax.clear()
    ax.set_xlabel("Czas [s]") 
    ax.set_ylabel("Amplituda sygnału")
    ax.plot(time, signal.samples, color='black') 

    canvas.draw()

# Gui
root = Tk() 
root.config(background='white') 
root.geometry("1300x600") 
     
warning = tkinter.StringVar()
lab = Label(root, text=warning, bg = 'white').pack()

fig = Figure() 
     
ax = fig.add_subplot(111) 
ax.set_xlabel("Czas [s]") 
ax.set_ylabel("Amplituda sygnału") 
 
canvas = FigureCanvasTkAgg(fig, master=root) 
canvas.get_tk_widget().pack(side="top",fill='both', expand=True)

toolBar = NavigationToolbar2Tk(canvas, root) 
toolBar.update()

canvas.get_tk_widget().pack(side="top",fill='both', expand=True)

  
b = Button(root, text="Wczytaj sygnal z pliku", command=wczytaj_sygnal, bg="white")
b.pack(side="left")
     
root.mainloop() 

