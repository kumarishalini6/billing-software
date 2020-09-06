from tkinter import *
import mysql.connector
from PIL import ImageTk
import tkinter.messagebox as mb
        
def pay():

        conn=mysql.connector.connect(host="localhost",user="root",password="",database="tkproject")
        cr=conn.cursor()
        user=e1.get()
        card_number=e2.get()
        holder_name=e3.get()
        expiary_date=e4.get()
        cvv=e5.get()
        cr.execute("insert into payment(user,card_number,holder_name,expiary_date,cvv) values('"+user+"','"+card_number+"','"+holder_name+"','"+expiary_date+"',"+cvv+")")
        conn.commit()
        mb.showinfo("done","your payment is done successfully")
        root.destroy()
        import end
        






root=Tk()

root.title("Pay Corner")
root.config(background="cadet blue")
root.geometry("1200x700")
root.resizable(0,0)

frame_pay=Frame(root,bg="cornsilk")
frame_pay.place(x=220,y=100,height=550,width=865)

Button(root,text="Pay Now",bg="green",font=("arial",30,'bold'),fg="black",bd=0,width=20,command=pay).place(x=400,y=610)
photo=PhotoImage(file="card2.png")
photo_image=Label(image=photo).place(x=30,y=250)
Label(frame_pay,text="SBI",font=("arial",30,'bold','underline'),bg="cornsilk",fg="purple").place(x=130,y=15)
Label(frame_pay,text="UCO",font=("arial",30,'bold'),bg="cornsilk",fg="purple").place(x=280,y=15)
Label(frame_pay,text="UNION",font=("arial",30,'bold'),bg="cornsilk",fg="purple").place(x=420,y=15)
Label(frame_pay,text="HDFC",font=("arial",30,'bold'),bg="cornsilk",fg="purple").place(x=630,y=15)
Label(frame_pay,height=-3,bg="cadet blue").place(x=0,y=70,relwidth=1)
Label(frame_pay,text="Payment Details",fg="purple",bg="cornsilk",font=("arial",40,'bold','underline')).place(x=230,y=100)
Label(frame_pay,text="Card Number",fg="purple",bg="cornsilk",font=("arial",20,'bold')).place(x=260,y=198)
e2=Entry(frame_pay,font=("arial",20,'bold'),fg="black",bd=3,width=20)
e2.place(x=530,y=198)
Label(frame_pay,text="Card holder name",fg="purple",bg="cornsilk",font=("arial",20,'bold')).place(x=260,y=268)
e3=Entry(frame_pay,font=("arial",20,'bold'),fg="black",bd=3,width=20)
e3.place(x=530,y=268)
Label(frame_pay,text="Expiary date",fg="purple",bg="cornsilk",font=("arial",20,'bold')).place(x=260,y=330)
e4=Entry(frame_pay,font=("arial",20,'bold'),fg="black",bd=3,width=12)
e4.place(x=270,y=370)
Label(frame_pay,text="CVV",fg="purple",bg="cornsilk",font=("arial",20,'bold')).place(x=570,y=330)
e5=Entry(frame_pay,font=("arial",20,'bold'),fg="black",bd=3,width=10)
e5.place(x=560,y=370)
Label(frame_pay,text="Your payment details is secure",bg="cornsilk",fg="black",font=("arial",14)).place(x=320,y=460)

Label(frame_pay,text="User",font=("arial",20,'bold'),fg="purple",bg="cornsilk").place(x=270,y=420)
e1=Entry(frame_pay,font=("arial",20,'bold'),fg="black",bd=3,width=14)
e1.place(x=370,y=420)

root.mainloop()