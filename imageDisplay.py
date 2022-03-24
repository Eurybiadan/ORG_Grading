import matplotlib.pyplot as plt
import csv
import torch
import numpy as np

from tkinter import *
from tkinter import ttk

ws= Tk()

ws.title("PythonGuides")
ws.geometry('400x300')
ws['bg'] = '#ffbf00'

# great example of embedding matlab plot into tkinter gui
# https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/

# ask for file directory: https://stackoverflow.com/questions/11295917/how-to-select-a-directory-and-store-the-location-using-tkinter-in-python

# To Do:
#   - get matlab plot embedded into tkinter gui using link above
#   - get file directory from user instead of setting variable directly to it
#   - store user response in general based on what the graph looks like

def printValue():
    pname = player_name.get()
    Label(ws, text=f'{pname}, Registered!', pady=20, bg='#ffbf00').pack()


player_name = Entry(ws)
player_name.pack(pady=30)

Button(
    ws,
    text="Register Player",
    padx=10,
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()

path = "C:\\Users\\grohd\\Downloads\\(-1,-0.2)\\00-33388_20210924_OS_(-1,-0.2)_1x1_789_760nm1_extract_reg_cropped_piped_profiles.csv"

numpy_data = np.loadtxt(path, dtype= np.float, delimiter=",", skiprows=1)

# converting data to
# print(data.shape) # making sure i have all the data
print((numpy_data))


# this is useful: https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image

for i in range(6): #numpy_data:
   plt.plot(numpy_data[:,i])
   plt.title(i)
   plt.show()

