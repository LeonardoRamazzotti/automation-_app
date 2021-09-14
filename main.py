
# MODULE SECTION -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from datetime import datetime
from openpyxl import load_workbook
from subprocess import call
import webbrowser
from bs4 import BeautifulSoup
import requests
import os
import subprocess
import webbrowser
import pandas as pd
import pathlib
import pyperclip

#Funciton Section-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Button_1(excel_path):   #Work icon function
    
    df = pd.read_excel(excel_path,sheet_name='Work')

    xl_key = list(df['actions'])

    for element in xl_key:
        if 'http' in element:
            webbrowser.open(element)
        else:
            subprocess.Popen(element)



def Button_2(excel_path):   #Study icon function
    
    df = pd.read_excel(excel_path,sheet_name='Study')

    xl_key = list(df['actions'])

    for element in xl_key:
        if 'http' in element:
            webbrowser.open(element)
        else:
            subprocess.Popen(element)

def Button_3(excel_path):  #Code Icon function
    
    df = pd.read_excel(excel_path,sheet_name='Code')

    xl_key = list(df['actions'])

    for element in xl_key:
        if 'http' in element:
            webbrowser.open(element)
        else:
            subprocess.Popen(element)



def Button_4(excel_path):  # Streaming icon function
    
    df = pd.read_excel(excel_path,sheet_name='Streaming')

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
    label_day.after(10000,daytime)


def Copy_path(file): #copy the label path on settings

    pyperclip.copy(file)



def weather(link,head):   # funzione che fa web scraping e cerca meteo nella posizione corrente

    page = requests.get(link, headers=head)
    soup = BeautifulSoup(page.content, 'html.parser')

    condizione = str(soup.find(id='wob_dc').get_text())
    Luogo = str(soup.find(id='wob_loc').get_text())

    wind_speed = str(soup.find(id='wob_ws').get_text()) # da rivedere wind speed , temp and rainfall percentage
    rainfall = str(soup.find(id='wob_pp').get_text())

    temp = str(soup.find(id='wob_tm').get_text())

    
    
    
    if condizione == 'Soleggiato' or condizione == 'Sereno':
        weather_img =weather_sunny
    
    
    elif condizione == 'Parzialmente nuvoloso'or condizione == 'Per lo più soleggiato':
        weather_img =weather_par_cloudy
    

    elif condizione == 'Temporale':
        weather_img =weather_temp



    elif condizione == 'Rovesci' or condizione == 'Pioggia':
        weather_img =weather_rainy
    
    
    
    elif condizione == 'Rovesci nevosi':
        weather_img =weather_snowing
    
    
    elif condizione == 'Grandine':
        weather_img =weather_hailstorm
    
    
    Label_Weather = Label(root, image = weather_img,bg='#333B41')
    Label_Weather.place(x=20,y=285)    

    Label_luogo = Label(root, text=Luogo,font = ('ABeeZee',18),bg='#333B41', fg= '#757778' )
    Label_luogo.place(x=220,y=290)

    Label_wind = Label(root,text='Wind:'+wind_speed,font = ('ABeeZee',12),bg='#333B41', fg= '#757778' )
    Label_wind.place(x=100,y=295)
    
    Label_rainfall = Label(root,text='Raifall:'+rainfall,font = ('ABeeZee',12),bg='#333B41', fg= '#757778')
    Label_rainfall.place(x=100,y=315)

    Label_temp = Label(root,text=temp+'°C',font = ('ABeeZee',28),bg='#202329', fg= '#757778')
    Label_temp.place(x=220,y=14)


    Label_cond =Label(root, text=condizione,font = ('ABeeZee',12),bg='#333B41', fg= '#757778' )
    Label_cond.place(x=220,y=320)

    

def VolumeUp(): #Volume Control UP
    

    call(["amixer","-D","pulse","sset","Master","10%+"])
    
def VolumeDown(): #Volume Control Down
    
     call(["amixer","-D","pulse","sset","Master","10%-"])
     
 
     
