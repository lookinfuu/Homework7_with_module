from mymodule import check_int_number


def factorial(number):
    """Выполнить рассчет факториала.
    
    Ключевые аргументы:
        number -- число (по умолчанию задается пользователем).

    Возвращает:
        l[-1] -- последний элемент списка, он и является
        результатом вычисления факториала
    
    """
    # Создаем список чисел для дальнейшего
    # перемножения:
    l = list(range(1,number + 1))
    for i in range(0, len(l) - 1):
        # Берем число из списка с индексом
        # большим на единицу и присваеваем
        # ему значение произведения его
        # на предыдущее:
        l[i + 1] = l[i] * l[i + 1]
    # Возвращаем последний элемент списка,
    # это и будет результат вычислений:
    return(l[-1])


def fac_number():
    """Выполнить проверку введеных данных и выдать
    результат вычислений факториала.
    
    """
    number = ""
    print("Введите \"выход\" для выхода")
    while True:
        number = input("Введите число:")
        if number == "выход":
            break
        number = check_int_number(number)
        if type(number) == int:
            if number < 0:
                print("Число должно быть положительным.")
            # Утем, что факториал нуля равен единице:
            elif number == 0:
                print(f"{number}! = 1")
            else:
                answer = factorial(number)
                print(f"{number}! = {answer}")
        else:
            print(number)


fac_number()
