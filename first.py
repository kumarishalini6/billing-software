from tkinter import *
import mysql.connector
from PIL import ImageTk
import tkinter.messagebox as mb 

def forget():
    mb.showinfo("hii","you can change your password")
    root.destroy()
    import forget

 


root=Tk()

def chk():
    conn=mysql.connector.connect(host='localhost',user="root",password="",database="tkproject")
    cr=conn.cursor()
    user=e1.get()
    pwd=e2.get()
    cr.execute("select * from register where user='"+user+"'and pwd='"+pwd+"'")
    if e1.get()=="" or e2.get()=="":
        mb.showerror("Error","You need to fill the form")
    elif(cr.fetchone()):
        mb.showinfo("success","Welcome")
        root.destroy()
        import billing

    else:
        mb.showerror("success","your data not found")



root.title("Login system")
root.config(background="gray")
root.geometry("1200x730")
root.resizable(0,0)
photo=PhotoImage(file="h2.png")
photo_image=Label(image=photo).place(x=0,y=0,relwidth=1,relheight=1)
frame_login=Frame(root,bg="white")
frame_login.place(x=140,y=250,height=400,width=550)
Label(frame_login,text="Login Here",fg="darkorange",bg="white",font=("impact",40,'bold')).place(x=135,y=30)
user=Label(frame_login,text="Username",fg="gray",bg="white",font=("arial",30,'bold')).place(x=70,y=135)
pwd=Label(frame_login,text="Password",fg="gray",bg="white",font=("arial",30,'bold')).place(x=70,y=228)
e1=Entry(frame_login,font=("arial",15),border=8)
e1.place(x=300,y=150,height=40,width=200)
e2=Entry(frame_login,show='*',font=("arial",15),border=8)
e2.place(x=300,y=230,height=40,width=200)
Button(frame_login,text="Forgrt password?",fg="orange",font=("arial",15),bg="white",command=forget).place(x=170,y=295)
Button(root,text="Login",bg="darkorange",font=("arial",20),fg="white",command=chk).place(x=355,y=620,width=150)

root.mainloop()