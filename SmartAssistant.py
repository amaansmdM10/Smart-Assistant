import pyttsx3
import speech_recognition as sr
import datetime as dt
import webbrowser
import os
import random
import smtplib
import pyaudio
import pywhatkit as pw
from tkinter import messagebox
from tkinter import * 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning {}".format(dic["name"][:-1]))
    elif hour >= 12 and hour < 17:
        speak("Good afternoon {}".format(dic["name"][:-1]))
    else:
        speak("Good evening mate")
    speak("Hello {}, Alizeh here, How can i Help you".format(dic["name"][:-1]))

def registerPath(app):
	speak("Please Enter the path of "+app)
	dic[app]=input("Enter path of "+app+" ")
	dic[app]+="\n"
	with open("paths.txt","a") as file:
		file.write(app+"="+dic[app])

dic={}
with open("paths.txt","r") as file:
	for i in file:
		if i!="\n":
			app,path=i.split("=")
			dic[app]=path


if "name" not in dic:
	speak("Hello, can i know you name ")
	dic["name"]=input("Enter your name ") + "\n"
	with open("paths.txt","a") as file:
		file.write("name="+dic["name"])



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        # print(e)
        
        print("Say that again please...")
        return "None"
    return query

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

def whatsapp(no,r,n,k):

    pw.sendwhatmsg(no,r,n,k)
  
    
    


if __name__ == "__main__":
    wishMe()
    while True:
        query= takeCommand().lower()


        if 'whatsapp' in query:
                    speak("want to open whatsapp")
                    speak("enter the senders no")
                    no=input()
                    speak("enter the msg")
                    r=takeCommand()
                    speak("the time to send")
                    n=int(input())
                    k=int(input())
                    whatsapp(no,r,n,k)
        elif 'send email' in query:
            try:
                root.configure(bg="skyblue")
                root.title("email")
                root.geometry("500x200")
                Label(root, text="UserName").place(x=10, y=10)
                Label(root, text="Msg").place(x=10, y=40)
                global e1,e2
                e1 = Entry(root)
                e1.place(x=140, y=10)
 
                e2 = Entry(root)
                e2.place(x=140, y=40,width=200,
                height=100)
                to=e1.get()
                content=e2.get()
                Button(root, text="submit", command=sendEmail).place(x=10, y=100)
                root.mainloop()
            except Exception as e:
                print(e)
                speak("Error, can't send the mail.")

        elif "what is your name" in query:
		        speak("Iam Alizeh")

        elif "my name" in query:
		        speak("You are "+dic["name"][:-1])
	
	
        elif "change" in query and "name" in query:
		        speak("Please enter your name")
		        dic["name"]=input("Enter you name ")+"\n"
		        with open("paths.txt","w") as file:
			        for i in dic:
				            file.write(i+"="+dic[i])
        elif "would you like to marry me" in query:
                speak("Iam bored at relations u can date me if you?")
			 
        elif "change" in query and ("path" in query or "settings" in query):
		        speak("Enter the application name ")
		        name=input("App name ")
		        speak("Enter new path of "+name)
		        path=input("new path ")
		        dic[name]=path+"\n"
		        with open("paths.txt","w") as file:
			        for i in dic:
				        file.write(i+"="+dic[i])

        elif "search" in query or "google" in query:
		        pw.search(query[7:])
	
        elif "what is" in query:
                pw.info(query[8:], lines=5)
	
        elif "who is" in query:
		        pw.info(query[7:], lines=5)
		
        elif "who are you" in query:
		        speak("Iam sam, your personal assisatant , ready to help you")
	
        elif "time" in query:
		        speak("The time is "+dt.now().strftime("%H:%M:%S"))
	
        elif "hi" in query  or "hey there" in query or "hello" in query or "hai" in query:
		        speak("Hey There "+dic["name"])
	
        elif "how are you" in query or "how you doing" in query:
		        speak("Iam fine")
		        speak("And what about you?")
	
        elif ("good" in query or "fine" in query) and ("i am" in query):
		        speak("Noice")
	
        elif "open" in query:
		        if query[5:] not in dic:
			            registerPath(query[5:])
		        print('"'+dic[query[5:]][:-1]+'"')
		        os.system('"'+dic[query[5:]][:-1]+'"')
        elif 'quit' in query:
            speak("Thank you!"+dic["name"])
            exit()
	
        elif "exit" in query or "quit" in query:
		        speak("Closing the assistant")
		        speak("Thank You Bye "+dic["name"])
		        exit()
	
        elif "play" in query:
		        print(query[5:])
		        pw.playonyt(query[5:])

        else:
            speak("Command unclear")

                
        
