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

def infofilm():
    file="info.txt"
    resp=str(response)
    subprocess.run(["python", "InfoFilm.py"])
    with open(file, "w", encoding="utf-8") as fi:
     fi.write(resp)   


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
        name = log.get()  # Предполагается, что у вас есть переменная log с данными

        url += name
        querystring = {"info": "mini_info"}
        headers = {
            "X-RapidAPI-Key": "fa496f835cmsh4a81279f7f21920p10ef49jsn3c9d647f0d2c",
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # Проверяем, что результаты не пусты
        if 'results' in data and data['results']:
            # Вывод информации
            print(f"Page: {data['page']}")
            print(f"Next: {data['next']}")
            print(f"Entries: {data['entries']}")

            # Вывод результатов
            for result in data['results']:
                # Проверка на точное соответствие названия
                if 'titleText' in result and 'text' in result['titleText'] and result['titleText']['text'] == name:
                    print("\nTitle ID:", result['id'])
                    print("Title Text:", result['titleText']['text'])

                    # Дополнительные проверки для изображения и ссылки
                    if 'primaryImage' in result and result['primaryImage'] is not None:
                        print("Image URL:", result['primaryImage']['url'])
                    else:
                        print("No Image Available")

                    print("Release Year:", result['releaseYear']['year'])
                    print("Release Date:", result['releaseDate'])

                    # Дополнительные параметры, которые необходимо вывести, могут быть добавлены по аналогии

                    print("-" * 30)  # Добавляем разделитель между записями
        else:
            print(f"No results found for the title: {name}")

    
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


# Загрузка изображения из API
new_width = 155
new_height = 200

response = requests.get('https://m.media-amazon.com/images/M/MV5BOGE4NzU1YTAtNzA3Mi00ZTA2LTg2YmYtMDJmMThiMjlkYjg2XkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_.jpg', stream=True).raw
img = Image.open(response)
# Уменьшение размера изображения
img.thumbnail((new_width, new_height))


# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo=Button(image=photo_img, command=infofilm)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=130, y=210)


response = requests.get('https://m.media-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_.jpg', stream=True).raw
img = Image.open(response)

# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=330,y=210)


response = requests.get('https://m.media-amazon.com/images/M/MV5BMjM2NTQ5Mzc2M15BMl5BanBnXkFtZTgwNTcxMDI2NTE@._V1_.jpg', stream=True).raw
img = Image.open(response)
# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=530,y=210)


response = requests.get('https://m.media-amazon.com/images/M/MV5BMTYzOTc2NzU3N15BMl5BanBnXkFtZTcwNjY3MDE3NQ@@._V1_.jpg', stream=True).raw
img = Image.open(response)

# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=730,y=210)


response = requests.get('https://m.media-amazon.com/images/M/MV5BNjgwNzAzNjk1Nl5BMl5BanBnXkFtZTgwMzQ2NjI1OTE@._V1_.jpg', stream=True).raw
img = Image.open(response)
# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=930,y=210)


response = requests.get('https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_.jpg', stream=True).raw
img = Image.open(response)

# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=1130,y=210)



response = requests.get('https://m.media-amazon.com/images/M/MV5BNTM4NjIxNmEtYWE5NS00NDczLTkyNWQtYThhNmQyZGQzMjM0XkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_.jpg', stream=True).raw
img = Image.open(response)
# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=130,y=455)


response = requests.get('https://m.media-amazon.com/images/M/MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_.jpg', stream=True).raw
img = Image.open(response)

# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=330,y=455)


response = requests.get('https://m.media-amazon.com/images/M/MV5BYmMxZWRiMTgtZjM0Ny00NDQxLWIxYWQtZDdlNDNkOTEzYTdlXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg', stream=True).raw
img = Image.open(response)
# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=530,y=455)


response = requests.get('https://m.media-amazon.com/images/M/MV5BODZhNzlmOGItMWUyYS00Y2Q5LWFlNzMtM2I2NDFkM2ZkYmE1XkEyXkFqcGdeQXVyMTU5OTA4NTIz._V1_.jpg', stream=True).raw
img = Image.open(response)

# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=730,y=455)


response = requests.get('https://m.media-amazon.com/images/M/MV5BNjM0NTc0NzItM2FlYS00YzEwLWE0YmUtNTA2ZWIzODc2OTgxXkEyXkFqcGdeQXVyNTgwNzIyNzg@._V1_.jpg', stream=True).raw
img = Image.open(response)
# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=930,y=455)


response = requests.get('https://m.media-amazon.com/images/M/MV5BM2U2YWU5NWMtOGI2Ni00MGMwLWFkNjItMjgyZWMxNjllNTMzXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_.jpg', stream=True).raw
img = Image.open(response)

# Уменьшение размера изображения
img.thumbnail((new_width, new_height))

# Преобразование в PhotoImage
photo_img = ImageTk.PhotoImage(img)

# Создание метки с уменьшенным и повернутым изображением
label_photo = Label(window, image=photo_img)
label_photo.config(width=new_width, height=new_height)
label_photo.image = photo_img
label_photo.place(x=1130,y=455)




window.mainloop()