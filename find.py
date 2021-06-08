import socket as s
from tkinter import *
from tkinter import Tk

root=Tk()
root.title('FindMe')
L=Label(root,text="Enter Domain :: ").grid(row=0,column=0,pady=20)
E1=Entry(root,bd=3).grid(row=0,column=1,pady=20)
B=Button(root,text="Find").grid(row=1,column=1,pady=20)
E2=Entry(root,bd=3).grid(row=2,column=1,pady=20)
root.mainloop()

a=input("Enter the domain name :: ")
print(f'IP of {a} is {s.gethostbyname(a)}')
