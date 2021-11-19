from random import randint

GCD_NUMBER_LIMIT = 25  # максимальное число для НОД
QST_STR = 'Find the greatest common divisor of given numbers.'
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


def main():
    """ Игра НОД. Генерирует случайные числа"""

    rn_fst = randint(1, GCD_NUMBER_LIMIT)     # fist random number
    rn_snd = randint(1, GCD_NUMBER_LIMIT)      # second random number
    ans_string = str(rn_fst) + " " + str(rn_snd)
    correct_answer = str(find_gcd(rn_fst, rn_snd))
    return ans_string, correct_answer
