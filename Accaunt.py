from tkinter import *
import csv

def info():
    file="lastac.txt"
    with open(file, "r") as d:
           logtext=d.read() 
           return logtext
           
    
           
window = Tk()
window.geometry('750x410')
window.resizable(False, False)
window.config(bg="Black")
window.title("Your account")


favorites = Button(window, text="Обране", fg="white", bg="#5F0000", width=27, height=2)
favorites.place(x=45,y=345)

edit = Button(window, text="Редагувати", fg="white", bg="#5F0000", width=27, height=2)
edit.place(x=297,y=345)

    
logintex = Label(window, text="Логін",fg="white", bg="black",font=("Mulish", 14))
logintex.pack()
logintex.place(x=45, y=30)

i=info()        
postntex = Label(window, text=i, fg="white", bg="black",font=("Mulish", 14))
postntex.pack()
postntex.place(x=45, y=70)

foruser = Canvas(window, width=440, height=190, bg="white")
foruser.pack()
foruser.place(x=45,y=125)

foruser = Canvas(window, width=435, height=185, bg="black")
foruser.pack()
foruser.place(x=45,y=128)



infouser = Label(window, text="Про мене", fg="white", bg="black",font=("Mulish", 14))
infouser.pack()
infouser.place(x=305, y=130) 

window.mainloop()