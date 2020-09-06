from tkinter import *
import tkinter.messagebox as mb 
import mysql.connector

def do():
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="tkproject")
    cr=conn.cursor()
    user=e1.get()
    pwd=e2.get()
    cr.execute("update register set pwd='"+pwd+"' where user='"+user+"'")
    conn.commit()
    mb.showinfo("Done","Your Data is inserted Now you can login")
    root.destroy()
    import first


root=Tk()
root.config(background="pink")
root.geometry("500x300")
root.resizable(0,0)
Label(root,text="Forget Form",font=("arial",30,'bold'),bg="pink",fg="green").pack()

Label(root,text="user",font=("arial",25,'bold'),bg="pink",fg="black",bd=12).place(x=50,y=55)
e1=Entry(root,font=("arial",15,),width=24,bd=8)
e1.place(x=150,y=66)

Label(root,text="pwd",font=("arial",25,'bold'),bg="pink",fg="black",bd=12).place(x=50,y=140)
e2=Entry(root,font=("arial",15,),width=24,bd=8)
e2.place(x=150,y=140)

Button(root,text="Register New Data",width=25,font=("arial",20,'bold'),bg="green",fg="Black",command=do).place(x=50,y=220)

root.mainloop()