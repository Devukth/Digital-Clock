from tkinter import *
from tkinter.ttk import *

from time import *

window = Tk()
window.title("Digital Clock")

label = Label(window, font = ("sans", 40), background = "blue", foreground = "orange")
label.pack(anchor = "center")

def clock():
    hours = int(strftime("%H"))
    if(strftime("%p") == "PM"):
        hours -= 12
    
    time_text = strftime(f"{hours}:%M %p")
    label.config(text = time_text)
    label.after(1000, clock)

clock()

mainloop()