import mymodule
from mymodule import read_file_b


def hooks():
    """Выполнить проверку расстоновки скобок.

    """
    print("***  Программа по проверке правильности расставленных скобок  ***")
    while True:
        text_list = list(input("Введите Ваш текст на проверку "
                               "(Enter - взять данные из файла)"))
        # Если пользователь не ввел текст,
        # то запрашиваем у него путь к файлу
        # из которого он хочет взять данные:
        if not text_list:
            road_to_file = input("Укажите путь к файлу:")
            if not road_to_file:
                print("Нет данных")
                continue
            # Если путь указан, то пробуем прочитать файл
            # по указанному пути используя модуль read_file_b:
            text = read_file_b(road_to_file)
            # Если файл не удалось прочитать, то text получил
            # значение False и пользователь получил сообщение
            # об ошибке. Начинаем цикл сначала:
            if not text:
                continue
            # Т.к. модуль читает данные в бинарном виде,
            # то возвращаем их в str представление:
            text = text.decode("utf-8")
            # Создаем поэлементный список из данных текста:
            text_list = list(text)
            if not text_list:
                print("Данных нет.\nПопробуйте снова.")
                continue
        # Создадим пустой список, в него мы будем записывать
        # открывающиеся скобки и удалять их, если найдем по
        # дальнейшему пути закрывающуюся того же типа:
        hook_list = list()
        # Создадим предварительно бинарную переменную
        # которая если получит значение False, в процессе
        # дальнейших проверок скажет нам об ошибке в скобках:
        flag = True
        for i in text_list:
            # При нахождении открывающейся скобки, 
            # мы добавляем ее в конец hook_list:
            if i == "(":
                hook_list.append(i)
            # При нахождении закрывающейся скобки, 
            # мы проверяем последнюю переменную в hook_list
            # на соответствующуюю открывающуюся скобку
            # если это она, то удаляем ее из hook_list,
            # иначе выдаем ошибку о несовпадении и даем
            # флагу значение false, и выходим из цикла:
            if i == ")":
                if hook_list and hook_list[-1] == "(":
                    hook_list.pop()
                else:
                    print("Не удалось найти пару для скобки типа: \")\"")
                    flag = False
                    break
            # Дальнейшие проверки аналогичны первой по поиску
            # скобок, только скобки другого типа:
            if i == "[":
                hook_list.append(i)
            if i == "]":
                if hook_list and hook_list[-1] == "[":
                    hook_list.pop()
                else:
                    print("Не удалось найти пару для скобки типа: \"]\"")
                    flag = False
                    break
            if i == "{":
                hook_list.append(i)
            if i == "}":
                if hook_list and hook_list[-1] == "{":
                    hook_list.pop()
                else:
                    print("Не удалось найти пару для скобки типа: \"}\"")
                    flag = False
                    break
            if i == "<":
                hook_list.append(i)
            if i == ">":
                if hook_list and hook_list[-1] == "<":
                    hook_list.pop()
                else:
                    print("Не удалось найти пару для скобки типа: \">\"")
                    flag = False
                    break
        # Проверяем остались ли какие-то данные в hook_list,
        # если да, то сообщаем пользователю об ошибке в скобках
        # и присваеваем флагу значение False:
        if len(hook_list) != 0:
            print("В тексте есть незакрытые скобки.")
            flag = False
        # Выводим пользователю результат проверки опираясь на
        # значение флага:
        print(f"Все {'хорошо' if flag == True else 'плохо'}.")


hooks()
