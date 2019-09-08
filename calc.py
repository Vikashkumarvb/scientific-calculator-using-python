from tkinter import *
import time
from math import *
root=Tk()
root.title('calc')
root.config(bg='white')
fe=Frame(root,bg="#001100")
def fun(x):
    x=int(x)
    global s1,s
    if x==0:
        s1='sin'
        s.set('sin(')
    elif x==1:
        s1='cos'
        s.set('cos(')
    elif x==2:
        s1='tan'
        s.set('tan(')
    elif x==3:
        s1='ln'
        s.set('ln(')
    elif x==4:
        s1='log'
        s.set('log(')
    elif x==5:
        s1='e'
        s.set('e(')
    elif x==6:
        s1=s.get()
        s1=s1+'('
        s.set(s1)
    elif x==7:
        s1=s.get()
        s1=s1+')'
        s.set(s1)
    elif x==8:
        s1=s.get()
        s1=s1+'^'
        s.set(s1)
    elif x==9:
        s1=s.get()
        s1=s1+'%'
        s.set(s1)

        
           
def Display(a):
    global s1
    s1=s.get()
    s1=s1+a
    s.set(s1)
def result():
    global s1,s
    s1=s.get()
    if 'sin' in s1:
        i=s1.find('(')
        e=s1.find(')')
        t=s1[i+1:e]
        t=float(t)
        s.set(str(sin(t)))
   
    elif 'cos' in s1:
        i=s1.find('(')
        e=s1.find(')')
        t=s1[i+1:e]
        t=float(t)
        s.set(str(cos(t)))
    elif 'tan' in s1:
        i=s1.find('(')
        e=s1.find(')')
        t=s1[i+1:e]
        t=float(t)
        s.set(str(tan(t)))
    elif 'ln' in s1:
        i=s1.find('(')
        e=s1.find(')')
        t=s1[i+1:e]
        t=float(t)
        s.set(str(ln(t)))
    elif 'log' in s1:
        i=s1.find('(')
        e=s1.find(')')
        t=s1[i+1:e]
        t=float(t)
        s.set(str(log(t)))
    elif 'e' in s1:
        i=s1.find('(')
        e=s1.find(')')
        t=s1[i+1:e]
        t=float(t)
        s.set(str(e(t)))
    elif 'tan' in s1:
        i=s1.find('(')
        e=s1.find(')')
        t=s1[i+1:e]
        t=float(t)
        s.set(str(tan(t)))
    else:
        try:
            s1=str(eval(s1))
            s.set(s1)
        except Exception as e:
            s1=''
            s.set(e)
        
def clear():
    global s1
    s1=''
    s.set(s1)
def clear1():
    global s1
    s1=s.get()
    s1=s1[:len(s1)-1]
    s.set(s1)
s=StringVar()
s1=''
e=Entry(fe,textvariable=s,justify='right',bg='white',relief=FLAT,bd=5,fg='black',font='arial 20 bold')
e.pack(padx=5,pady=5,expand=YES,fill=BOTH)
fe.pack(padx=5,pady=5,expand=YES,fill=BOTH)
#le=['white','red','yellow','pink']
t1=['sin','cos','tan','ln','log','e','(',')','^','%']
for i in ['0123','4567','89']:
    f5=Frame(root,bg='blue')
    for j in i:
        b5=Button(f5,text='{}'.format(t1[int(j)]),bg='blue',relief=FLAT,fg='white',
                  font='arial 20 bold',command=lambda x=j:fun(x))
        b5.pack(padx=5,pady=5,expand=YES,fill=BOTH)      
    f5.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)

z=0

for i in ['789/','456*','123+','0.-']:
    f1=Frame(root,bg='white')#.format(le[z]))
    for j in i:
        b=Button(f1,text=j,bg='white',relief=FLAT,bd=5,fg='black',font='arial 20 bold',command=lambda x=j:Display(x))
        b.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
    z=z+1
    f1.pack(padx=5,pady=5,expand=YES,fill=BOTH)

f2=Frame(root,bg='blue')
b1=Button(f2,text='C',bg='blue',relief=FLAT,fg='white',font='arial 20 bold',command=clear)
b1.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
b3=Button(f2,text='CE',bg='blue',relief=FLAT,fg='white',font='arial 20 bold',command=clear1)
b3.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
b2=Button(f2 ,text='=',bg='blue',relief=FLAT,fg='white',font='arial 20 bold',command=result)
b2.pack(side=LEFT,padx=5,pady=5,expand=YES,fill=BOTH)
f2.pack(padx=5,pady=5,expand=YES,fill=BOTH)
f6=Frame(root,bg='black')
def Time():
    global l
    l['text']=time.ctime()
    l.after(1000,Time)

l=Label(f6,text=time.ctime,bg='black',relief=RAISED,fg='white',font='arial 20 bold')
l.pack(padx=5,pady=5,expand=YES,fill=BOTH)
f6.pack(padx=5,pady=5,expand=YES,fill=BOTH)
Time()
root.mainloop()


