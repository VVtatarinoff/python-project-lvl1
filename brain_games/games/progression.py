from random import randint

PROGR_LENGTH_MIN = 5  # минимальная длина прогрессии
PROGR_LENGTH_MAX = 10  # максимальная длина прогрессии
PROGR_START_MAX = 15   # максимальное число для начала прогрессии
PROGR_DIF_MAX = 10    # максимальный шаг прогрессии

RULES = 'What number is missing in the progression?'


def get_question(members, member_to_hide):
    result = [str(x) for x in members]
    result[member_to_hide - 1] = '..'
    return ' '.join(result)


def get_progression():
    quantity_of_terms = randint(PROGR_LENGTH_MIN,
                                PROGR_LENGTH_MAX)
    start = randint(1, PROGR_START_MAX)
    difference = randint(1, PROGR_DIF_MAX)
    missing_member = randint(1, quantity_of_terms)
    stop = start + difference * (quantity_of_terms - 1)
    result = list(x for x in range(start, stop + 1, difference))
    return result, missing_member

# возвращает
#   1 под строка - задание
#   2 правильный ответ


def get_question_and_answer():
    """ Игра арифметическая прогрессия, генерируется ряд чисел
    одно число заменяется двумя точками, игрок должен ввести
    правильный ответ
    Длина прогрессии, шаг, скрываемое число генерируются
    случайным образом"""
    progression_list, member_to_hide = get_progression()
    question_to_user = get_question(progression_list, member_to_hide)
    correct_answer = str(progression_list[member_to_hide - 1])
    return question_to_user, correct_answer
