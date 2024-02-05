from tkinter import *
from tkinter import Tk, Label
from PIL import Image, ImageTk
from tkinter import PhotoImage
from PIL import Image, UnidentifiedImageError
import webbrowser
import subprocess
import openai
import requests
from io import BytesIO
import os



def open_telegram_bot(event):
     telegram_bot_url = "https://t.me/MarvelPracticalBot"
     webbrowser.open(telegram_bot_url)
def openaidialog():
    subprocess.run(["python", "AIdialog.py"])
     
def opentwo():     
  subprocess.run(["python", "login.py"])
    
def closed():
    window.destroy()

def openone():
  subprocess.run(["python", "regestratoin.py"])



def seartch():
      
        url = "https://moviesdatabase.p.rapidapi.com/titles/search/akas/"
        name=log.get()
        url+=name
        
        querystring = {"info":"mini_info"}
        headers = {
            "X-RapidAPI-Key": "fa496f835cmsh4a81279f7f21920p10ef49jsn3c9d647f0d2c",
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)

        print(response.json())
    
window = Tk()
window.geometry('1410x800')
window.resizable(False, False)
window.config(bg="#191919")
window.title("Marvel")



photo1=Image.open('AI.png')
photo1=ImageTk.PhotoImage(photo1)
labelai=Button(image=photo1, command=openaidialog)
labelai.image=photo1
labelai.config(width=50,height=50)
labelai.place(x=1305,y=704)


photo=Image.open('logo.png')
photo=ImageTk.PhotoImage(photo)
labelp=Label(image=photo)
labelp.image=photo
labelp.place(x=80,y=18)

photo=Image.open('telegram.png')
photo=ImageTk.PhotoImage(photo)
labelp=Label(image=photo)
labelp.image=photo
labelp.config(width=50,height=50)
labelp.place(x=1235,y=704)
labelp.bind("<Button-1>", open_telegram_bot)

def openwingo():
    opentwo()

def openregectration():
    openone()

button_go = Button(window, text="Вхід", fg="black", bg="#910000", width=15, height=1, font=("Inter", 13), relief='solid', bd=3, command=openwingo)
button_go.place(x=1040,y=38)

button_log = Button(window, text="Регестрація", fg="black", bg="#910000", width=15, height=1, font=("Inter", 13), relief='solid', bd=3, command=openregectration)
button_log.place(x=1200,y=38)

button_search = Button(window, text="Пошук", fg="black", bg="#910000", width=10, height=1, font=("Inter", 14), relief='solid', bd=3, command=seartch)
button_search.place(x=845,y=36) 

button_all = Button(window, text="Все", fg="black", bg="#910000", width=10,height=1, font=("Inter", 13), relief='solid', bd=3)
button_all.place(x=100,y=140) 

button_comics = Button(window, text="Комікси", fg="black", bg="#910000", width=20, height=1, font=("Inter", 13), relief='solid', bd=3 )
button_comics.place(x=210,y=140)

button_films = Button(window, text="Фільми", fg="black", bg="#910000", width=20, height=1, font=("Inter", 13), relief='solid', bd=3)
button_films.place(x=410,y=140)

button_download = Button(window, text="Завантажити ще", fg="black", bg="#910000", width=0, height=0, font=("Inter", 20),  relief='solid', bd=3)
button_download.place(x=600, y=700)

log = Entry(window, bg="white", width=44, font=("Inter", 20))
log.pack()
log.place(x=180, y=38)


rectangle_visible = BooleanVar()
rectangle_visible.set(False)



film1 = Canvas(window, width=155, height=200, bg="gray")
film1.pack()
film1.place(x=130,y=210)

film2 = Canvas(window, width=155, height=200, bg="gray")
film2.pack()
film2.place(x=330,y=210)

film3 = Canvas(window, width=155, height=200, bg="gray")
film3.pack()
film3.place(x=530,y=210)

film4 = Canvas(window, width=155, height=200, bg="gray")
film4.pack()
film4.place(x=730,y=210)

film5 = Canvas(window, width=155, height=200, bg="gray")
film5.pack()
film5.place(x=930,y=210)

film6 = Canvas(window, width=155, height=200, bg="gray")
film6.pack()
film6.place(x=1130,y=210)

film7 = Canvas(window, width=155, height=200, bg="gray")
film7.pack()
film7.place(x=130,y=455)

film8 = Canvas(window, width=155, height=200, bg="gray")
film8.pack()
film8.place(x=330,y=455)

film9 = Canvas(window, width=155, height=200, bg="gray")
film9.pack()
film9.place(x=530,y=455)

film10 = Canvas(window, width=155, height=200, bg="gray")
film10.pack()
film10.place(x=730,y=455)

film11 = Canvas(window, width=155, height=200, bg="gray")
film11.pack()
film11.place(x=930,y=455)

film12 = Canvas(window, width=155, height=200, bg="gray")
film12.pack()
film12.place(x=1130,y=455)



window.mainloop()