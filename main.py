
from tkinter import *
from tkinter import ttk, messagebox
import pyqrcode
 


root = Tk()
root.title("QR GERERATOR")
root.geometry("600x600")
root.iconbitmap("image1.ico")
root.configure(background="#808080")

def genQR():
   if len(user_ip.get()) != 0:
       global qr, img 
       qr = pyqrcode.create(user_ip.get(), error="H", version=15, mode="binary") 
    
       img = BitmapImage(data=qr.xbm(scale=4), background="white", foreground="black")
       display()
       clear_entry()
       warning()
   else:
       labe.config(text= "Warming "+"Please enter the feilds!", font=("poppins", 10, "bold"), foreground="red", background="#808080")
       
       
    
def display():
    lab.config(image=img)
    output.config(text="QR code for: " + user_ip.get())
    
def clear_entry():
    entry.delete(0, END)
    
def warning():
    labe.destroy()
   
        
    
    
label = ttk.Label(root, text="QR Generator", background="#808080", foreground="white", font=("poppins", 20, "bold"))
label.pack(padx=10, pady=10)

user_ip = StringVar() 


entry = ttk.Entry(root, textvariable=user_ip, background="lightgray", width="40", font=("poppins", 15, "bold"))
entry.pack(padx=10, pady=10)

labe = Label(root, bg="#808080")
labe.pack(padx=5, pady=5)



button = Button(root, text="Generate",command=genQR ,padx=10, pady=10, font=("poppins", 15, "bold"), foreground="skyblue")
button.pack(padx=5, pady=5)


lab = Label(root, bg="#808080")
lab.pack()

output = Label(root, bg="#808080", font=("poppins", 15, "bold"))
output.pack(padx=5, pady=5)

 



root.mainloop()


