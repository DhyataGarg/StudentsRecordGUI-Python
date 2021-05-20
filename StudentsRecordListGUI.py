from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

def mysave():
    di=[]
    d=[]
    name=e2.get()
    roll=e3.get()
    per=e4.get()
    filename1=filename.get()
    d.append(('Name',name))
    d.append(('Rollno',roll))
    d.append(('Percentage',per))
    di.extend((roll,d))
    with open(filename1,'a')as f:
        f.write(str(di)+'\n')
    e2.delete(0,END)  
    e3.delete(0,END)
    e4.delete(0,END)
    messagebox.showinfo('showinfo','Your record has been saved')    
    return

def display():
    try:
        e2.delete(0,END) 
        e4.delete(0,END)  
        fi=filename.get()
        if e3.get()=='':
            text=ScrolledText(dg)
            text.grid(row=4,column=0)
            with open(fi) as f:
                text.delete('1.0', END)
                text.insert("1.0",f.read())
        else:
            with open(fi) as f:
                a=f.read()
                t=a.find("'"+str(e3.get())+"'")
                if t!=-1:
                    n=a[t:].find('Name')+t
                    r=a[t:].find('Rollno')+t
                    p=a[t:].find('Percentage')+t
                    s=a[t:].find(')]]')+t
                    e2.insert('0',a[n+8:r-6])
                    e4.insert('0',a[p+14:s-1])
                else:
                    messagebox.showinfo('showinfo','No result found')
    except:
         messagebox.showinfo('showinfo','No result found 1')
    return

dg=Tk()

dg.title('DHYATA')

frame1=Frame(dg, width=600,height=50,bg='black')
frame1.grid(row=0,column=0,sticky='ew')

l1=Label(frame1,text="STUDENT'S RECORD",font=('Algerian',29),bg='black',fg='white')
l1.pack(fill=BOTH)

frame2=Frame(dg, width=600,height=300,bg='green')
frame2.grid(row=1,column=0,sticky='ew')

for i in range(3):
    frame2.columnconfigure(i,weight=1)

iframe1=Frame(frame2,width=60,height=300,bg='blue')
iframe1.grid(row=0,column=0,sticky='w')

iframe2=Frame(frame2,width=500,height=300,bg='pink')
iframe2.grid(row=0,column=1,sticky='nsew')

iframe3=Frame(frame2,width=60,height=300,bg='blue')
iframe3.grid(row=0,column=2,sticky='e')

for i in range(3):
    iframe2.columnconfigure(i,weight=1)

for i in range(2):
    iframe3.columnconfigure(i,weight=1)
    
file=Label(iframe2,text='File Name',font=('Times New Roman',12),bg='pink',fg='black')
filename=Entry(iframe2,width=30)
file.grid(row=1,column=0,sticky="w")
filename.grid(row=1,column=1,sticky='e')

l2=Label(iframe2,text='Student\'s Name',font=('Times New Roman',12),bg='pink',fg='black')
e2=Entry(iframe2,width=30)

l2.grid(row=2,column=0,sticky="w")
e2.grid(row=2,column=1,sticky="e")

l3=Label(iframe2,text='Student\'s Rollno',font=('Times New Roman',12),bg='pink',fg='black')
e3=Entry(iframe2,width=30)

l3.grid(row=3,column=0,sticky='w')
e3.grid(row=3,column=1,sticky='e')

l4=Label(iframe2,text='Student\'s Percentage',font=('Times New Roman',12),bg='pink',fg='black')
e4=Entry(iframe2,width=30)

l4.grid(row=4,column=0,sticky='w')
e4.grid(row=4,column=1,sticky='e')

b=Button(iframe2,text='Save',command=mysave)
b.grid(row=0,column=0)

b=Button(iframe2,text='Open',command=display)
b.grid(row=0,column=1)

frame3=Frame(dg,width=600,height=50,bg='black')
frame3.grid(row=2,column=0,sticky=('ew'))

dg.mainloop()