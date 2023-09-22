##Alex Olhovskiy
import view
import model

def circle():
    while True:
        view.menu()
        c=input("Делайте выбор ")
        match c:
            case "a":
                print("Добавление")
                t=view.dialogNewNote()
                model.makeNote(t[0],t[1])
            case "f":
                print("Поиск")
                searchSubMenu()
            case "s":
                print("Удаление")
                num=view.delete()
                deleteSubMenu(num)
            case "d":
                print("Редактирование")
                num=view.edit()
                editSubMenu(num)
            case "z":
                print("Сохранение")
                model.save()
            case "x":
                print("Загрузка")
                model.load()
            case "p":
                print("Печать")
                view.notesOutput(model.notesPrint())


def deleteSubMenu():
    if num>0 & num<len(model.notes):
        print(model.getNote(num))
        if view.confirm():
            model.deleteNote(num)
    else:
        view.error()


def editSubMenu(num):
    if num>0 & num<len(model.notes):
        print(model.getNote(num))
        c=view.editDialog()
        match c:
            case "a":
                model.headEdit(num,view.headEdit())
            case "s":
                model.bodyEdit(num,view.bodyEdit())
    else:
        view.error()
        

def searchSubMenu():
    c=view.searchDialog()
    match c:
        case "a":
            view.notesOutput(model.toString(model.getNoteByNum(view.dialogChooseNum())))
        case "s":
            view.notesOutput(model.toString(model.getNoteByHead(view.dialogChooseHead())))
        case "d":
            view.notesOutput(model.toString(model.getNoteByBody(view.dialogChooseBoody())))
        case "f":
            view.notesOutput(model.toString(model.getNoteByDate(view.dialogChooseDate())))
                
        

circle()
