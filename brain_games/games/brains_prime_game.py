from random import randint
from brain_games.special_functions import generate_prime_list

# максимальное число в игре
PRIME_RANGE = 50
QST_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'

# возвращает
#   1 первоночальный вопрос
#   2 под строка - задание
#   3 является ли ввод числом (TRUE), иначе - строка
#   4 правильный ответ


def ask_prime():
    """Игра 'Правильное ли число?'
    функция генерирует случайное число от 0 до PRIME_RANGE - 1
    для определения простоты числа используется список prime_array
    возвращает два параметра - ответ игрока и правильный ответ"""

    random_number = randint(0, PRIME_RANGE - 1)
    prime_array = generate_prime_list(PRIME_RANGE + 1)
    right_answer = "yes" if prime_array[random_number] else "no"
    return QST_PRIME, random_number, False, right_answer
