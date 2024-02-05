from tkinter import *
#from PIL import Image
import tkinter as tk
import subprocess
import csv

# windows
window = Tk()
window.geometry('654x520')
window.resizable(False, False)
window.config(bg="#022B49")
window.title("Welcome")

#labels

log = Entry(window, bg="white", width=32)
log.pack()
log.place(x=400, y=170)

pas = Entry(window, bg="white", width=32)
pas.pack()
pas.place(x=400, y=250)

hello = Label(window, text="Ласкаво просимо", fg="white", bg="#022B49",font=("Mulish", 18))
hello.pack()
hello.place(x=400, y=60)

logtext = Label(window, text="Пошта", fg="white", bg="#022B49",font=("Mulish", 10))
logtext.pack()
logtext.place(x=400, y=140)


pastext = Label(window, text="Пароль", fg="white", bg="#022B49",font=("Mulish", 10))
pastext.pack()
pastext.place(x=400, y=220)

textab = Label(window, text="або", fg="white", bg="#022B49",font=("Mulish", 10))
textab.pack()
textab.place(x=482, y=371)


n = 0 

# open registration window
def openone():
    
  subprocess.run(["python", "regestratoin.py"])

# open account window
def opentwo():
    
  subprocess.run(["python", "Accaunt.py"])
    
# close
def closedo():
    window.destroy()
    
# function for open registration window function and close prevous window
def openwinregestration():
     closedo()
     openone()
    
# function for open account window function and close prevous window
def openacc():
    opentwo()
    closedo()
    

# function tcheck is there anything
def is_entry_empty(entry_widget):
    return not entry_widget.get()

# function that sets standart colors
def standartcolor():
      newtext="Логін"
      newcolor="white"
      newbag="#022B49"
      
      logtext.config(text=newtext, fg=newcolor, bg=newbag)
      logtext.pack()
      logtext.place(x=400, y=140)
      
      newtext="Пароль"
      
      pastext.config(text=newtext, fg=newcolor, bg=newbag)
      pastext.pack()
      pastext.place(x=400, y=220)

def notlog():
    newtext="Поле порожне"
    newcolor="#5F0000"
    newbag="white"
    logtext.config(text=newtext, fg=newcolor, bg=newbag)
    logtext.pack()
    logtext.place(x=400, y=140)
    
def notpas():
    newtext="Поле порожне"
    newcolor="#5F0000"
    newbag="white"     
    pastext.config(text=newtext, fg=newcolor, bg=newbag)
    pastext.pack()
    pastext.place(x=400, y=220)
def notlogin():
    newtext="Невірна пошта"
    newcolor="#5F0000"
    newbag="white"
    logtext.config(text=newtext, fg=newcolor, bg=newbag)
    logtext.pack()
    logtext.place(x=400, y=140)
def notpassword():
    newtext="Невірний пароль"
    newcolor="#5F0000"
    newbag="white"     
    pastext.config(text=newtext, fg=newcolor, bg=newbag)
    pastext.pack()
    pastext.place(x=400, y=220)   
    
# try to write global function, not working properly
def glob():
    global global_variable
    global n
    n+=1

# entry point
def go():
      global n 
      standartcolor()
     
      log_text = log.get()
      pas_text = pas.get()
      
      print(log_text)
        
      if is_entry_empty(log) and is_entry_empty(pas):
          notlog()
          notpas()
          return
      elif is_entry_empty(pas):
          notpas()
          return
      elif is_entry_empty(log):
          notlog()
          
      filename="base.csv"
            
      with open(filename, "r", newline='') as h:
         reader = csv.reader(h, delimiter=';')
         for row in reader:
            if len(row) > 2 and  (log_text == row[1] and pas_text == row[2]):
               openacc()
            elif len(row) > 2 and  log_text != row[1]:
                n += 1
                notlogin()
            elif len(row) > 2 and  pas_text != row[2]:
                notpassword()
                n += 1

      if n >= 3:
            message_label = tk.Label(window, text="Можливо у вас немає акаунту,\n спробуйде зарегеструватися", fg="White",bg="#022B49", font=("Mulish", 20))
            message_label.pack()
            message_label.place(relx=0.5, rely=0.5, anchor='center')
            window.after(5000)
            message_label.destroy

        
          
# form elements and layout

button_go = Button(window, text="Вхід", bg="#022B40", fg="white", width=27, height=2, command=go)
button_go.place(x=400,y=310)

button_log = Button(window, text="Регестрація", fg="white", bg="#022B40", width=27, height=2, command=openwinregestration) 
button_log.place(x=400,y=420)

photo = Canvas(window, width=326, height=520, bg="#5F0000")
photo.pack()
photo.place(x=0,y=0)


window.mainloop()
