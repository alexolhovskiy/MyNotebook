import view
import model

def circle():
    while True:
        view.menu()
        c=input("Делайте выбор ")
        match c:
            case "a":
                print("Case A")
                t=view.dialog()
                model.makeNote(t[0],t[1])
            case "f":
                print("Case F")
                subMenu()
            case "s":
                print("Case S")
            case "d":
                print("Case D")
            case "z":
                print("Case Z")
            case "x":
                print("Case X")
            case "p":
                print("Case P")
                view.notesOutput(model.toString(model.notes))



def subMenu():
        view.subMenu()
        c=input("Делайте выбор")
        match c:
            case "a":
                view.notesOutput(model.toString(model.getNoteByNum(view.dialogChooseNum())))
            case "s":
                view.notesOutput(model.toString(model.getNoteByHead(view.dialogChooseHead())))
            case "d":
                view.notesOutput(model.toString(model.getNoteByBoody(view.dialogChooseBoody())))
            case "f":
                view.notesOutput(model.toString(model.getNoteByDate(view.dialogChooseDate())))
                
        

circle()
