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


def info():
    file="info.txt"
    with open(file, "r") as d:
           logtext=d.read() 
           return logtext
           

window = Tk()
window.geometry('800x460')
window.resizable(False, False)
window.config(bg="#191919")
window.title("Marvel")


response=info()
new_width=315

new_height=390
img = Image.open(response)
# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=30,y=30)



window.mainloop()