from random import randint
from brain_games.special_functions import find_gcd

GCD_NUMBER_LIMIT = 25  # максимальное число для НОД
QST_GCD = 'Find the greatest common divisor of given numbers.'

#  возвращает
#   1 первоночальный вопрос
#   2 под строка - задание
#   3 является ли ввод числом (TRUE), иначе - строка
#   4 правильный ответ


def ask_gcd():
    """ Игра НОД. Генерирует случайные числа"""

    rn_fst = randint(1, GCD_NUMBER_LIMIT)     # fist random number
    rn_snd = randint(1, GCD_NUMBER_LIMIT)      # second random number
    ans_string = str(rn_fst) + " " + str(rn_snd)
    correct_answer = find_gcd(rn_fst, rn_snd)
    return QST_GCD, ans_string, True, correct_answer
