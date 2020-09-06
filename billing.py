from tkinter import *
import time
import tempfile
import os
import math,random
import tkinter.messagebox as mb 
root=Tk()

SOAPLIST={
   "PEARS":40,
   "HIMALAYA":35,
   "LUX":30,
   "LIFEBOY":20,
   "MILK & HONEY":60,
   "DOVE":45

} 
CREAMLIST={

   "Lakme":570,
   "Biotique":480,
   "Nivea":366,
   "Body Shop":855,
   "Ponds":270,
   "L'Oreal Paris":599,
   "Kama Ayurveda":790
}
WASHLIST={
   "VLCC":275,
   "Biotique":288,
   "Jovees":199,
   "Clean & Clear":167,
   "BodyShop":360,
   "Himalaya":255

}
SPRAYLIST={
   "L'Oreal Paris":455,
   "Matrix":430,
   "Tresme":450,
   "Kenra Volume":390
}
GELLIST={
   "Garnier":280,
   "Set Wet":320,
   "Jolen":275,
   "Schwarzkopf":270,
   "Gatsby":240
}
LOSHANLIST={
   "Vaseline":230,
   "Joy":155,
   "Nivea":185,
   "Parachute":190,

}
TEALIST={
   "Taj Mahal":640,
   "Red Label":580,
   "Bagh Bakri":360,
   "Patanjali":420
}
SUGARLIST={
   "Brown Sugar":215,
   "White Sugar":45
}
WHEATLIST={
   "Aashiwaad Multigrains":380,
   "Natureland Organics":275,
   "Patanjali Atta":320,
   "Samrat Atta":316

}
RICELIST={
   "India Gate":70,
   "Daawat":65,
   "Kohinoor":60,
   "Hari Patti":68
}
DALLIST={
    "Arhar":54,
    "Masoor":45,
    "Moong":35,
    "Urad":40,
}
OILLIST={
     "Fortune Oil":550,
     "Saffola Oil":600,
     "Patanjali Oil":575

}
MAZALIST={
   "500ml":45,
   "1 L":84,
   "2 L":160,
}
COCALIST={
   "500ml":45,
   "1 L":84,
   "2 L":160,
}
FROOTILIST={
   "500ml":45,
   "1 L":84,
   "2 L":160,
}
THUMBSLIST={
   "500ml":45,
   "1 L":84,
   "2 L":160,
}
LIMCALIST={
   "500ml":45,
   "1 L":84,
   "2 L":160,
}
SPRITELIST={
   "500ml":45,
   "1 L":84,
   "2 L":160,
}

def total():
        '''bs=bathsoap.get()
        fc=facecream.get()'''
        totalcosmeticprice=(
            (bath.get() * SOAPLIST.get(bathsoap.get(),None))+
            (cream.get() * CREAMLIST.get(facecream.get(),None))+
            (wash.get() * WASHLIST.get(facewash.get(),None))+
            (spray.get() * SPRAYLIST.get(hairspray.get(),None))+
            (gel.get() * GELLIST.get(hairgel.get(),None))+
            (loshan.get() * LOSHANLIST.get(bodyloshan.get(),None))
        )
        cosmeticprice.set(str(totalcosmeticprice))
        ctax=(totalcosmeticprice*10)/100
        totalcosmetictax=(str(ctax))
        cosmetictax.set(totalcosmetictax)
        
        totalgroceryprice=(
            (rice.get() * RICELIST.get(ricevar.get(),None))+
            (oil.get() * OILLIST.get(oilvar.get(),None))+
            (daal.get() * DALLIST.get(dallvar.get(),None))+
            (wheat.get() * WHEATLIST.get(wheatvar.get(),None))+
            (sugar.get() * SUGARLIST.get(sugarvar.get(),None))+
            (tea.get() * TEALIST.get(teavar.get(),None))
        )
        groceryprice.set(str(totalgroceryprice))
        gtax=(totalgroceryprice*5)/100
        totalgrocerytax=(str(gtax))
        grocerytax.set(totalgrocerytax)
         
        totaldrinkprice=(
            (maza.get() * MAZALIST.get(mazavar.get(),None) )+
            (coca.get() * COCALIST.get(cocavar.get(),None))+
            (frooti.get() * FROOTILIST.get(frootivar.get(),None))+
            (thumbs.get() * THUMBSLIST.get(thumbsvar.get(),None))+
            (limca.get() * LIMCALIST.get(limcavar.get(),None))+
            (sprite.get() * SPRITELIST.get(spritevar.get(),None))
        )
        drinkprice.set(str(totaldrinkprice))
        dtax=(totaldrinkprice*2)/100
        totaldrinktax=(str(dtax))
        drinktax.set(totaldrinktax)

        
        t=totalgroceryprice+gtax+totaldrinkprice+dtax+totalcosmeticprice+ctax
        totalbill.set(float(t))
        
