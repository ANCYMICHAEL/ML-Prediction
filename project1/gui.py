from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox,DISABLED,NORMAL
# import pymysql
import pickle
import datetime
from functools import partial
from PIL import Image, ImageTk
#from testing import process
import time
from tkinter.scrolledtext  import ScrolledText
title="Stock trend prediction"
bgmain='#344764'

def logcheck():
     global username_var,pass_var
     uname=username_var.get()
     pass1=pass_var.get()
     if uname=="ancy" and pass1=="ancym":
        showcheck()
     else:
        #showcheck()
        messagebox.showinfo("alert","Wrong Credentials")   

# show home page
def showhome():
    top.config(menu=menubar)
    global f
    f.pack_forget()
    f=Frame(top)
    f.config(bg=bgmain)
    f.pack(side="top", fill="both", expand=True,padx=10,pady=10)
    image = Image.open("leaf.jpg")
    photo = ImageTk.PhotoImage(image.resize((top.winfo_width(), top.winfo_height()), Image.ANTIALIAS))
    label = Label(f, image=photo, bg=bgmain)
    label.image = photo
    label.pack()

    l=Label(f,text="Welcome",font = "Verdana 60 bold",fg="White",bg=bgmain)
    l.place(x=500,y=300)

def showcheck():
    top.title(title)
    top.config(menu=menubar)
    global f
    f.pack_forget()
    f=Frame(top)
    f.config(bg="#5777a7")
    f.pack(side="top", fill="both", expand=True,padx=10,pady=10)

    #left 
    f1=Frame(f)
    f1.pack_propagate(False)
    f1.config(bg="#5777a7",width=500)
    f1.pack(side="left",fill="both")
    
    #right
    global f2
    f2=Frame(f)
    f2.pack_propagate(False)
    f2.config(bg="#5777a7",width=500)
    f2.pack(side="right",fill="both")

    #center
    f3=Frame(f)
    f3.pack_propagate(False)
    f3.config(bg="#5777a7",width=600)
    f3.pack(side="right",fill="both")

    f4=Frame(f3)
    f4.pack_propagate(False)
    f4.config(bg="#5777a7",height=200)
    f4.pack(side="bottom",fill="both")

    f7=Frame(f3)
    f7.pack_propagate(False)
    f7.config(height=20)
    f7.pack(side="top",fill="both",padx="3")

    l2=Label(f7,text="Process",font="Helvetica 13 bold")
    l2.pack()

    global lb1
    
    # b3=Button(f4,text="Cancel",font="Verdana 10 bold")
    # b3.pack(pady=2)
    
    

    f5=Frame(f1)
    f5.config(bg="#664a8a")
    f5.pack(side='top',fill="both",padx=10)

    
    
    global f6
    f6=Frame(f2)
    f6.config(bg="#5777a7")
    f6.pack(side="top",fill="both")
    l1=Label(f6,text="Result",font="Helvetica 13 bold")
    l1.pack(side="top",fill="both")
    
    
    global st1,st2

    # st1=ScrolledText(f5,height=5)
    # st1.pack(side="bottom",fill="both",pady=7)
    global fv1,fv2,fv3,fv4,fv5,fv6,fv7,fv8,fv9,fv10,fv11,fv12,variable
   

    fl1=Label(f5,text='SMA',bg="#664a8a",fg='white',font="Helvetica 10 bold")
    fl1.pack(pady=1)
    fv1=StringVar()
    fe1=Entry(f5,textvariable=fv1)
    fe1.pack(pady=1)

    fl2=Label(f5,text='SMA_b',bg="#664a8a",fg='white',font="Helvetica 10 bold")
    fl2.pack(pady=1)
    fv2=StringVar()
    fe2=Entry(f5,textvariable=fv2)
    fe2.pack(pady=1)

    
    fl3=Label(f5,text='WMA_b',bg="#664a8a",fg='white',font="Helvetica 10 bold")
    fl3.pack(pady=1)
    fv3=StringVar()
    fe3=Entry(f5,textvariable=fv3)
    fe3.pack(pady=1)

    fl4=Label(f5,text='STCK_b',bg="#664a8a",fg='white',font="Helvetica 10 bold")
    fl4.pack(pady=1)
    fv4=StringVar()
    fe4=Entry(f5,textvariable=fv4)
    fe4.pack(pady=1)

    fl5=Label(f5,text='MOM_b',bg="#664a8a",fg='white',font="Helvetica 10 bold")
    fl5.pack(pady=1)
    fv5=StringVar()
    fe5=Entry(f5,textvariable=fv5)
    fe5.pack(pady=1)

    fl6=Label(f5,text='LWR_b',bg="#664a8a",fg='white',font="Helvetica 10 bold")
    fl6.pack(pady=1)
    fv6=StringVar()
    fe6=Entry(f5,textvariable=fv6)
    fe6.pack(pady=1)

    fl7=Label(f5,text='ADO_b',bg="#664a8a",fg='white',font="Helvetica 10 bold")
    fl7.pack(pady=1)
    fv7=StringVar()
    fe7=Entry(f5,textvariable=fv7)
    fe7.pack(pady=1)

    fl8=Label(f5,text='CCI_b',bg="#664a8a",fg='white',font="Helvetica 10 bold")
    fl8.pack(pady=1)
    fv8=StringVar()
    fe8=Entry(f5,textvariable=fv8)
    fe8.pack(pady=1)

    

    

    b2=Button(f5,text="Prediction",fg="#d82626",font="Verdana 10 bold",command=process1)
    b2.pack(pady=5)
    
   

    st2=ScrolledText(f6,height=5)
    st2.pack(side="top",fill="both",pady=7)

    
   
    
    lb1=Listbox(f3,width=400,height=200,font="Helvetica 13 bold")
    lb1.pack(pady=20,padx=5,side='top')
    b3=Button(f1,text="Show Accuracies (Continuous)",fg="#2cd61c",font="Verdana 10 bold",command=plot1)
    b3.pack(pady=10,side='top')
    b3=Button(f1,text="Show Accuracies (Binary)",fg="#2cd61c",font="Verdana 10 bold",command=plot2)
    b3.pack(pady=10,side='top')
    
