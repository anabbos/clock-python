from tkinter import *
from time import *

window.Tk()
window.title("Clock")

time_label = Label(window,font=("Arial",50),fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window,font=("Ink Free",25))
day_label.pack()

date_label = Label(window,font=("Ink Free", 30))
date_label.pack()

window.mainloop()