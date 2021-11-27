from tkinter import messagebox
from tkinter import * 
import smtplib


def sendEmail():
    to=e1.get()
    content=e2.get()
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("amaansmd1@gmail.com","Foodworld2")
    
    server.sendmail("amaansmd1", to, content)
    messagebox.showinfo("  ","    Message Sent   ")
    root.destroy()

root = Tk()
root.geometry("500x500")

    
    
 

root.configure(bg="skyblue")
root.title("email")
root.geometry("350x200")
Label(root, text="UserName",bg="skyblue").place(x=10, y=10)
Label(root, text="Msg",bg="skyblue").place(x=10, y=40)
global e1,e2
e1 = Entry(root)
e1.place(x=140, y=10)

 
e2 = Entry(root)
e2.place(x=140, y=40,width=200,
        height=100)
to=e1.get()
content=e2.get()
Button(root, text="submit", command=sendEmail).place(x=140, y=150)

root.mainloop()
