from random import randint

GCD_NUMBER_LIMIT = 25  # максимальное число для НОД

RULES = 'Find the greatest common divisor of given numbers.'

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def find_gcd(input1, input2):
    # сортируем по возрастанию
    if input1 > input2:
        min_value, max_value = input2, input1
    else:
        min_value, max_value = input1, input2
    while max_value % min_value != 0:
        # предыдущее меньшее число становится большим
        # остаток становится текущим меньшим числом
        max_value, min_value = min_value, max_value % min_value
    return min_value


def get_question_and_answer():
    """ Игра НОД. Генерирует случайные числа"""

    first_number = randint(1, GCD_NUMBER_LIMIT)     # fist random number
    second_number = randint(1, GCD_NUMBER_LIMIT)      # second random number
    question_to_user = f'{first_number} {second_number}'
    correct_answer = str(find_gcd(first_number, second_number))
    return question_to_user, correct_answer