def Mute():  #Volume Control Mute
    
     call(["amixer","-D","pulse","sset","Master","100%-"])
    

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
root.title('Control Center')
root.geometry('428x926')
root.resizable(False, False)

#Image Section ---------------------------------------------------------------------------------------------------------------------------------------------------------

bg = PhotoImage(file='design.png')
b1 = PhotoImage(file='study_icon.png')
b2 = PhotoImage(file='work_icon.png')
b3 = PhotoImage(file='streaming_icon.png')
b4 = PhotoImage(file= 'code_icon.png')
bsettings = PhotoImage(file='settings_icon.png')

volumeup = PhotoImage(file='volumeup.png')
volumedown = PhotoImage(file='volumedown.png')
mute = PhotoImage(file='mute.png')

weather_sunny = PhotoImage(file='sunny.png')
weather_cloudy = PhotoImage(file='cover.png')
weather_rainy = PhotoImage(file='rain.png')
weather_temp = PhotoImage(file='temporal.png')
weather_hailstorm = PhotoImage(file='hailstorm.png')
weather_snowing = PhotoImage(file='snow.png')
weather_par_cloudy = PhotoImage(file='par_cloudy.png')

#Background Settings----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

label_bg = Label(root,image=bg)
label_bg.place(x=0,y=0,relwidth=1,relheight=1) 

#Calling Date and time Function ------------------------------------------------------------------------------------------------------------------------------------------------------

clock()
daytime()

# Button Groups Section ----------------------------------------------------------------------------------------------------------------------------------------------------------

Label_study=Label(root,text='Study',font = ('ABeeZee',16),bg='#333B41', fg= '#757778')
Label_study.place(x=55,y=600)

Button_study = Button(image=b1,bg='#333B41',command= lambda: Button_2(loc),highlightthickness = 0,borderwidth=0)
Button_study.place(x=55,y=650)

Label_streaming=Label(root,text='Streaming',font = ('ABeeZee',16),bg='#333B41', fg= '#757778')
Label_streaming.place(x=275,y=600)

Button_streaming = Button(image=b3,bg='#333B41',command= lambda: Button_4(loc),highlightthickness = 0,borderwidth=0)
Button_streaming.place(x=275,y=650)

Label_work=Label(root,text='Work',font = ('ABeeZee',16),bg='#333B41', fg= '#757778')
Label_work.place(x=55,y=400)

Button_work = Button(image=b2,bg='#333B41',command= lambda: Button_1(loc),highlightthickness = 0,borderwidth=0) 
Button_work.place(x=55,y=450)

Label_code=Label(root,text='Code',font = ('ABeeZee',16),bg='#333B41', fg= '#757778')
Label_code.place(x=275,y=400)

Button_code = Button(image=b4,bg='#333B41',command= lambda: Button_4(loc),highlightthickness = 0,borderwidth=0)
Button_code.place(x=275,y=445)


Button_settings = Button(root,image = bsettings,bg='#202329',command= Settings ,highlightthickness = 0,borderwidth=0)
Button_settings.place(x=350,y=20)


volumeupButton = Button(root,image=volumeup,bg='#202329',command= VolumeUp ,highlightthickness = 0,borderwidth=0)
volumeupButton.place(x=25,y=835) 

volumedownButton = Button(root,image=volumedown,bg='#202329',command= VolumeDown ,highlightthickness = 0,borderwidth=0)
volumedownButton.place(x=75,y=835) 

volumemuteButton = Button(root,image=mute,bg='#202329',command= Mute ,highlightthickness = 0,borderwidth=0)
volumemuteButton.place(x=125,y=835)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Section Weather Web Scraping


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' }


URL = 'https://www.google.com/search?q=weather+location&oq=weather+location&aqs=chrome..69i57.3274j0j7&sourceid=chrome&ie=UTF-8'

weather(URL,headers)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



root.mainloop()