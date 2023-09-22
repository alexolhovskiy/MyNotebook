import json
import time

notes=[]

def makeNote(head,body):
    global notes
    temp={}
    temp["head"]=head
    temp["body"]=body
    temp["date"]=time.time()
    notes.append(temp)

def headEdit(num,head):
    global notes
    notes[num]["head"]=head
    notes[num]["date"]=time.time()

def bodyEdit(num,body):
    global notes
    notes[num]["body"]=body
    notes[num]["date"]=time.time()


def save():
    global notes
    with open("data_file.json", "w") as write_file:
        json.dump(notes,write_file)


def load():
    global notes
    with open("data_file.json", "r") as read_file:
        notes = json.load(read_file)

##def printNotes():
##    for i in notes:
##        print(f"Тема: {i['head']},сообщение: {i['body']}, дата: {time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(i['date']))}")

def notesPrint():
    arr=[]
    for i in notes:
        arr.append("Запись № {},Тема: {}, Сообщение: {}, Дата: {}\n".format(notes.index(i),i['head'],i['body'],time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i['date']))))
    return arr

def getNote(num):
    return "Запись № {},Тема: {}, Сообщение: {}, Дата: {}\n".format(num,notes[num]['head'],notes[num]['body'],time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(notes[num]['date'])))

def toString(anyNotes):
    arr=[]
    for i in anyNotes:
        arr.append("Запись № {},Тема: {}, Сообщение: {}, Дата: {}\n".format(i[0],i[1]['head'],i[1]['body'],time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i[1]['date']))))
    return arr

def getNoteByNum(num):
    arr=[]
    arr.append((num,notes[num]))
    return arr

def getNoteByHead(words):
    arr=[]
    for i in notes:
        if words.lower() in i["head"].lower():
            arr.append((notes.index(i),i))
    return arr

def getNoteByBody(words):
    arr=[]
    for i in notes:
        if words.lower() in i["body"].lower():
            arr.append((notes.index(i),i))
    return arr

def getNoteByDate(date):
    arr=[]
    for i in notes:
        if time.strftime("%Y-%m-%d",date)==time.strftime("%Y-%m-%d",time.localtime(i['date'])):
            arr.append((notes.index(i),i))
    return arr

def deleteNote(num):
    notes.pop(num)

####makeNote("Sasha","body1")
####makeNote("Masha","body2")
####makeNote("Grisha","body3")
####makeNote("Misha","body4")
##
####for i in notes:
####    print(i,end="\n")
##
####printNotes()
##
##print(getNoteByHead("misha"))
##
####print(*toString(notes))
##
####print(getNoteByDate(datetime.datetime(*[int(i) for i in "2023,9,2".split(',')])))
##print([int(i) for i in "2023,9,2".split(',')])
##print(datetime.datetime(*[int(i) for i in "2023,9,2".split(',')]))
##