def billhead():
    
    textarea.delete(0.1,END)
    textarea.insert(END,"                                 SUPERMART")
    textarea.insert(END,f"\n BILL NUMBER : { bill.get() }")
    textarea.insert(END,f"\n CUSTOMER NAME : { name.get() }")
    textarea.insert(END,F"\n CONTACT NUMBER :{number.get()} ")
    textarea.insert(END,F"\n============================================")
    textarea.insert(END,F"\n ITEM NAME\t\tQTY\t\tPRICE")
    textarea.insert(END,F"\n============================================")
def billarea():
     billhead()
     if name.get()=="":
            mb.showwarning("showwarning", "Warning")
     if number.get()=="":  
            mb.showwarning("showwarning","Warning")
     if bath.get()!=0:
        textarea.insert(END,F"\n Bath Soap\t\t{bath.get()}\t\t{bath.get() * SOAPLIST.get(bathsoap.get(),None)}")
     if cream.get()!=0:
        textarea.insert(END,F"\n Face Cream\t\t{cream.get()}\t\t{cream.get() * CREAMLIST.get(facecream.get(),None)}")
     if wash.get()!=0:
        textarea.insert(END,F"\n Face Wash\t\t{wash.get()}\t\t{wash.get() * WASHLIST.get(facewash.get(),None)}")
     if spray.get()!=0:
        textarea.insert(END,F"\n Hair spray\t\t{spray.get()}\t\t{spray.get() * SPRAYLIST.get(hairspray.get(),None)}")
     if gel.get()!=0:
        textarea.insert(END,F"\n Hair Gel\t\t{gel.get()}\t\t{gel.get() * GELLIST.get(hairgel.get(),None)}")
     if loshan.get()!=0:
        textarea.insert(END,F"\n Body Lotion\t\t{loshan.get()}\t\t{loshan.get() * LOSHANLIST.get(bodyloshan.get(),None)}")
     if rice.get()!=0:
        textarea.insert(END,F"\n Rice\t\t{rice.get()}\t\t{rice.get() * RICELIST.get(ricevar.get(),None)}")
     if oil.get()!=0:
        textarea.insert(END,F"\n Food Oil\t\t{oil.get()}\t\t{oil.get() * OILLIST.get(oilvar.get(),None)}")
     if daal.get()!=0:
        textarea.insert(END,F"\n Daal\t\t{daal.get()}\t\t{daal.get() * DALLIST.get(dallvar.get(),None) }")
     if wheat.get()!=0:
        textarea.insert(END,F"\n Wheat\t\t{wheat.get()}\t\t{wheat.get() * WHEATLIST.get(wheatvar.get(),None) }")
     if sugar.get()!=0:
        textarea.insert(END,F"\n Sugar\t\t{sugar.get()}\t\t{sugar.get() * SUGARLIST.get(sugarvar.get(),None)}")
     if tea.get()!=0:
        textarea.insert(END,F"\n Tea\t\t{tea.get()}\t\t{tea.get() * TEALIST.get(teavar.get(),None)}")
     if maza.get()!=0:
        textarea.insert(END,F"\n Maza\t\t{maza.get()}\t\t{maza.get() * MAZALIST.get(mazavar.get(),None)}")
     if coca.get()!=0:
        textarea.insert(END,F"\n Coca Cola\t\t{coca.get()}\t\t{coca.get() * COCALIST.get(cocavar.get(),None)}")
     if frooti.get()!=0:
        textarea.insert(END,F"\n Frooti\t\t{frooti.get()}\t\t{frooti.get() * FROOTILIST.get(frootivar.get(),None)}")
     if thumbs.get()!=0:
        textarea.insert(END,F"\n Thumbs Up\t\t{thumbs.get()}\t\t{thumbs.get() * THUMBSLIST.get(thumbsvar.get(),None)}")
     if limca.get()!=0:
        textarea.insert(END,F"\n Limca\t\t{limca.get()}\t\t{limca.get() * LIMCALIST.get(limcavar.get(),None)}")
     if sprite.get()!=0:
        textarea.insert(END,F"\n Sprite\t\t{sprite.get()}\t\t{sprite.get() * SPRITELIST.get(spritevar.get(),None)}")
     textarea.insert(END,F"\n============================================")
     textarea.insert(END,f"\n Cosmetic Tax : { cosmetictax.get() }\n")
     textarea.insert(END,f"\n Grocery Tax : { grocerytax.get() }\n")
     textarea.insert(END,f"\n Cold Drink Tax : { drinktax.get() }\n")
     textarea.insert(END,F"\n============================================")
     textarea.insert(END,F"\n TOTAL AMOUNT : {totalbill.get()}")
                     


