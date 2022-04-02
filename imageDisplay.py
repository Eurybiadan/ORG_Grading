import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import csv
import torch
import numpy as np
import os

from tkinter import *
from tkinter import ttk, filedialog


ws= Tk()


# To Do:
#   - store user response in general based on what the graph looks like
#   - organize and comment code

def keyPress(event):
    key = event.char
    print(key, 'is pressed')

    with open(outputNum+'_output_values.csv', 'a') as file:
        file.write(key)
        file.write(',\n')


def printValue():

    #path = "C:\\Users\\grohd\\Downloads\\(-1,-0.2)\\00-33388_20210924_OS_(-1,-0.2)_1x1_789_760nm1_extract_reg_cropped_piped_profiles.csv"

    # askopenfilename will be changed to askdirectory
    pName = filedialog.askopenfilename(title="Select the folder containing all data of interest.")

    numpy_data = np.loadtxt(pName, dtype=np.float, delimiter=",", skiprows=1)

    plot = Figure(figsize = (5,5), dpi=100)
    plotGraph = plot.add_subplot(111)

    seqNum = pName
    (head, seqNum) = os.path.split(seqNum)
    parseTemp = seqNum.split(("_"))
    global outputNum
    outputNum = parseTemp[5]

    num_rows, num_cols = numpy_data.shape

    i = 0
    while i <= num_rows:
        print(i)
        i = i + 1
        plotGraph.plot((numpy_data[i, :]))
    ws.bind('<Key>', keyPress)


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


# references:
# https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image
# https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python
# https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/
# https://stackoverflow.com/questions/58186325/tkinter-not-waiting-for-user-input-inside-functions
# https://www.geeksforgeeks.org/python-binding-function-in-tkinter/