from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk
import mysql.connector



def register():

    conn=mysql.connector.connect(host="localhost",user="root",password="",database="tkproject")
    cr=conn.cursor()
    user=e1.get()
    contact=e3.get()
    email=e4.get()
    pwd=e5.get()
    cr.execute("insert into register(user,contact,email,pwd) values('"+user+"','"+contact+"','"+email+"','"+pwd+"')")
    conn.commit()
    if e1.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or e6.get()=="":
        mb.showerror("Error","You Need To Fill The Form")
    else:
        mb.showinfo("done","Data inserted successfully")
        root.destroy()
        import first

    
 

root=Tk()
root.title("Register page")
root.config(background="skyblue")
root.geometry("1100x700")
root.resizable(0,0)

frame_reg=Frame(root,bg="white")
frame_reg.place(x=90,y=100,height=500,width=900)
photo= ImageTk.PhotoImage(file="TPQ.jpg")
photo_image=Label(image=photo).place(x=60,y=150)
Label(frame_reg,width=-2,bg="skyblue").place(x=330,relheight=1)

Button(frame_reg,text="Register",font=("impact",20,'bold'),bg="blue",fg="black",bd=5,width=30,command=register).place(x=400,y=428)
Label(frame_reg,text="Register Here",font=("arial",30,'bold'),bg="white",fg="blue").place(x=470,y=10)

Label(frame_reg,text="First Name",font=("arial",20,),bg="white",fg="black").place(x=370,y=65)
e1=Entry(frame_reg,bd=7,font=("arial",15))
e1.place(x=370,y=100,width=200)

Label(frame_reg,text="Last Name",font=("arial",20,),bg="white",fg="black").place(x=650,y=65)
e2=Entry(frame_reg,bd=7,font=("arial",15))
e2.place(x=650,y=100,width=200)

Label(frame_reg,text="Contact no",font=("arial",20,),bg="white",fg="black").place(x=370,y=150)
e3=Entry(frame_reg,bd=7,font=("arial",15))
e3.place(x=370,y=190,width=200)

Label(frame_reg,text="Email",font=("arial",20,),bg="white",fg="black").place(x=650,y=150)
e4=Entry(frame_reg,bd=7,font=("arial",15))
e4.place(x=650,y=190,width=200)


Label(frame_reg,text="Password",font=("arial",20,),bg="white",fg="black").place(x=370,y=230)
e5=Entry(frame_reg,bd=7,font=("arial",15),show="*")
e5.place(x=370,y=270,width=260)

Label(frame_reg,text="Confirm password",font=("arial",20,),bg="white",fg="black").place(x=370,y=320)
e6=Entry(frame_reg,bd=7,font=("arial",15),show="*")
e6.place(x=370,y=360,width=260)

chk=Checkbutton(frame_reg,text="I Agree The Terms & Conditions",font=("arial",10),fg="black",bg="white").place(x=400,y=400)




root.mainloop()

