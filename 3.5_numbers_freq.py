import mymodule


def a_in():
    while True:
        a = input("Введите первое число:")
        a = mymodule.check_int_number(a)
        if type(a) == int:
            return a
        else:
            print(a)

def b_in():
    while True:
        b = input("Введите второе число:")
        b = mymodule.check_int_number(b)
        if type(b) == int:
            return b
        else:
            print(b)

def symbols(num_list):
    """Считаем количесво совпадений в списке цифр"""
    # Cоздаем пустой словарь для последующей записи результата
    d = {}
    for i in num_list:
        if i in d:
            # Если цифра из num_list совпадает с ключем словаря,
            # то прибавляем единицу к значению. 
            d[i] += 1
        else:
            # Если цифра из num_list не совпала с ключем словаря,
            # или ключа нет, то создаем ключ с соответствующей
            # цифрой и присваеваем значению единицу.
            d[i] = 1
    return(d)

def number_freq():
    print("***  Программа по подсчету цифр в диапазоне чисел  ***")
    a = a_in()
    b = b_in()
    # Проверяем правильно ли пользователь ввел диапазон,
    # (от меньшего к большему)
    if a > b:
        a, b = b, a
    # Cоздаем пустой список для последующей записи цифр
    # в диапазоне чисел
    num_list = []
    # Формируем список цифр
    for i in range(a,b + 1):
        # Преобразуем число к str типу, для удобного формирования
        # списка поэлементно
        i = str(i)
        # Создаем список числа
        i = list(i)
        for u in range(0,len(i)):
            # Добавляем каждый элемент числа в список цифр
            num_list.append(i[u])
    d = symbols(num_list)
    print(f"Частота использования цифр в диапазоне чисел от {a} до {b}:")
    for i in d:
        print(f'{i}:{d[i]}')

number_freq()
