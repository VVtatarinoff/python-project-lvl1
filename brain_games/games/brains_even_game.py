from random import randint

EVEN_NUMBER_LIMIT = 100  # максимальное число для чет/нечет
QST_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'

# возвращает
#   1 первоночальный вопрос
#   2 под строка - задание
#   3 является ли ввод числом (TRUE), иначе - строка
#   4 правильный ответ


def ask_even():
    """ Игра чет/нечет. Генерирует случайное число"""

    random_number = randint(1, EVEN_NUMBER_LIMIT)
    correct_answer = "yes" if random_number % 2 == 0 else "no"
    return QST_EVEN, random_number, False, correct_answer
