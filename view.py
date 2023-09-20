
def dialogNewNote():
    head=input("Введите тему сообщения")
    boody=input("Введите сообщение")
    return head,boody

def confirm():
    c=input("Удалить запись   ->y/n")
    if c=="y":
        return True
    return False

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

def subMenu():
    print("Поиск")
    print("Поиск по номеру              ->a")
    print("Поиск по теме                ->s")
    print("Поиск по фразам в сообщении  ->d")
    print("Поиск по дате                ->f")
    
def dialogChooseNum():
    return int(input("Введите номер записи"))

def dialogChooseHead():
    return input("Введите слово или словосочетание из темы")

def dialogChooseBoody():
    return input("Введите слово или словосочетание из сообщения")
    
def dialogChooseDate():
    return input("Введите дату")
