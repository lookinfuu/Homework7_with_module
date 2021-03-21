import mymodule


def factorial(number):
    """Считаем факториал числа"""
    # Создаем список чисел для дальнейшего
    # перемножения
    l = list(range(1,number + 1))
    for i in range(0, len(l) - 1):
        # Берем число из списка с индексом
        # большим на единицу и присваеваем
        # ему значение произведения его
        # на предыдущее
        l[i + 1] = l[i] * l[i + 1]
    # Возвращаем последний элемент списка,
    # это и будет результат вычислений
    return(l[-1])

def fac_number(number):
    if number < 0:
        print("Число должно быть положительным.")
    # Утем, что факториал нуля равен единице
    elif number == 0:
        print(f"{number}! = 1")
    else:
        answer = factorial(number)
        print(f"{number}! = {answer}")

fac_number(mymodule.check_int_number(0))
