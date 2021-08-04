from tkinter import *
import os
import keyboard
import pyautogui
import datetime

class Gui_entry():
    
    def __init__(self, master):
        self.master = master
        master.title("Printscreen manager")
        self.width , self.height = (450,50)
        self.x, self.y = (880, 10)
        master.geometry('%dx%d+%d+%d'%(self.width, self.height, self.x, self.y))
        self.label = Label(master, text="Název obrázku <ENTER>")
        self.label.config(font=("Helvetica", 15))
        self.label.grid(row=0)
        self.file_name = Entry(self.master)
        self.file_name.config(width= 15, font=("Courier", 15))
        self.file_name.grid(row=0, column = 1)
        def callback(event):
            name = self.file_name.get()
            if '.' in name:
                with open("entry.txt", "w+") as file:
                    file.truncate()
                    data = name
                    correct = data.split('.')
                    correct = correct[0]
                    file.write(correct)
                    file.close()
            if '\\' in name: 
                with open("entry.txt", "w+") as file:
                    file.truncate()
                    data = name
                    correct = data.replace("\\", "")
                    file.write(correct)
                    file.close()
            else:
                with open("entry.txt", "w+") as file:
                    file.truncate()
                    file.write(name)
                    file.close()
            print(f"name you entered: {name}")  
            self.master.destroy()
            
        self.master.bind('<Return>', callback)
        
class Gui_exists():
    def __init__(self, master, file_name, image):
        global callback
        self.master = master   
        self.width, self.height =  (510, 125)
        self.x, self.y = (500, 200)
        master.geometry("%dx%d+%d+%d"%(self.width, self.height, self.x, self.y)) 
        master.title("FILE ALREADY EXISTS!")
        
        self.label = Label(master, text=f"File '{file_name}' already exists, do you want to over write it?")
        self.label.config(font=("Helvetica", 15))
        
        self.button_yes = Button(master, text= "YES", command =lambda: callback("p"))
        self.button_yes.config(font=("Helvetica", 15), fg="green")
        def n_overwrite():
            today = datetime.datetime.today()
            ran = str(file_name)+ str("-"+today.strftime("%d.%m.%Y"))
            image.save(r"C:\Users\YOUR_PATH\%s.png" %ran)
            self.master.destroy()
        self.button_no = Button(master, text= "NO", command = n_overwrite)
        self.button_no.config(font=("Helvetica", 15), fg="red")
        
        self.label.grid(row=0, column=1)
        self.button_yes.grid(row=1, column=1)
        self.button_no.grid(row=2, column=1)
        
        def callback(event):
            image.save(r"C:\Users\YOUR_PATH\%s.png" %file_name)
            self.master.destroy()
            
        master.bind("<Return>", callback )
        
        
global read_file
def read_file():
    with open("entry.txt", "r+") as f:
        data = f.read()
        
        return data
global clear_file
def clear_file():
    with open("entry.txt", "w+") as f:
        f.truncate()
def main():
    
    while True:
        if keyboard.is_pressed("ctrl+print screen"):
            im_1 = pyautogui.screenshot()
            a_root = Tk()
            Gui_entry(a_root)
            a_root.mainloop()
            file = read_file()
            clear_file()
            if file != "":
                if not os.path.exists(r"C:\Users\YOUR_PATH\%s.png" %file):
                    im_1.save(r"C:\Users\YOUR_PATH\%s.png" %(file)) 
                    
                else:
                    b_root = Tk()
                    Gui_exists(b_root, file, im_1)   
                    b_root.mainloop() 
            else:
                pass
            
    
          
main()
        
