"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Ты кто?": "Я программа", "Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Язык": "Пайтон", "Версия": "3.10"}

def ask_user(answers_dict):
    question = ''
    while question!= 'Пока':
        question = input('Пользователь: ')
        if question in questions_and_answers:
            print('Программа: {0}'.format(questions_and_answers[question]))
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
