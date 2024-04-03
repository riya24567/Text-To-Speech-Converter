import tkinter as tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.config(bg="#104E8B")

engine = pyttsx3.init()

def speaknow():
 text= text_area.get(1.0,END)
 gender = gender_combobox.get()
 speed = speed_combobox.get()
 voices = engine.getProperty('voices')
 def setvoices():
    if (gender =='Male'):
        engine.setProperty('voice',voices[0].id)
        engine.say(text)
        engine.runAndWait()   
        
    else:
        engine.setProperty('voice',voices[1].id)
        engine.say(text)
        engine.runAndWait()    
       
    if(text):
      if(speed=="Fast"):
       engine.setProperty('rate',250)        
       setvoices()
    elif(speed =="Normal"):
        engine.setProperty('rate',150)        
        setvoices()
    
    elif(speed =="Slow"):
            engine.setProperty('rate',60)        
            setvoices()     
       
def download():
    text= text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
 
    def setvoices():
        if (gender =='Male'):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()   
        
        else:
            engine.setProperty('voice',voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()    
       
    if(text):
        if(speed=="Fast"):
            engine.setProperty('rate',250)        
            setvoices()
        elif(speed =="Normal"):
            engine.setProperty('rate',150)        
            setvoices()
            
        elif(speed =="Slow"):
            engine.setProperty('rate',60)        
            setvoices()     
      
#icon
image_icon= PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)

#Top Frame
Top_frame=Frame(root,bg ="#DCDCDC",width=900,height =100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file= "speaker logo.png")
Label(Top_frame,image= Logo,bg="#DCDCDC").place(x=10,y=5)

Label(Top_frame,text="TEXT TO SPEECH",font ="arial 20 bold",bg="#DCDCDC",fg="black").place(x=100,y=30)
##########
text_area=Text(root,font="Robote 20",bg ="white",relief=GROOVE,wrap =WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arail 15 bold",bg ="#104E8B",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arail 15 bold",bg ="#104E8B",fg="white").place(x=760,y=160)

gender_combobox= Combobox(root,values=['Male','Female'],font ="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox= Combobox(root,values=['Slow','Normal','Fast'],font ="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')

imageicon=PhotoImage(file= "kk.png")
btn=Button(root,text="Speak",compound=LEFT,image = imageicon,width=130,bg ="#EE7621",font="arial 14 bold",command = speaknow)
btn.place(x=550,y=280)

imageicon2=PhotoImage(file="download.png")
save=Button(root,text="Save",compound=LEFT,image = imageicon2,width=130,bg ="#00C957",font="arial 14 bold",command= download)
save.place(x=730,y=280)

root.mainloop()