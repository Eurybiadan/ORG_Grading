import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import csv
import torch
import numpy as np

from tkinter import *
from tkinter import ttk, filedialog


ws= Tk()


# great example of embedding matlab plot into tkinter gui
# https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/

# ask for file directory: https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python

# To Do:
#   - get matlab plot embedded into tkinter gui using link above
#   - get file directory from user instead of setting variable directly to it
#   - store user response in general based on what the graph looks like

def printValue():

    #path = "C:\\Users\\grohd\\Downloads\\(-1,-0.2)\\00-33388_20210924_OS_(-1,-0.2)_1x1_789_760nm1_extract_reg_cropped_piped_profiles.csv"

    #
    pName = filedialog.askopenfilename(title="Select the folder containing all data of interest.")

    numpy_data = np.loadtxt(pName, dtype=np.float, delimiter=",", skiprows=1)

    plot = Figure(figsize = (5,5), dpi=100)
    plotGraph = plot.add_subplot(111)

    plotGraph.plot((numpy_data[:,1]))

    canvas = FigureCanvasTkAgg(plot, master=ws)
    canvas.draw()

    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, ws)
    toolbar.update()
    canvas.get_tk_widget().pack()


ws.title('Hello')
ws.geometry("500x500")

plot_button = Button(master = ws,
                     command = printValue,
                     height = 2,
                     width = 10,
                     text = "Get directory")

plot_button.pack()

ws.mainloop()


# this is useful: https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image

#for i in range(6): #numpy_data:
#   plt.plot(numpy_data[:,i])
#   plt.title(i)
#   plt.show()

