import matplotlib.pyplot as plt
import csv
import torch
import numpy as np

from tkinter import *
from tkinter import ttk

win= Tk()

#Set the geometry of Tkinter frame
win.geometry("500x250")

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Press button",width= 20, command= display_text).pack(pady=20)


#win.mainloop()

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