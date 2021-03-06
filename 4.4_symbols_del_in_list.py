def symbols_del_in_list():
    """Сформировать список без повторов в последующих элементах.

    """
    print("***  Программа по удалению повторяющихся элементов в списке  ***")
    text_list = list(input("Введите Ваш список значений:"))
    for i in text_list:
        # Присваеваем значению "a" количество элемента "i" в списке:
        a = text_list.count(i)
        if a > 1:
            # Узнаем первый индекс "i" - элемента в списке:
            i1 = text_list.index(i)
            # Выполняем цикл, пока не останеться один "i" - элемент:
            while a != 1:
                # Узнаем второй индекс "i" - элемента в списке,
                # который идет после первого "i" - элемента:
                i2 = text_list.index(i,i1 + 1,len(text_list))
                # Удаляем второй "i" - элемент в списке:
                text_list.pop(i2)
                # Присваиваем значению i1 индекс выбывшего
                # "i" - элемента, чтобы поиск следующих 
                # "i" - элементов начинался с этой точки.
                i1 = i2 - 1
                # Уменьшаем количество "i" - элементов на единицу:
                a -= 1
    print(f"Ваш список без повторов в элементах:{text_list}")


symbols_del_in_list()
