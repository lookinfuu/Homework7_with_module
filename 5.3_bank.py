import mymodule


def a_in():
    while True:
        a = input("Введите ежемесячный взнос:")
        # Проверяем правильность ввода с помощью модуля
        a = mymodule.check_float_number(a)
        if type(a) == float:
            if a < 0:
                print("Число должно быть положительным.")
                continue
            else:
                return a
        else:
            print(a)

def b_in():
    while True:
        b = input("Введите ежемесячный банковский процент:")
        # Проверяем правильность ввода с помощью модуля
        b = mymodule.check_float_number(b)
        if type(b) == float:
            if b < 0:
                print("Число должно быть положительным.")
                continue
            else:
                return b
        else:
            print(b)

def c_in():
    while True:
        c = input("Введите срок накоплений в месяцах:")
        # Проверяем правильность ввода с помощью модуля
        c = mymodule.check_int_number(c)
        if type(c) == int:
            if c < 0:
                print("Число должно быть положительным.")
                continue
            else:
                return c
        else:
            print(c)

def bank_eq(a,b,c):
    """В данном блоке считаем результат начислений
    
    a - ежемесячный взнос
    b - ежемесячный банковский процент
    c - срок накоплений в месяцах
    cash - общее количество денег
    your_cash - деньги, которые вкладывались
    bank_cash - деньги, которые начислились банком"""
    cash = a
    your_cash = 0
    bank_cash = 0
    # Каждый пробег по циклу = 1 месяцу
    for i in range(0,c):
        # Прибавляем к your_cash сумму вклада
        your_cash += a
        # Считаем сколько начислил банк
        bank_cash += cash * b / 100
        # Считаем на сколько увеличился общий вклад
        cash = cash + cash * b / 100
        # Если остался 1 месяц до закрытия вклада,
        # то деньги в конце месяца не начисляться
        # вкладчиком
        if c - i != 1:
            cash = cash + a
    return(cash, your_cash, bank_cash)

def words_in_result(ls):
    """Дополнительная проверка к блоку last_symbols()
    
    Когда предпоследняя цифра в "c" не равна единице 
    или она отсутствует"""
    # Окончание на цифру 1, написание будет "месяц"
    if ls == 1:
        flag = 1
    # Окончание на цифру: 2, 3, 4. Написание будет "месяца"
    elif ls == 2 or ls == 3 or ls == 4:
        flag = 2
    # Окончание на другие цифры. Написание будет "месяцев"
    else:
        flag = 3
    return flag

def last_symbols(c):
    """Проверяем какое указано количество месяцев
    и опираясь на это в конечном выводе соблюдаем
    грамматику
    
    ls - последняя цифра в "c"
    ls2 - предпоследняя цифра в "c"
    flag - техническая точка, для правильного
    определения грамматического написания
    """
    c = str(c)
    l = list(c)
    ls = int(l[-1])
    if len(l) > 1:
        ls2 = int(l[-2])
        # Во всех числах где предпоследняя цифра
        # равна единице, написание будет "месяцев"
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
    """Дополнительный блок, который предполагает
    о возможной интеграции межгалактической валюты,
    в случае, если прошло более 2400 месяцев"""
    if u:
        return 'intergalactic pennies'
    else:
        return ''

def bank():
    """Основная программа по рассчету вклада в банке
    с дальнейшим выводом результата"""
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
    # опирается на возможную "инфляцию"
    if c > 2400:
        cash = cash * 10 ** (-150)
        u = True
    # Вывод развернутого результата вклада 
    print(f"Итоговая сумма, спустя {c} месяц{last_symbols(c)}: {cash:.2f} {universe(u)}")
    print(f"За все время:\nВы внесли: {your_cash:.0f}\nБанк вам начислил: {bank_cash:.2f}")

bank()