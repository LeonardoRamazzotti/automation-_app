
# MODULE SECTION -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from datetime import datetime
from openpyxl import load_workbook
import os
import subprocess
import webbrowser
import pandas as pd
import pathlib
import pyperclip

#Funciton Section-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Button_1(excel_path):   #Work icon function
    
    df = pd.read_excel(excel_path,sheet_name='Button1')

    xl_key = list(df['actions'])

    for element in xl_key:
        if 'http' in element:
            webbrowser.open(element)
        else:
            subprocess.Popen(element)



def Button_2(excel_path):   #Study icon function
    
    df = pd.read_excel(excel_path,sheet_name='Button2')

    xl_key = list(df['actions'])

    for element in xl_key:
        if 'http' in element:
            webbrowser.open(element)
        else:
            subprocess.Popen(element)

def Button_3(excel_path):  #Code Icon function
    
    df = pd.read_excel(excel_path,sheet_name='Button3')

    xl_key = list(df['actions'])

    for element in xl_key:
        if 'http' in element:
            webbrowser.open(element)
        else:
            subprocess.Popen(element)



def Button_4(excel_path):  # Streaming icon function
    
    df = pd.read_excel(excel_path,sheet_name='Button4')

    xl_key = list(df['actions'])

    for element in xl_key:
        if 'http' in element:
            webbrowser.open(element)
        else:
            subprocess.Popen(element)

def clock():   #Clock function
    now = datetime.now()

    current_time = now.strftime("%H:%M")

    label_time = Label(root,text=current_time, font = ('ABeeZee',100),bg='#333B41', fg= '#757778')
    label_time.place(x=42,y=100)
    label_time.after(1000,clock)


def daytime():  # Daydate function

    now = datetime.now()
    currentday = now.strftime('%d/%m/%Y')

    label_day = Label(root,text=currentday, font = ('ABeeZee',20),bg='#202329', fg= '#757778')
    label_day.place(x=42,y=22)
    label_day.after(10000,clock)


def Copy_path(file): #copy the label path on settings

    pyperclip.copy(file)
    

def Settings():  # Setting Windows 
    setting_window = Toplevel(root)

    setting_window.title('Settings')
    setting_window.geometry('700x600')
    setting_window.config(bg='#333B41')

    Label_1 = Label(setting_window,text='Modify Launchers:',font = ('ABeeZee',14),bg='#333B41', fg= 'white')
    Label_1.place(x=10,y=10)

    path = str(pathlib.Path(__file__).parent.resolve())
    path_main = path.replace('test','')
    
    file_path = path+'/automation_groups.xlsx'

    Label_path = Label(setting_window,text=file_path,font = ('ABeeZee',11),bg='#333B41', fg= 'white')
    Label_path.place(x=15,y=50)

    Button_copy = Button(setting_window,text='Copy',font = ('ABeeZee',10),bg='#333B41', fg= 'white',command= lambda:Copy_path(file_path))
    Button_copy.place(x=550,y=45)

    Readme_label = Label(setting_window,text='Info Version:',font = ('ABeeZee',14),bg='#333B41', fg= 'white')
    Readme_label.place(x=10,y=500)

    Label_info = Label(setting_window,text='Copyright Leonardo Ramazzotti 2021',font = ('ABeeZee',12),bg='#333B41', fg= 'white')
    Label_info.place(x=15,y=550)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

#GUI section -END----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if os.name == "posix":
    fonts = ("Courier", 16)
    border='white'    
else:
    fonts = ("Courier", 12)
    border='black'

#Window Settings-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root = Tk()
root.title('Shortcut')
root.geometry('428x926')
root.resizable(False, False)

#Image Section ---------------------------------------------------------------------------------------------------------------------------------------------------------

bg = PhotoImage(file='design.png')
b1 = PhotoImage(file='study_icon.png')
b2 = PhotoImage(file='work_icon.png')
b3 = PhotoImage(file='streaming_icon.png')
b4 = PhotoImage(file= 'code_icon.png')
bsettings = PhotoImage(file='settings_icon.png')

#Background Settings----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

label_bg = Label(root,image=bg)
label_bg.place(x=0,y=0,relwidth=1,relheight=1) 

#Calling Date and time Function ------------------------------------------------------------------------------------------------------------------------------------------------------

clock()
daytime()

# Button Groups Section ----------------------------------------------------------------------------------------------------------------------------------------------------------

Button_study = Button(image=b1,bg='#333B41',command= lambda: Button_2(loc),borderwidth=0)
Button_study.place(x=55,y=650)

Button_streaming = Button(image=b3,bg='#333B41',command= lambda: Button_4(loc),borderwidth=0)
Button_streaming.place(x=275,y=650)

Button_work = Button(image=b2,bg='#333B41',command= lambda: Button_1(loc),borderwidth=0) 
Button_work.place(x=55,y=450)

Button_code = Button(image=b4,bg='#333B41',command= lambda: Button_4(loc),borderwidth=0)
Button_code.place(x=275,y=448)


Button_settings = Button(root,image = bsettings,bg='#202329',command= Settings ,borderwidth=0)
Button_settings.place(x=350,y=20)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()