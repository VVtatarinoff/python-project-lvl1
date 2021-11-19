from random import randint

EVEN_NUMBER_LIMIT = 100  # максимальное число для чет/нечет
QST_STR = 'Answer "yes" if the number is even, otherwise answer "no".'

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def is_even(n):
    return n % 2 == 0


def main():
    """ Игра чет/нечет. Генерирует случайное число"""
    random_number = randint(1, EVEN_NUMBER_LIMIT)
    correct_answer = "yes" if is_even(random_number) else "no"
    return random_number, correct_answer
