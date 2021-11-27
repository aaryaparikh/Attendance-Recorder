import os
import re
import tkinter.font as font
from datetime import date
from collections import Counter
from tkinter import *
import tkinter as tk
def createfile(filename):
    file=open(filename+".txt","w+")
    for i in app.children.values():
        i.pack_forget()
    lab=Label(app,bg="green",font=fbutton,text=filename+" Created Successfully")
    lab.pack(pady=10)
    btn=Button(text="Back to home",bg="green",font=fbutton,command=main)
    btn.pack(pady=10)
def newwindow():
    for i in app.children.values():
        i.pack_forget()
    lab=Label(app,bg="green",font=fbutton,text="Enter Class Name:- ")
    lab.pack(pady=10)
    e=Entry(width=30,font=fbutton)
    e.pack()
    create=Button(text="Create",bg="green",font=fbutton,command=lambda: createfile(e.get()))
    create.pack()
def listclass():
    for i in app.children.values():
        i.pack_forget()
    arr=os.listdir('.')
    btn=[]
    lab=Label(app,bg="green",font=fbutton,text="Enter the attendance and then select a class")
    lab.pack(pady=10)
    e=Entry(font=fbutton)
    e.pack(pady=10)
    v=StringVar()
    for i in range(len(arr)):
        a=arr[i].split('.')
        if a[1]=="txt":
            btn.append(Radiobutton(app,bg="green",text=a[0],tristatevalue=arr[1],variable=v,value=arr[i]))
            btn[-1].pack(pady=2)
    b=Button(text="Record",bg="green",font=fbutton,command=lambda: addtofile(v.get(),e.get()))
    b.pack()
def addtofile(filename,data):
    text=data
    a=text.split()
    text=" "
    for i in a:
        text=text+" "+i+" "
    match1=re.compile(r'(\w{2})(\d{2})(\d)(\d{3})(\d{4})')
    match2=re.compile(r' (\d{3}) ')
    match3=re.compile(r' (\d{2}) ')
    match4=re.compile(r' (\d) ')
    matches1=re.findall(match1,text)
    matches2=re.findall(match2,text)
    matches3=re.findall(match3,text)
    matches4=re.findall(match4,text)
    li=[]
    for i in matches1:
        li.append(int(i[4]))
    for i in matches2:
        li.append(int(i))
    for i in matches3:
        li.append(int(i))
    for i in matches4:
        li.append(int(i))
    li.sort()
    dt=date.today()
    file=open(filename,"a")
    file.write(f"\n{dt}\n")
    for i in li:
        file.write(f"{i}\n")
    file.close()
    for i in app.children.values():
        i.pack_forget()
    lab=Label(app,font=fbutton,bg="green",text="Attendance Recorded Succesfully.")
    lab.pack(pady=10)
    home=Button(text="Return to home",bg="green",font=fbutton,command=main)
    home.pack(pady=10)
def disp(filename):
    for i in app.children.values():
        i.pack_forget()
    file=open(filename,"r")
    data=file.readlines()
    li=[]
    for i in data:
        if i.strip().isnumeric():
            li.append(int(i.strip()))
    attendance=Counter(li)
    e=Text(app,height=20,width=20)
    e.pack()
    
    for i in sorted(attendance.keys()):
        e.insert(tk.END,f"{i} : {attendance[i]}\n")
    b=Button(text="Home",bg="green",font=fbutton,command=main)
    b.pack()
def check():
    for i in app.children.values():
        i.pack_forget()
    arr=os.listdir('.')
    btn=[]
    v=StringVar()
    for i in range(len(arr)):
        a=arr[i].split('.')
        if a[1]=="txt":
            btn.append(Radiobutton(app,bg="green",text=a[0],tristatevalue=arr[1],variable=v,value=arr[i]))
            btn[-1].pack(pady=2)
    bt=Button(text="Check",bg="green",font=fbutton,command=lambda: disp(v.get()))
    bt.pack()
def main():
    for i in app.children.values():
        i.pack_forget()
    create=Button(text="Create a new class",font=fbutton,bg="green",command=newwindow)
    create.pack(pady=10)
    exist=Button(text="Add to Existing class",font=fbutton,bg="green",command=listclass)
    exist.pack(pady=10)
    show=Button(text="Check Attendance",font=fbutton,bg="green",command=check)
    show.pack(pady=10)
app=Tk()
app.title('Attendance Recoreder')
app.geometry('725x355')
bg=PhotoImage(file="bg.png")
fbutton=font.Font(family='Helvetica',size=14)
label=Label(app,image=bg)
label.place(x=0,y=0)
main()
app.mainloop()