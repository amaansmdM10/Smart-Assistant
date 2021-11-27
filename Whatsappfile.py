from tkinter import *
from tkinter import messagebox
import pywhatkit as pw
def whatsapp():
    no=l.get()
    r=m.get()
    n=int(t.get())
    k=int(z.get())
    pw.sendwhatmsg(no,r,n,k)
    messagebox.showinfo("  ","    Message Sent   ")
    root.destroy()

root=Tk()
root.configure(bg="skyblue")
root.title("Whatsapp")
root.geometry("400x280")
Label(root, text="Enter no").place(x=10, y=10)
Label(root, text="Msg").place(x=10, y=40)
Label(root, text="Time").place(x=10, y=160)
global l,m,t,z
l= Entry(root)
l.place(x=140, y=10)

 
m= Entry(root)
m.place(x=140, y=40,width=200,height=100)
t= Entry(root)
t.place(x=140, y=150)
z= Entry(root)
z.place(x=140, y=180)
Button(root, text="submit", command=whatsapp).place(x=140, y=220)
root.mainloop()
                    