def reset():
      bath.set(0)
      cream.set(0)
      wash.set(0)
      spray.set(0)
      gel.set(0)
      loshan.set(0)
      rice.set(0)
      oil.set(0)
      daal.set(0)
      wheat.set(0)
      sugar.set(0)
      tea.set(0)
      maza.set(0)
      coca.set(0)
      frooti.set(0)
      thumbs.set(0)
      limca.set(0)
      sprite.set(0)
      cosmeticprice.set("")
      groceryprice.set("")
      drinkprice.set("")
      cosmetictax.set("")
      grocerytax.set("")
      drinktax.set("")
      name.set("")
      number.set("")
      bill.set("")
      x=random.randint(350,2000)
      bill.set(str(x))
    #billarea().destroy()
      totalbill.set("")

      billhead()
def pay():
     root.destroy()
     import pay
                    

root.title("BILLING")
root.geometry("1600x900")
bgcolor="black"
Label(root,text="Billing Software",bg=bgcolor,fg="white",padx=10,pady=2,font=("calibri",26,"bold"),borderwidth=5,relief=GROOVE,width=2,height=2).pack(fill=X)
local_time = time.asctime(time.localtime(time.time()))
label_info = Label(root,font= ('DigifaceWide',15,'bold','italic'), text = local_time,bg="black",width=20, fg = "pink")
label_info.place(x=25,y=14) 
 #====variables====
bath=IntVar()
cream=IntVar()
wash=IntVar()
spray=IntVar()
gel=IntVar()
loshan=IntVar()
rice=IntVar()
oil=IntVar()
daal=IntVar()
wheat=IntVar()
sugar=IntVar()
tea=IntVar()
maza=IntVar()
coca=IntVar()
frooti=IntVar()
thumbs=IntVar()
limca=IntVar()
sprite=IntVar()
cosmeticprice=StringVar()
groceryprice=StringVar()
drinkprice=StringVar()
cosmetictax=StringVar()
grocerytax=StringVar()
drinktax=StringVar()
name=StringVar()
number=StringVar()
bill=StringVar()
x=random.randint(350,2000)
bill.set(str(x))
totalbill=IntVar()

