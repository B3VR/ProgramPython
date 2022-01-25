from tkinter import *
from tkinter import filedialog
import numpy as np
import TxtHelper

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure 
 
# Metody
def wczytajSygnal(): 
    
    path = filedialog.askopenfilename(initialdir="Sygnały", title="Wybierz plik")
    signal = TxtHelper.readSignalFromTxt(path)
    time = np.linspace(0, signal.measurmentTime, num= len(signal.samples))

    labelWarning.config(text=signal.warning)
    labelName.config(text=str(nazwaBadania + signal.name))
    labelTime.config(text=czasBadania + str(signal.measurmentTime) + " sekund")

    ax.clear()
    ax.set_xlabel("Czas [s]") 
    ax.set_ylabel("Amplituda sygnału")
    ax.plot(time, signal.samples, color='black') 

    canvas.draw()

# Gui
root = Tk() 
root.title("Przeglądarka sygnału EKG")
root.config(background='white') 
root.geometry("1300x630") 
     
labelWarning = Label(root, text="", font='Helvetica 12 bold', bg = 'white', fg="red" )
labelWarning.pack()

nazwaBadania = "Nazwa badania: "
labelName = Label(root, bg = 'white', font='Helvetica 12 bold', text=nazwaBadania, pady=3)
labelName.pack()

czasBadania = "Czas badania: "
labelTime = Label(root, bg = 'white', font='Helvetica 12 bold',text=czasBadania)
labelTime.pack()

fig = Figure() 
ax = fig.add_subplot(111) 
ax.set_xlabel("Czas [s]") 
ax.set_ylabel("Amplituda sygnału") 
 
canvas = FigureCanvasTkAgg(fig, master=root) 
canvas.get_tk_widget().pack(side="top",fill='both', expand=True)

toolBar = NavigationToolbar2Tk(canvas, root) 
toolBar.update()

canvas.get_tk_widget().pack(side="top",fill='both', expand=True)

  
btnWczytaj = Button(root, text="Wczytaj sygnał z pliku", command=wczytajSygnal, bg="white smoke", font=8, height=5, width=25)
btnWczytaj.pack(side="left")
     
root.mainloop() 

