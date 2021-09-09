from tkinter import *
from datetime import datetime
import os
import subprocess
import webbrowser
import pandas as pd

def Button_1():
    loc = (r'automation_groups.xlsx')

    df = pd.read_excel(loc,sheet_name='Foglio1')

    xl_key = df['key'[1]]



#GUI section

if os.name == "posix":
    fonts = ("Courier", 16)
    border='white'    
else:
    fonts = ("Courier", 12)
    border='black'


root = Tk()
root.geometry('428x926')

def clock():
    now = datetime.now()

    current_time = now.strftime("%H:%M")

    label_time = Label(root,text=current_time, font = ('ABeeZee',100),bg='#333B41', fg= 'white')
    label_time.place(x=45,y=100)
    label_time.after(1000,clock)

bg = PhotoImage(file='design.png')

label_bg = Label(root,image=bg)
label_bg.place(x=0,y=0,relwidth=1,relheight=1) 



clock()








root.mainloop()