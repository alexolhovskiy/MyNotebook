import json
import time

notes=[]

def makeNote(head,body):
    global notes
    temp={}
    temp["head"]=head
    temp["body"]=body
    temp["date"]=time.ctime()
    notes.append(temp)


def save(data):
    with open("data_file.json", "w") as write_file:
        json.dump(notes, write_file)


def load():
    with open("data_file.json", "r") as read_file:
        notes = json.load(read_file)

def printNotes():
    for i in notes:
        print(f"Тема: {i['head']},сообщение: {i['body']}, дата: {i['date']}")

def toString(anyNotes):
    arr=[]
    for i in anyNotes:
        arr.append("Запись № {},Тема: {}, Сообщение: {}, Дата: {}\n".format(anyNotes.index(i),i['head'],i['body'],i['date']))
    return arr

def getNoteByNum(num):
    arr=[]
    arr.append(notes[num])
    return arr

def getNoteByHead(worlds):
    arr=[]
    for i in notes:
        if worlds.lower() in i["head"].lower():
            arr.append(i)
    return arr

def getNoteByBoody(worlds):
    arr=[]
    for i in notes:
        if worlds.lower() in i["body"].lower():
            arr.append(i)
    return arr



makeNote("Sasha","body1")
makeNote("Masha","body2")
makeNote("Grisha","body3")
makeNote("Misha","body4")

##for i in notes:
##    print(i,end="\n")

##printNotes()

print(getNoteByHead("misha"))

print(*toString(notes))
