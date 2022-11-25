"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def is_string(str1, str2: str) -> int:
    if not type(str1) is str or not type(str2) is str:
        return 0
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2
    if str2 == 'learn':
        return 3

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(is_string(1, 'Уася'))       # 0
    print(is_string('Уася', 'Уася'))  # 1
    print(is_string('привееет', 'Уася'))       # 2
    print(is_string('Уася', 'learn'))       # 3
# комментарий для проверки    
if __name__ == "__main__":
    main()
