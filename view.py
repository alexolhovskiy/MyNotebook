##Alex Olhovskiy
import time

def dialogNewNote():
    head=input("Введите тему сообщения")
    boody=input("Введите сообщение")
    return head,boody

def confirm():
    c=input("Вы уверены?   ->y/n")
    if c=="y":
        return True
    return False

def delete():
    num=input("Введите номер записи которую хотите удалить")
    if num.isdigit():
        return int(num)
    return -1
    
def edit():
    num=input("Введите номер записи которую хотите редактировать")
    if num.isdigit():
        return int(num)
    return -1       

def menu():
    print("----------Меню-----------")
    print("Новая запись          ->а")
    print("Выбрать запись        ->f")
    print("Удалить запись        ->s")
    print("Редактировать запись  ->d")
    print("Сохранить записи      ->z")
    print("Загрузить записи      ->x")
    print("Распечатать           ->p")
    print("-------------------------")


def notesOutput(arr):
    print(*arr)

def searchDialog():
    print("Поиск")
    print("Поиск по номеру              ->a")
    print("Поиск по теме                ->s")
    print("Поиск по фразам в сообщении  ->d")
    print("Поиск по дате                ->f")
    return input("Делайте выбор")
    
def dialogChooseNum():
    return int(input("Введите номер записи"))

def dialogChooseHead():
    return input("Введите слово или словосочетание из темы")

def dialogChooseBoody():
    return input("Введите слово или словосочетание из сообщения")
    
def dialogChooseDate():
    return time.strptime(input("Введите дату по типу: Г,М,Д"),"%Y,%m,%d")

def editDialog():
    print("Редактировать тему      ->a")
    print("Редактировать сообщение ->s")
    return input("Делайте выбор")

def headEdit():
    return input("Введите новую тему сообщения")

def bodyEdit():
    return input("Введите новое сообщение")

def error():
    print("Ошибка ввода!")
