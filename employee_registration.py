from tkinter import*
import pymysql
import tkinter.messagebox
from PIL import ImageTk,Image

t=Tk()
t.title('profile')
t.geometry('500x300')

p=Image.open("C:\\Users\\HP 245 G7\\Pictures\\Saved Pictures\\bg.jpg.jpg")
p=p.resize((500,500))
p=ImageTk.PhotoImage(p)
pic=Label(t,image=p)
pic.place(x=0,y=0)

a=Label(text='Employee Registration',bg='black',fg='red',font=('times new roman',25,'bold'))
a.place(x=5,y=0)

b=Label(text='Employee Name: ',bg='black',fg='blue',font=('times new roman',10,'bold'))
b.place(x=5,y=65)

c=Entry(width=30)
c.place(x=110,y=65)

d=Label(text='Employee Post:',bg='black',fg='blue',font=('times new roman',10,'bold'))
d.place(x=5,y=95)

e=Entry(width=30)
e.place(x=110,y=95)

f=Label(text='Employee salary:',bg='black',fg='blue',font=('times new roman',10,'bold'))
f.place(x=5,y=125)

g=Entry(width=30)
g.place(x=110,y=125)

def fill():
    Name=c.get()
    post=e.get()
    salary=g.get()
    if (Name=="" or post=="" or salary==""):
        tkinter.messagebox.showerror('error','please complete blanked space')
    else:
        x=pymysql.connect(host='localhost',user='root',password='123456',db='employee')
        cur=x.cursor()
        cur.execute("insert into employers values('"+Name+"','"+post+"','"+salary+"')")
        x.commit()
        x.close()
        tkinter.messagebox.showinfo('Thanks','Your registration submitted.Thankyou')
        t.destroy()
        




Button(text='submit',bg='red',fg='black',font=('times new roman',15,'bold'),command=fill).place(x=215,y=200)
t.mainloop()