search=StringVar()
#===customer detail=====
F1=LabelFrame(root,text="Customer Details",fg="pink",bg=bgcolor,width=1600,height=95,font=("arial",16),borderwidth=5,relief=GROOVE)
F1.place(x=0,y=100,relwidth=1)

Label(F1,text="Customer Names",fg="white",bg="black",font=("times new roman",15),padx=40,pady=5).grid(row=0,column=0)
cname_ent=Entry(F1,width=30,textvariable=name,fg="black",bg="white",font=("times new roman",12))
cname_ent.grid(row=0,column=1)

Label(F1,text="Contact Number",fg="white",bg="black",font=("times new roman",15),padx=40,pady=5).grid(row=0,column=2)
cno_ent=Entry(F1,width=30,textvariable=number,fg="black",bg="white",font=("times new roman",12))
cno_ent.grid(row=0,column=3)

Label(F1,text="Bill Number",fg="white",bg="black",font=("times new roman",15),padx=40,pady=5).grid(row=0,column=4)
bn_ent=Entry(F1,width=30,textvariable=bill,fg="black",bg="white",font=("times new roman",12))
bn_ent.grid(row=0,column=5)

Button(F1,text="Search",pady=5,width=10,bd=7,command= lambda : search).grid(row=0,column=6,padx=30,pady=5)

#====cosmetic=====
F2=LabelFrame(root,text="Cosmetics",fg="pink",bg=bgcolor,width=420,height=475,font=("arial",12),borderwidth=3,relief=GROOVE)
F2.place(x=0,y=178)

