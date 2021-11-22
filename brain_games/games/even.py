from random import randint

EVEN_NUMBER_LIMIT = 100  # максимальное число для чет/нечет
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def is_even(value):
    return value % 2 == 0


def get_question_and_answer():
    """ Игра чет/нечет. Генерирует случайное число"""
    number_to_ask = randint(1, EVEN_NUMBER_LIMIT)
    correct_answer = "yes" if is_even(number_to_ask) else "no"
    return number_to_ask, correct_answer
