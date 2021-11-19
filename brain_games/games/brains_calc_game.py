from random import randint

CALC_LIMIT = 10        # максимальное число для калькулятора
QST_STR = 'What is the result of the expression?'

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def main():
    """ Игра Калькулятор. Генерирует случайные числа,
    случайную операцию"""
    rn_fst = randint(1, CALC_LIMIT)     # первое число
    rn_snd = randint(1, CALC_LIMIT)      # второе число
    operations = [' + ', " - ", " * "]
    correct_results = [rn_fst + rn_snd, rn_fst - rn_snd, rn_fst * rn_snd]
    r_count = randint(0, 2)     # выбрать операцию
    ans_string = str(rn_fst) + operations[r_count] + str(rn_snd)
    correct_answer = str(correct_results[r_count])
    return ans_string, correct_answer
