from tkinter import *
from datetime import datetime
import os
import subprocess
import webbrowser
import pandas as pd

loc = (r'automation_groups.xlsx')

def Button_1(excel_path):
    
    df = pd.read_excel(excel_path,sheet_name='Button1')

    xl_key = list(df['actions'])


def Button_2(excel_path):
    
    df = pd.read_excel(excel_path,sheet_name='Button2')

    xl_key = list(df['actions'])

    for element in xl_key:
        if 'http' in element:
            webbrowser.open(element)
        else:
            pass
def Button_3(excel_path):
    
    df = pd.read_excel(excel_path,sheet_name='Button3')

    xl_key = list(df['actions'])


def Button_4(excel_path):
    
    df = pd.read_excel(excel_path,sheet_name='Button4')

    xl_key = list(df['actions'])


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
b1 = PhotoImage(file='study_icon.png')
b2 = PhotoImage(file='work_icon.png')
b3 = PhotoImage(file='streaming_icon.png')

label_bg = Label(root,image=bg)
label_bg.place(x=0,y=0,relwidth=1,relheight=1) 



clock()


Button_study = Button(image=b1,bg='#333B41',command= Button_2(loc),borderwidth=0)
Button_study.place(x=50,y=650)

Button_streaming = Button(image=b3,bg='#333B41',command= Button_3,borderwidth=0)
Button_streaming.place(x=250,y=650)

Button_work = Button(image=b2,bg='#333B41',command= Button_3,borderwidth=0)
Button_work.place(x=50,y=450)







root.mainloop()