import numpy as np
from plot import plot1,plot2
    
def notint(x):
    try:
        x=float(x)
        return False
    except:
        return True   


import pickle
#from testing import NB_pred,RF_pred

def process1():
    f1=open('clf.pkl','rb')
    clf=pickle.load(f1)
    f1.close()
    
    global fv1,fv2,fv3,fv4,fv5,fv6,fv7,fv8
    global st2
    lb1.delete(0,'end')
    st2.delete('1.0','end')
    t=0
    p=0
    lb1.after(t,delayed_insert,lb1,p,"Reading values")
    t+=10
    p+=1
    st2.delete('1.0','end')
    v1=fv1.get();
    v2=fv2.get();
    v3=fv3.get();
    v4=fv4.get();
    v5=fv5.get();
    v6=fv6.get()
    v7=fv7.get()
    v8=fv8.get()
    
    ft=[v1,v2,v3,v4,v5,v6,v7,v8]
    #ft=[500,0,0,0,0,0,0,0]
    lb1.after(t,delayed_insert,lb1,p,"Creating list of value")
    t+=10
    p+=1

    for i in ft:
        if i=="":
            messagebox.showinfo('Alert','plese fill all the fields')
            return
        
   
    lb1.after(t,delayed_insert,lb1,p,"Checking Values")
    t+=10
    p+=1
    lb1.after(t,delayed_insert,lb1,p,"Prediction with Model")
    t+=10
    p+=1
    ft=np.array(ft)
    ft=ft.reshape(1,-1)
    pred=clf.predict(ft)[0]
    
    if pred==1:
        res='UP'
    else:
        res='DOWN'    

    

    #ft=[i for i in range(0,30)]
    print(pred)
    st2.after(2,showresult,res)   


    
    
    







    

def showresult(res):
    global st2

    st2.insert(INSERT,res)

#from plot import plot1


def delayed_insert(label,index,message):
    label.insert(index,message)  
    

if __name__=="__main__":

    top = Tk()  
    top.title("STOCK MARKET")
    top.geometry("1900x700")
    footer = Frame(top, bg='grey', height=30)
    footer.pack(fill='both', side='bottom')

    lab1=Label(footer,text="Developed by Ancy",font = "Verdana 8 bold",fg="white",bg="grey")
    lab1.pack()

    menubar = Menu(top)    
    menubar.add_command(label="Prediction",command=showcheck)

    top.config(bg=bgmain,relief=RAISED)  
    f=Frame(top)
    f.config(bg=bgmain)
    f.pack(side="top", fill="both", expand=True,padx=10,pady=10)
    img_ar = Image.open("image.png")
    ph_ar = ImageTk.PhotoImage(img_ar)
    lbl_ar = Label(f,image=ph_ar)
    lbl_ar.image = ph_ar
    lbl_ar.pack()
    l=Label(f,text=title,font = "Verdana 40 bold",bg=bgmain,fg="#00c853")
    l.place(x=50,y=50)
    l2=Label(f,text="Username:",font="Verdana 13 bold",bg='white')
    l2.place(x=550,y=300)
    global username_var
    username_var=StringVar()
    e1=Entry(f,textvariable=username_var,font="Verdana 13 bold")
    e1.place(x=720,y=300)

    l3=Label(f,text="Password:",font="Verdana 13 bold",bg='white')
    l3.place(x=550,y=340)
    global pass_var
    pass_var=StringVar()
    e2=Entry(f,textvariable=pass_var,font="Verdana 13 bold",show='*')
    e2.place(x=720,y=340)

    b1=Button(f,text="Login", command=logcheck,font="Verdana 13 bold")
    b1.place(x=750,y=400)

    top.mainloop() 
