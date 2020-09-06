from tkinter import *
from PIL import ImageTk
def Go():
    root.destroy()
    import reg
    

root=Tk()
root.title("front page")
root.config(background="gray")
root.geometry("950x430")
root.resizable(0,0)
Label(root,text="Welcome to  my first project ",bg="gray",font=("arial",50,'bold'),fg="white").pack()
Label(root,text="in Tkinter",bg="gray",font=("arial",50,'bold'),fg="white").pack()
photo=PhotoImage(file="tk.png")
photo_image=Label(root,image=photo).place(x=300,y=200)
Button(root,text="Go",font=("arial",20,'bold'),fg="black",bg="red",bd=8,command=Go).place(x=470,y=330)  


root.mainloop()