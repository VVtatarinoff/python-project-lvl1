from random import randint

PROGR_LENGTH_MIN = 5  # минимальная длина прогрессии
PROGR_LENGTH_MAX = 10  # максимальная длина прогрессии
PROGR_START_MAX = 15   # максимальное число для начала прогрессии
PROGR_DIF_MAX = 10    # максимальный шаг прогрессии
QST_STR = 'What number is missing in the progression?'


def pr_string(start, step, qnty, miss):
    stop = start + step * (qnty - 1)
    a = list(str(x) for x in range(start, stop + 1, step))
    a[miss - 1] = '..'
    return ' '.join(a)

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def main():
    """ Игра арифметическая прогрессия, генерируется ряд чисел
    одно число заменяется двумя точками, игрок должен ввести
    правильный ответ
    Длина прогрессии, шаг, скрываемое число генерируются
    случайным образом"""

    n_terms = randint(PROGR_LENGTH_MIN, PROGR_LENGTH_MAX)    # длина прогрессии
    start = randint(1, PROGR_START_MAX)  # начальное число
    dif = randint(1, PROGR_DIF_MAX)   # шаг прогрессии
    missing = randint(1, n_terms)  # номер числа для пропуска
    ans_string = pr_string(start, dif, n_terms, missing)
    correct_answer = str(start + dif * (missing - 1))
    return ans_string, correct_answer
