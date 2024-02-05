from tkinter import *
#from PIL import Image
import tkinter as tk
import subprocess
import csv

p="gmail.com"
def opentwo():
    
  subprocess.run(["python", "Untitled-1.py"])
    
def closed():
    window.destroy()
    
def Back():
     closed()
     opentwo()
     
def is_entry_empty(entry_widget):
    return not entry_widget.get()

def standartcolor():
      newtext="Логін"
      newcolor="white"
      newbag="#022B49"
      
      logtext2.config(text=newtext, fg=newcolor, bg=newbag)
      logtext2.pack()
      logtext2.place(x=400, y=125)
      
      newtext="Пошта"
      
      posttext.config(text=newtext, fg=newcolor, bg=newbag)
      posttext.pack()
      posttext.place(x=400, y=185)
      
      newtext="Підтвердити пароль"
      
      paspovttext.config(text=newtext, fg=newcolor, bg=newbag)
      paspovttext.pack()
      paspovttext.place(x=400, y=305)

def notlog():
    newtext="Поле порожнє, введіть логін"
    newcolor="#5F0000"
    newbag="white"
    logtext2.config(text=newtext,fg=newcolor, bg=newbag)
    logtext2.pack()
    logtext2.place(x=400, y=125)

def notmail():
    newtext="Поле порожнє, введіть пошту"
    newcolor="#5F0000"
    newbag="white"
    posttext.config(text=newtext,fg=newcolor, bg=newbag)
    posttext.pack()
    posttext.place(x=400, y=185)
    
def notpas():
    newtext="Поле порожнє, введіть пароль"
    newcolor="#5F0000"
    newbag="white"
    pastext2.config(text=newtext,fg=newcolor, bg=newbag)
    pastext2.pack()
    pastext2.place(x=400, y=245)

def notpaspovt():
    newtext="Підтвердіть пароль"
    newcolor="#5F0000"
    newbag="white"
    paspovttext.config(text=newtext,fg=newcolor, bg=newbag)
    paspovttext.pack()
    paspovttext.place(x=400, y=305)
          
def loggy():
    standartcolor()
    mail_text = mail.get()
    pas2_text = pas2.get()
    log2_text = log2.get()
    paspovt_text = paspovt.get()
    ps = "@gmail.com"
    o=0
    p=0

    if is_entry_empty(log2):
        notlog()
        p+=1
    if is_entry_empty(mail):
         notmail()
         p+=1
    if is_entry_empty(pas2):
         notpas()
         p+=1
    if is_entry_empty(paspovt):
         notpaspovt()
         p+=1
    if(p>=1):
        return 0
          
    if ps in mail_text:
        with open("example.csv", "r",newline='') as h:
            reader = csv.reader(h)
            for row in reader:
                if mail_text in row:
                    notmail()
                    newtextt="Така пошта вже зареєстрована"
                    posttext.config(text=newtextt)
                    posttext.pack()
                    posttext.place(x=400, y=185)
                    o+=1
                    return
                elif log2_text in row:
                    notlog()
                    newtextt="Такий логін вже існує"
                    logtext2.config(text=newtextt)             
                    logtext2.pack()
                    logtext2.place(x=400, y=125)
                    o+=1
                    return
                elif pas2_text != paspovt_text:
                    newtextt="Паролі не співпадають"
                    paspovttext.config(text=newtextt)                 
                    paspovttext.pack()
                    paspovttext.place(x=400, y=305)
                    o+=1
                    return
                
    else:   
            notmail()
            newtextt="Ви не вірно вказали пошту"
            posttext.config(text=newtextt)
            posttext.pack()
            posttext.place(x=400, y=185)
            o+=1
            return     
    log2_text+=';'
    mail_text+=';'
    log2_text+=';'
    data_to_write = [
                  ['Column1', 'Column2', 'Column3'],  # Optional: You can include headers
                  [log2_text, mail_text, log2_text]]
    if o==0:   
                standartcolor()
                csv_file_path = 'example.csv'
                with open(csv_file_path, 'a', newline='') as csv_file:
                   csv_writer = csv.writer(csv_file)
                   csv_writer.writerows(data_to_write)
                
                   message_label = tk.Label(window, text="Вас успішно зарегестровано", fg="White",bg="#022B49", font=("Mulish", 20))
                   message_label.pack()
                   message_label.place(relx=0.5, rely=0.5, anchor='center')
                   window.after(4000, Back)
                return        
   

window = Tk()
window.geometry('654x520')
window.resizable(False, False)
window.config(bg="#022B49")
window.title("Welcome")

button_log2 = Button(window, text="Зарегеструватися", fg="white", bg="#022B40", width=27, height=2, command=loggy)
button_log2.place(x=400,y=390)

button_back = Button(window, text="Назад", fg="white", bg="#022B40", width=27, height=2, command=Back )
button_back.place(x=400,y=440)

log2 = Entry(window, bg="white", width=32)
log2.pack()
log2.place(x=400, y=150)

mail = Entry(window, bg="white", width=32)
mail.pack()
mail.place(x=400, y=210)

pas2 = Entry(window, bg="white", width=32)
pas2.pack()
pas2.place(x=400, y=270)

paspovt = Entry(window, bg="white", width=32)
paspovt.pack()
paspovt.place(x=400, y=330)


hello2 = Label(window, text="Ласкаво просимо", fg="white", bg="#022B49",font=("Mulish", 18))
hello2.pack()
hello2.place(x=400, y=60)

logtext2 = Label(window, text="Логін", fg="white", bg="#022B49",font=("Mulish", 10))
logtext2.pack()
logtext2.place(x=400, y=125)


posttext = Label(window, text="Пошта", fg="white", bg="#022B49",font=("Mulish", 10))
posttext.pack()
posttext.place(x=400, y=185)


pastext2 = Label(window, text="Пароль", fg="white", bg="#022B49",font=("Mulish", 10))
pastext2.pack()
pastext2.place(x=400, y=245)


paspovttext = Label(window, text="Підтвердити пароль", fg="white", bg="#022B49",font=("Mulish", 10))
paspovttext.pack()
paspovttext.place(x=400, y=305)


photo2 = Canvas(window, width=326, height=520, bg="#5F0000")
photo2.pack()
photo2.place(x=0,y=0)
'''

image_path = "./Screenshot_2.png"  # Укажите путь к вашему изображению
photo = PhotoImage(file=image_path)
'''
window.mainloop()