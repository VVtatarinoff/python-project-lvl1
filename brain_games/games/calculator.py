from random import randint, choice
from operator import add, sub, mul

UPPER_LIMIT = 10        # максимальное число для калькулятора

RULES = 'What is the result of the expression?'

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def get_question_and_answer():
    """ Игра Калькулятор. Генерирует случайные числа,
    случайную операцию"""
    sign_to_operation = {'+': add, '-': sub, '*': mul}
    first_number = randint(1, UPPER_LIMIT)     # первое число
    second_number = randint(1, UPPER_LIMIT)      # второе число
    math_operations_signs = ['+', '-', '*']
    sign = choice(math_operations_signs)
    question_to_user = f'{first_number} {sign} {second_number}'
    correct_answer = str(sign_to_operation[sign](first_number,
                         second_number))
    return question_to_user, correct_answer
