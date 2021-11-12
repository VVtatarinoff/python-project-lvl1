# модуль содержит в себе главную функцию exec_game - прогоняет циклы
# и определяет победитель/проигравший
# все остальные функции - это вопрос-ответ для каждой игры отдельно

import prompt
from random import randint

# find_gcd - поиск наибольшего делителя для двух чисел
# generate_prime_list - заполнение глобальной переменной prime_array (ниже)
from brain_games.special_functions import find_gcd, generate_prime_list

CODE_EVEN = "even"
CODE_CALC = "calc"
CODE_GCD = "gcd"
CODE_PRIME = "prime"
CODE_PROGR = "progr"
QST_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
QST_CALC = 'What is the result of the expression?'
QST_GCD = 'Find the greatest common divisor of given numbers.'
QST_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
QST_PROGR = 'What number is missing in the progression?'
GREETINGS_DICT = {CODE_EVEN: QST_EVEN,
                  CODE_CALC: QST_CALC,
                  CODE_GCD: QST_GCD,
                  CODE_PRIME: QST_PRIME,
                  CODE_PROGR: QST_PROGR}


# шаблон вопроса - для всех игр одинаковый
QUESTION_STR = "Question: {0}\nYour answer: "
WRONG_ANSWER_STRING =  "'{0}' is wrong answer ;(. Correct answer was '{1}'."
CORRECT_ANSWER = "Correct!"

# размер списка простых чисел: от 0 до (PRIME_RANGE - 1)
PRIME_RANGE = 50

PROGR_LENGTH_START = 5 # минимальная длина прогрессии
PROGR_LENGTH_END = 10  # максимальная длина прогрессии
PROGR_START_MAX = 15   # максимальное число для начала прогрессии
PROGR_STEP_MAX = 10    # максимальный шаг прогрессии

CALC_LIMIT = 10        # максимальное число для калькулятора

GCD_NUMBER_LIMIT = 25  # максимальное число для НОД

EVEN_NUMBER_LIMIT = 100  # максимальное число для чет/нечет

ROUND_COUNT = 3        # количество циклов в игре

prime_array = list()   # флаги 'простоты' чисел по индексу - bool


def ask_progr():
    """ Игра арифметическая прогрессия, генерируется ряд чисел
    одно число заменяется двумя точками, игрок должен ввести
    правильный ответ
    Длина прогрессии, шаг, скрываемое число генерируются
    случайным образом
    возвращает два параметра - ответ игрока и правильный ответ"""
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
    answer = prompt.integer(QUESTION_STR.format(ans_string))
    return answer, pr_start + pr_step * (i_missing - 1)


def ask_calc():
    """ Игра Калькулятор. Генерирует случайные числа,
    случайную операцию, задает вопрос и получает ответ игрока.
    возвращает два параметра - ответ игрока и правильный ответ"""

    operations = (' + ', " - ", " * ")
    rn_fst = randint(1, CALC_LIMIT)     # fist random number
    rn_snd = randint(1, CALC_LIMIT)      # second random number
    # as choice is limited we put it into two separated lists
    # first - type of operations
    # second - results of those operations in the same order
    correct_results = (rn_fst + rn_snd, rn_fst - rn_snd, rn_fst * rn_snd)
    r_count = randint(0, 2)     # trigger for type of operation
    ans_string = str(rn_fst) + operations[r_count] + str(rn_snd)
    user_answer = prompt.integer(QUESTION_STR.format(ans_string))
    correct_answer = correct_results[r_count]
    return user_answer, correct_answer


def ask_gcd():
    """ Игра НОД. Генерирует случайные числа,
    задает вопрос и получает ответ игрока.
    возвращает два параметра - ответ игрока и правильный ответ"""

    rn_fst = randint(1, GCD_NUMBER_LIMIT)     # fist random number
    rn_snd = randint(1, GCD_NUMBER_LIMIT)      # second random number
    ans_string = str(rn_fst) + " " + str(rn_snd)
    user_answer = prompt.integer(QUESTION_STR.format(ans_string))
    correct_answer = find_gcd(rn_fst, rn_snd)
    return user_answer, correct_answer


def ask_even():
    """ Игра чет/нечет. Генерирует случайное число,
    задает вопрос и получает ответ игрока.
    возвращает два параметра - ответ игрока и правильный ответ"""

    random_number = randint(1, EVEN_NUMBER_LIMIT)
    answer = prompt.string(QUESTION_STR.format(str(random_number)))
    correct_answer = "yes" if random_number % 2 == 0 else "no"
    return answer, correct_answer


def ask_prime():
    """Игра 'Правильное ли число?'
    функция генерирует случайное число от 0 до PRIME_RANGE - 1
    для определения простоты числа используется список prime_array
    возвращает два параметра - ответ игрока и правильный ответ"""
    random_number = randint(0, PRIME_RANGE - 1)
    answer = prompt.string(QUESTION_STR.format(str(random_number)))
    return answer, "yes" if prime_array[random_number] else "no"


# словарь со логическими функциями для каждого типа игры
GAME_FUNCTIONS = {CODE_EVEN: ask_even, CODE_PROGR: ask_progr,
                  CODE_CALC: ask_calc, CODE_GCD: ask_gcd,
                  CODE_PRIME: ask_prime}


def exec_game(game_code, user_name):
    """ входные параметры - имя игры, имя игрока"""

    is_winner = True
    print(GREETINGS_DICT[game_code])
    # если игра 'простое число', то создаем сперва проверочную таблицу,
    # чтобы не создавать ее каждый раз в цикле
    if game_code == CODE_PRIME:
        global prime_array
        prime_array = generate_prime_list(PRIME_RANGE)
    count = ROUND_COUNT
    while count > 0 and is_winner:
        user_answer, correct_answer = GAME_FUNCTIONS[game_code]()
        if user_answer == correct_answer:
            count -= 1
            print(CORRECT_ANSWER)
        else:
            print(WRONG_ANSWER_STRING.format(user_answer, correct_answer))
            is_winner = False
    print('Congratulations,' if is_winner else "Let's try again,", user_name + '!')
