from random import randint

CALC_LIMIT = 10        # максимальное число для калькулятора
QST_CALC = 'What is the result of the expression?'

# возвращает
#   1 первоночальный вопрос
#   2 под строка - задание
#   3 является ли ввод числом (TRUE), иначе - строка
#   4 правильный ответ


def ask_calc():
    """ Игра Калькулятор. Генерирует случайные числа,
    случайную операцию"""

    rn_fst = randint(1, CALC_LIMIT)     # первое число
    rn_snd = randint(1, CALC_LIMIT)      # второе число
    operations = [' + ', " - ", " * "]
    correct_results = [rn_fst + rn_snd, rn_fst - rn_snd, rn_fst * rn_snd]
    r_count = randint(0, 2)     # выбрать операцию
    ans_string = str(rn_fst) + operations[r_count] + str(rn_snd)
    correct_answer = correct_results[r_count]
    return QST_CALC, ans_string, True, correct_answer
