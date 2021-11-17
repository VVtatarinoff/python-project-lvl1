from random import randint


PROGR_LENGTH_START = 5  # минимальная длина прогрессии
PROGR_LENGTH_END = 10  # максимальная длина прогрессии
PROGR_START_MAX = 15   # максимальное число для начала прогрессии
PROGR_STEP_MAX = 10    # максимальный шаг прогрессии
QST_PROGR = 'What number is missing in the progression?'


# возвращает
#   1 первоночальный вопрос
#   2 под строка - задание
#   3 является ли ввод числом (TRUE), иначе - строка
#   4 правильный ответ

def ask_progr():
    """ Игра арифметическая прогрессия, генерируется ряд чисел
    одно число заменяется двумя точками, игрок должен ввести
    правильный ответ
    Длина прогрессии, шаг, скрываемое число генерируются
    случайным образом"""

    pr_len = randint(PROGR_LENGTH_START, PROGR_LENGTH_END)    # длина прогрессии
    pr_start = randint(1, PROGR_START_MAX)  # начальное число
    pr_step = randint(1, PROGR_STEP_MAX)   # шаг прогрессии
    i_missing = randint(1, pr_len)  # номер числа для пропуска
    count = 0
    ans_string = ""
    while count < pr_len:
        if count + 1 == i_missing:
            ans_string += ".. "
        else:
            ans_string += str(pr_start + pr_step * count)
            if count != (pr_len - 1):
                ans_string += " "
        count += 1
    correct_answer = pr_start + pr_step * (i_missing - 1)
    return QST_PROGR, ans_string, True, correct_answer
