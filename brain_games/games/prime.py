from random import randint

# максимальное число в игре
PRIME_RANGE = 50
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number_to_check):
    if number_to_check < 2:
        return False
    elif number_to_check == 2:
        return True
    counter = 2
    limit = int(number_to_check ** 0.5)
    while counter <= limit:
        if number_to_check % counter == 0:
            return False
        counter += 1
    return True

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def get_question_and_answer():
    """Игра 'Правильное ли число?'
    функция генерирует случайное число от 0 до PRIME_RANGE - 1
    для определения простоты числа используется список prime_array
    возвращает два параметра - ответ игрока и правильный ответ"""

    number_to_ask = randint(0, PRIME_RANGE - 1)
    right_answer = "yes" if is_prime(number_to_ask) else "no"
    return number_to_ask, right_answer
