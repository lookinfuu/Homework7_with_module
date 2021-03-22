import mymodule
from mymodule import read_file_b


def symbols_freq_lambda():
    print("***   Программа подсчета частоты вхождений символов в текст   ***")
    # Подсчет частоты символов с помощью функции lambda,
    # создается словарь, где для каждого символа(ключа)
    # указывается его количество в тексте:
    words_dict = (lambda x: {i: x.count(i) for i in x})
    while True:
        text = input("Введите текст (Enter - взять данные из файла):")
        if not text:
            road_to_file = input("Укажите путь к файлу:")
            if not road_to_file:
                print("Данных нет.\nПопробуйте снова.")
                continue
            # Читаем данные из файла с помощью модуля mymodule:
            text = read_file_b(road_to_file)
            if not text:
                print("Данных нет.\nПопробуйте снова.")
                continue
            else:
                text = text.decode("utf-8")
        # Разбиваем текст на посимвольный список:
        text_l = list(text)
        print('Частота вхождения символов текст:')
        # Обращаемся к lamda - функции для подсчета символов
        # и записываем в symbols_freq - словарь:
        symbols_freq = words_dict(text_l)
        for i in symbols_freq:
            # Выводим результат для каждого символа(ключа) с
            # соответствующим количеством(значением):
            print(f"{i}:{symbols_freq[i]}")


symbols_freq_lambda()
