from tkinter import *
import keyboard

import pyautogui
import os
import datetime 

def gui():
    m = Tk()
    m.title("printscreen manager") 
    w = 450
    h = 50
    x = 880
    y = 10
    m.geometry('%dx%d+%d+%d' % (w, h, x, y))
    label = Label(m, text="Název obrázku <ENTER>")
    name = Entry(m)
    label.config(font=("Helvetica", 15))
    name.config(width= 15, font=("Courier", 15))
    name.grid(row=0, column=1)
    label.grid(row=0)
    
    def callback(event):
        if not "\\" in name.get():
            with open("entry.txt", "w+") as file:
                file.truncate()
                file.write(name.get())
                file.close()
        if '.' in name.get():
            with open("entry.txt", "w+") as file:
                file.truncate()
                data = name.get()
                correct = data.split('.')
                correct = correct[0]
                file.write(correct)
                file.close()
        else: 
            with open("entry.txt", "w+") as file:
                file.truncate()
                data = name.get()
                correct = data.replace("\\", "")
                file.write(correct)
                file.close()
            
        m.destroy()
        
    
    m.bind('<Return>', callback)
    m.mainloop()
    with open("entry.txt", "r+") as f:
                ff = f.read()
                f.close()
    return ff
    

def exists(file_name, image):
    
    r = Tk()
    w = 510
    h = 125
    x = 500
    y = 200
    r.geometry('%dx%d+%d+%d'% (w ,h ,x ,y))
    r.title("File already exists!")
    lab = Label(r, text=f"File '{file_name}' already exists do yu want to overwrite it?")
    lab.config(font=("Helvetica", 15))
    def callback(event):
        image.save(r"C:\Users\Tomáš\Pictures\Pyscreens\%s.png" %file_name)
        r.destroy()
    def overw():
        image.save(r"C:\Users\Tomáš\Pictures\Pyscreens\%s.png" %file_name)
        r.destroy()
        
        
    def notverw():
        today = datetime.datetime.today()
        ran = str(file_name)+ str("-"+today.strftime("%d.%m.%Y"))
        image.save(r"C:\Users\Tomáš\Pictures\Pyscreens\%s.png" %ran)
        r.destroy()
        
    but = Button(r, text="NO", command=notverw)
    but.config(font=("Helvetica", 15), fg="red")
    but2 = Button(r, text="YES", command=overw)
    but2.config(font=("Helvetica", 15), fg="green")
    
    lab.grid(row=0, column=1)
    but.grid(row=2, column=1)
    but2.grid(row=1, column=1)
    r.bind('<Return>', callback)
    r.mainloop()
    
    
  
def main():
    while True:
        if keyboard.is_pressed("ctrl+print screen"):
            im1 = pyautogui.screenshot()
            name = gui()
            file = name
            if not os.path.exists(r"C:\Users\Tomáš\Pictures\Pyscreens\%s.png" %file):
                im1.save(r"C:\Users\Tomáš\Pictures\Pyscreens\%s.png" %file) 
            else:
                write = exists(file, im1)
                if write==True:
                    im1.save(r"C:\Users\Tomáš\Pictures\Pyscreens\%s.png" %file)
                if write ==False:
                    print("do not overwrite")
                    

main()        