Label(F2,text="Bath Soap",fg="white",bg="black",font=("times new roman",11),padx=10,pady=23).grid(row=0,column=0)
bathsoap=StringVar()
bathsoap.set("PEARS")
OptionMenu(F2,bathsoap,*SOAPLIST).grid(row=0,column=1)
a_ent=Entry(F2,width=15,textvariable=bath,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
a_ent.grid(row=0,column=2)

Label(F2,text="Face Cream",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=1,column=0)
facecream=StringVar()
facecream.set("Lakme")
OptionMenu(F2,facecream,*CREAMLIST).grid(row=1,column=1)
b_ent=Entry(F2,width=15,textvariable=cream,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
b_ent.grid(row=1,column=2)

Label(F2,text="Face Wash",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=2,column=0)
facewash=StringVar()
facewash.set("VLCC")
OptionMenu(F2,facewash,*WASHLIST).grid(row=2,column=1)
c_ent=Entry(F2,width=15,textvariable=wash,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
c_ent.grid(row=2,column=2)

Label(F2,text="Hair Spray",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=3,column=0)
hairspray=StringVar()
hairspray.set( "L'Oreal Paris")
OptionMenu(F2,hairspray,*SPRAYLIST).grid(row=3,column=1)
d_ent=Entry(F2,width=15,textvariable=spray,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
d_ent.grid(row=3,column=2)

Label(F2,text="Hair Gel",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=4,column=0)
hairgel=StringVar()
hairgel.set("Garnier")
OptionMenu(F2,hairgel,*GELLIST).grid(row=4,column=1)
e_ent=Entry(F2,width=15,textvariable=gel,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
e_ent.grid(row=4,column=2)

Label(F2,text="Body Loshan",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=5,column=0)
bodyloshan=StringVar()
bodyloshan.set("Vaseline")
OptionMenu(F2,bodyloshan,*LOSHANLIST).grid(row=5,column=1)
f_ent=Entry(F2,width=15,textvariable=loshan,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
f_ent.grid(row=5,column=2)

#===grocery===

F3=LabelFrame(root,text="Grocery",fg="pink",bg=bgcolor,width=350,height=475,font=("arial",16),borderwidth=5,relief=GROOVE)
F3.place(x=400,y=178)
Label(F3,text="Rice/kg",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=0,column=0)
ricevar=StringVar()
ricevar.set("India Gate")
OptionMenu(F3,ricevar,*RICELIST).grid(row=0,column=1)
g_ent=Entry(F3,width=15,textvariable=rice,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
g_ent.grid(row=0,column=2)

Label(F3,text="Food Oil/L",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=1,column=0)
oilvar=StringVar()
oilvar.set("Fortune Oil")
OptionMenu(F3,oilvar,*OILLIST).grid(row=1,column=1)
h_ent=Entry(F3,width=15,textvariable=oil,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
h_ent.grid(row=1,column=2)

Label(F3,text="Daal/kg",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=2,column=0)
dallvar=StringVar()
dallvar.set("Arhar")
OptionMenu(F3,dallvar,*DALLIST).grid(row=2,column=1)
i_ent=Entry(F3,width=15,textvariable=daal,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
i_ent.grid(row=2,column=2)

Label(F3,text="Wheat/5kg",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=3,column=0)
wheatvar=StringVar()
wheatvar.set("Aashiwaad Multigrains")
OptionMenu(F3,wheatvar,*WHEATLIST).grid(row=3,column=1)
j_ent=Entry(F3,width=15,textvariable=wheat,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
j_ent.grid(row=3,column=2)

Label(F3,text="Sugar/kg",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=4,column=0)
sugarvar=StringVar()
sugarvar.set("Brown Sugar")
OptionMenu(F3,sugarvar,*SUGARLIST).grid(row=4,column=1)
k_ent=Entry(F3,width=15,textvariable=sugar,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
k_ent.grid(row=4,column=2)

Label(F3,text="Tea/kg",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=5,column=0)
teavar=StringVar()
teavar.set("Taj Mahal")
OptionMenu(F3,teavar,*TEALIST).grid(row=5,column=1)
l_ent=Entry(F3,width=15,textvariable=tea,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
l_ent.grid(row=5,column=2)

#====drinks===

F4=LabelFrame(text="Cold Drinks",fg="pink",bg=bgcolor,width=350,height=475,font=("arial",16),borderwidth=5,relief=GROOVE)
F4.place(x=740,y=178)

Label(F4,text="Maza",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=0,column=0)
mazavar=StringVar()
mazavar.set("500ml")
OptionMenu(F4,mazavar,*MAZALIST).grid(row=0,column=1)
m_ent=Entry(F4,width=15,textvariable=maza,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
m_ent.grid(row=0,column=2)

Label(F4,text="Coca Cola",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=1,column=0)
cocavar=StringVar()
cocavar.set("500ml")
OptionMenu(F4,cocavar,*COCALIST).grid(row=1,column=1)
n_ent=Entry(F4,width=15,textvariable=coca,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
n_ent.grid(row=1,column=2)

Label(F4,text="Frooti",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=2,column=0)
frootivar=StringVar()
frootivar.set("500ml")
OptionMenu(F4,frootivar,*FROOTILIST).grid(row=2,column=1)
o_ent=Entry(F4,width=15,textvariable=frooti,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
o_ent.grid(row=2,column=2)

Label(F4,text="Thumbs Up",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=3,column=0)
thumbsvar=StringVar()
thumbsvar.set("500ml")
OptionMenu(F4,thumbsvar,*THUMBSLIST).grid(row=3,column=1)
p_ent=Entry(F4,width=15,textvariable=thumbs,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
p_ent.grid(row=3,column=2)

Label(F4,text="Limca",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=4,column=0)
limcavar=StringVar()
limcavar.set("500ml")
OptionMenu(F4,thumbsvar,*LIMCALIST).grid(row=4,column=1)
q_ent=Entry(F4,width=15,textvariable=limca,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
q_ent.grid(row=4,column=2)

Label(F4,text="Sprite",fg="white",bg="black",font=("times new roman",15),padx=45,pady=23).grid(row=5,column=0)
spritevar=StringVar()
spritevar.set("500ml")
OptionMenu(F4,thumbsvar,*SPRITELIST).grid(row=5,column=1)
r_ent=Entry(F4,width=15,textvariable=sprite,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
r_ent.grid(row=5,column=2)

#===bill ====

F5=LabelFrame(root,borderwidth=5,relief=GROOVE)
F5.place(x=1130,y=178,width=400,height=470)
Label(F5,text="BILL",font=("calibri",16,"bold"),padx=10,pady=5,bg="black",fg="pink").pack(fill=X)
scrol_y=Scrollbar(F5,orient=VERTICAL)
textarea=Text(F5,yscrollcommand=scrol_y.set,font=("calibri",12))
scrol_y.pack(fill=Y,side=RIGHT)
scrol_y.config(command=textarea.yview)
textarea.pack(fill=BOTH)
#===tax===
F6=LabelFrame(root,text="Billing Menu",fg="pink",bg=bgcolor,width=1600,height=130,font=("arial",16),borderwidth=5,relief=GROOVE)
F6.place(x=0,y=640,relwidth=1)

Label(F6,text="Total Cosmetic Price",fg="white",bg="black",font=("times new roman",12),padx=5,pady=3).grid(row=0,column=0)
s_ent=Entry(F6,width=10,textvariable=cosmeticprice,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
s_ent.grid(row=0,column=1)

Label(F6,text="Total Grocery Price",fg="white",bg="black",font=("times new roman",12),padx=5,pady=3).grid(row=1,column=0)
t_ent=Entry(F6,width=10,textvariable=groceryprice,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
t_ent.grid(row=1,column=1)

Label(F6,text="Total Drinks Price",fg="white",bg="black",font=("times new roman",12),padx=5,pady=3).grid(row=2,column=0)
u_ent=Entry(F6,width=10,textvariable=drinkprice,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
u_ent.grid(row=2,column=1)

Label(F6,text="Cosmetic Tax",fg="white",bg="black",font=("times new roman",12),padx=5,pady=3).grid(row=0,column=2)
v_ent=Entry(F6,width=10,textvariable=cosmetictax,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
v_ent.grid(row=0,column=3)

Label(F6,text="Grocery Tax",fg="white",bg="black",font=("times new roman",12),padx=5,pady=3).grid(row=1,column=2)
w_ent=Entry(F6,width=10,textvariable=grocerytax,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
w_ent.grid(row=1,column=3)

Label(F6,text="Drink Tax",fg="white",bg="black",font=("times new roman",12),padx=5,pady=3).grid(row=2,column=2)
x_ent=Entry(F6,width=10,textvariable=drinktax,fg="black",bg="white",font=("times new roman",12),bd=7,relief=SUNKEN)
x_ent.grid(row=2,column=3)

#===buttons====

t_btn1=Button(F6,text="TOTAL AMOUNT",font=("times new roman",16,"bold"),bg="black",fg="pink",bd=5,relief=SUNKEN,width=20,command=total)
t_btn1.grid(row=1,column=4,padx=38,pady=5)

t_btn2=Button(F6,text="Generate Bill",font=("times new roman",16,"bold"),bg="black",fg="pink",bd=5,relief=SUNKEN,width=16,command=billarea)
t_btn2.grid(row=1,column=5,padx=38,pady=3)

t_btn3=Button(F6,text="Clear",font=("times new roman",16,"bold"),bg="black",fg="pink",bd=5,relief=SUNKEN,width=12,command=reset)
t_btn3.grid(row=1,column=6,padx=38,pady=3)

t_btn4=Button(F6,text="Pay",font=("times new roman",16,"bold"),bg="black",fg="pink",bd=5,relief=SUNKEN,width=12,command=pay)
t_btn4.grid(row=1,column=7,padx=38,pady=3)    
billhead()

root.mainloop()