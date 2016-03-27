#!/usr/bin/env python3
import urllib.request

def get_content(name):
    try:
        data = bytes()
        with urllib.request.urlopen(name) as f:
            data = f.read().decode('utf-8')
        return data
    else:
        return None
    """
    Функция возвращает содержимое вики-страницы name из русской Википедии.
    В случае ошибки загрузки или отсутствия страницы возвращается None.
    """


def extract_content(page):
    start = page.find('<div id="content"')
    queque = 1 if (start > 0) else return (0, 0)
    point = start
    while(queque > 0):
        point += 3
        point  = page.find("div",point)
        if (page[point - 2: point + 4] == "</div>"):
            queque -= 1
        elif (page[point - 1: point + 4] == "<div "):
            queque += 1
    return (start, point + 3)
    """
    Функция принимает на вход содержимое страницы и возвращает 2-элементный
    tuple, первый элемент которого — номер позиции, с которой начинается
    содержимое статьи, второй элемент — номер позиции, на котором заканчивается
    содержимое статьи.
    Если содержимое отсутствует, возвращается (0, 0).
    """


def extract_links(page, begin, end):
    """
    Функция принимает на вход содержимое страницы и начало и конец интервала,
    задающего позицию содержимого статьи на странице и возвращает все имеющиеся
    ссылки на другие вики-страницы без повторений и с учётом регистра.
    """
    pass


def find_chain(start, finish):
    """
    Функция принимает на вход название начальной и конечной статьи и возвращает
    список переходов, позволяющий добраться из начальной статьи в конечную.
    Первым элементом результата должен быть start, последним — finish.
    Если построить переходы невозможно, возвращается None.
    """
    pass


def main():
    pass


if __name__ == '__main__':
    main()