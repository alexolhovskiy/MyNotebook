##Alex Olhovskiy
from tkinter import *
from tkinter import ttk
import time
import model
 
root = Tk()
root.title("Записная книга")
root.geometry("800x400")

root.columnconfigure(index=0,weight=1)
root.columnconfigure(index=1,weight=4)
for n in range(14):
    root.rowconfigure(index=n,weight=1)

label1=ttk.Label(text='Тема/Дата(Г,М,Д)',anchor=W,background="#FFCDD2",width=22)
label1.grid(column=0,row=0,sticky=NS)
entry1=ttk.Entry()
entry1.grid(column=0,row=1,padx=6,pady=6,sticky=EW)

label2=ttk.Label(text='Сообщение',anchor=W,background="#FFCDD2",width=22)
label2.grid(column=0,row=2,sticky=NS)
entry2=ttk.Entry()
entry2.grid(column=0,row=3,padx=6,pady=6,sticky=EW)

num=0
searchArr=[]

def tkEdit(event):
    global num
    entry1.delete(0,END)
    entry2.delete(0,END)
    num=lb.curselection()[0]
    if len(searchArr)>0:
        num=searchArr[num][0]
    entry1.insert(0,model.notes[num]["head"])
    entry2.insert(0,model.notes[num]["body"])

lb=Listbox()
lb.grid(row=0,rowspan=14,column=1,sticky=NSEW,padx=5,pady=5)
scroll=ttk.Scrollbar(orient="vertical",command=lb.yview)
scroll.grid(column=2,row=0,rowspan=14,sticky=NS)
lb["yscrollcommand"]=scroll.set
lb.bind("<<ListboxSelect>>",tkEdit)

def newNote():
    model.makeNote(entry1.get(),entry2.get())
    tkPrint()

def tkSave():
    model.save()

def tkLoad():
    model.load()
    tkPrint()

def tkPrint():
    searchArr.clear()
    lb.delete(0,END)
    arr=model.notesPrint()
    for i in arr:
        lb.insert(arr.index(i),i)

def tkEditConfirm():
    global num
    model.headEdit(num,entry1.get())
    model.bodyEdit(num,entry2.get())
    tkPrint()
    
def tkDelete():
    global num
    model.deleteNote(num)
    tkPrint()

def tkHeadSearch():
    global searchArr
    searchArr.clear()
    searchArr=model.getNoteByHead(entry1.get())
    arr=model.toString(searchArr)
    lb.delete(0,END)
    for i in arr:
        lb.insert(arr.index(i),i)

def tkBodySearch():
    global searchArr
    searchArr.clear()
    searchArr=model.getNoteByBody(entry2.get())
    arr=model.toString(searchArr)
    lb.delete(0,END)
    for i in arr:
        lb.insert(arr.index(i),i)

def tkDateSearch():
    global searchArr
    searchArr.clear()
    searchArr=model.getNoteByDate(time.strptime(entry1.get(),"%Y,%m,%d"))
    arr=model.toString(searchArr)
    lb.delete(0,END)
    for i in arr:
        lb.insert(arr.index(i),i)

button1=ttk.Button(text="Добавить новую запись",command=newNote)
button1.grid(column=0,row=4,padx=0,pady=0,sticky=NSEW)
button2=ttk.Button(text="Удалить запись",command=tkDelete)
button2.grid(column=0,row=5,padx=0,pady=0,sticky=NSEW)
button3=ttk.Button(text="Редактировать запись",command=tkEditConfirm)
button3.grid(column=0,row=6,padx=0,pady=0,sticky=NSEW)
button4=ttk.Button(text="Сохранить записи",command=tkSave)
button4.grid(column=0,row=7,padx=0,pady=0,sticky=NSEW)
button5=ttk.Button(text="Загрузить записи",command=tkLoad)
button5.grid(column=0,row=8,padx=0,pady=0,sticky=NSEW)
button6=ttk.Button(text="Показать все записи",command=tkPrint)
button6.grid(column=0,row=9,padx=0,pady=0,sticky=NSEW)
button7=ttk.Button(text="Найти запись по дате",command=tkDateSearch)
button7.grid(column=0,row=10,padx=0,pady=0,sticky=NSEW)
button8=ttk.Button(text="Найти запись по теме",command=tkHeadSearch)
button8.grid(column=0,row=11,padx=0,pady=0,sticky=NSEW)
button9=ttk.Button(text="Найти запись по сообщению",command=tkBodySearch)
button9.grid(column=0,row=12,padx=0,pady=0,sticky=NSEW)

root.mainloop()
