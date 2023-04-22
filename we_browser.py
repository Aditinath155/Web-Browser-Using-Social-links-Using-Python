from tkinter import *
from tkinter import messagebox
from tkinter import font

import webbrowser
root = Tk()
root.title('Welcome to the web browser')
root.geometry('600x600')

def search():
    word=e1.get()
    search ='http://google.com/search?q=' + word
    webbrowser.open_new(search)

def facebook():
    webbrowser.open_new('www.facebook.com')

def instagram():
    webbrowser.open_new('www.instagram.com')

def github():
    webbrowser.open_new('www.github.com')

def snapchat():
    webbrowser.open_new('www.snapchat.com')

def twitter():
    webbrowser.open_new('www.twitter.com')

def youtube():
    webbrowser.open_new('www.youtube.com')

def whatsapp():
    webbrowser.open_new("www.whatsapp.com")
#Heading Box
Label(root,text='My Web Browser',font ='impack 25 bold',bg='#ade6d8',fg='black').pack(fill='x')

#Entry box
e1 = Entry(root,font='impack 15 bold',bd=3,bg='#ade6d8',width=50)
e1.place(x=5,y=80,width=320,height=40)
#Search Button
Button(root,text='Search',font = 'impack 15 bold',fg='white',bg='green',width=10,command=search).place(x=365,y=82,height=40)

#
Label(root,text='Access your social media account',bg='#FEC8D8',fg='black',font='impack 17 bold').pack(fill='x',pady=120)
#Facebook button
Button(root,text='Facebook',font='impack 17 bold',bg='#106EBE',fg='white',width=10,command=facebook).place(x=40,y=225)

#Instagram Button
Button(root,text='Instagram',font='impack 17 bold',bg='#E1306C',fg='white',width=10,command=instagram).place(x=200,y=225)

#Github
Button(root,text='Github',font='impack 17 bold',bg='black',fg='white',width=10,command=github).place(x=40,y=290)

#Snapchat
Button(root,text='Snap Chat',font='impack 17 bold',bg='#ffff00',fg='white',width=10,command=snapchat).place(x=375,y=225)

#WhatsApp Button
Button(root,text='Whats App',font='impack 17 bold',bg='green',fg='white',width=10,command=whatsapp).place(x=200,y=290)

#Twitter Button
Button(root,text='Twitter',font='impack 17 bold',bg='#388DEE',fg='white',width=10,command=twitter).place(x=375,y=290)

#Youtube Button
Button(root,text='Youtube',font='impack 17 bold',bg='#E21B22',fg='white',width=20,command=youtube).place(x=125,y=355)

mainloop()
