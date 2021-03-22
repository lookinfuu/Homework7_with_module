import mymodule
from mymodule import check_int_number, check_float_number


def a_in():
    """Проверит соответствие введенных данных
    классу float.
    
    Возвращает:
    a -- число типом float.
    
    """
    while True:
        a = input("Введите ежемесячный взнос:")
        a = check_float_number(a)
        if type(a) == float:
            if a < 0:
                print("Число должно быть положительным.")
                continue
            else:
                return a
        else:
            print(a)


def b_in():
    """Проверит соответствие введенных данных
    классу float.
    
    Возвращает:
    b -- число типом float.
    
    """
    while True:
        b = input("Введите ежемесячный банковский процент:")
        b = check_float_number(b)
        if type(b) == float:
            if b < 0:
                print("Число должно быть положительным.")
                continue
            else:
                return b
        else:
            print(b)


def c_in():
    """Проверит соответствие введенных данных
    классу int.
    
    Возвращает:
        c -- число типом int.
    
    """
    while True:
        c = input("Введите срок накоплений в месяцах:")
        c = check_int_number(c)
        if type(c) == int:
            if c < 0:
                print("Число должно быть положительным.")
                continue
            else:
                return c
        else:
            print(c)


def bank_eq(a,b,c):
    """Считает результат начислений.

    Ключевые аргументы:    
        a -- число(float), ежемесячный взнос.
        b -- число(float), ежемесячный банковский процент.
        c -- число(int), срок накоплений в месяцах.

    Возвращает:
        cash -- общее количество денег.
        your_cash -- деньги, которые вкладывались.
        bank_cash -- деньги, которые начислились банком.
    
    """
    cash = a
    your_cash = 0
    bank_cash = 0
    for i in range(0,c):
        # Прибавляем к your_cash сумму вклада:
        your_cash += a
        # Считаем сколько начислил банк:
        bank_cash += cash * b / 100
        # Считаем на сколько увеличился общий вклад:
        cash = cash + cash * b / 100
        # Если остался 1 месяц до закрытия вклада,
        # то деньги в конце месяца не начисляться
        # вкладчиком:
        if c - i != 1:
            cash = cash + a
    return(cash, your_cash, bank_cash)


def words_in_result(ls):
    """Делает дополнительную проверку грамматики.

    Ключевые аргументы: 
        ls -- последняя цифра из срока накоплений
    
    Возвращает:
        flag -- техническая точка для правильного
        опредления грамматического написания
    
    """
    if ls == 1:
        flag = 1
    elif ls == 2 or ls == 3 or ls == 4:
        flag = 2
    else:
        flag = 3
    return flag


def last_symbols(c):
    """Делает проверку грамматики.

    Ключевые аргументы:
        c -- число(int), срок накоплений в месяцах.

    Возвращает:
        '' -- будет использовано для правильного
        грамматического написания "месяц"
        'а' -- будет использовано для правильного
        грамматического написания "месяца"
        'ев' ---- будет использовано для правильного
        грамматического написания "месяцев"
    
    """
    c = str(c)
    l = list(c)
    ls = int(l[-1])
    if len(l) > 1:
        ls2 = int(l[-2])
        if ls2 == 1:
            flag = 3
        else:
            flag = words_in_result(ls)
    else:
        flag = words_in_result(ls)
    if flag == 1:
        return ''
    elif flag == 2:
        return 'а'
    else:
        return 'ев'


def universe(u):
    if u:
        return 'intergalactic pennies'
    else:
        return ''


def bank():
    print("*********   Программа 18+   *********")
    a = a_in()
    b = b_in()
    c = c_in()
    list_cash = bank_eq(a,b,c)
    cash = list_cash[0] 
    your_cash = list_cash[1]
    bank_cash = list_cash[2]
    u = ""
    # Если данное условие выполняется, то дальнейший рассчет
    # опирается на возможную "инфляцию":
    if c > 2400:
        cash = cash * 10 ** (-150)
        u = True
    print(f"Итоговая сумма, спустя {c} месяц{last_symbols(c)}: {cash:.2f} {universe(u)}")
    print(f"За все время:\nВы внесли: {your_cash:.0f}\nБанк вам начислил: {bank_cash:.2f}")


bank()
