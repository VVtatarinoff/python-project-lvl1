import prompt
from random import randint
# from brain_games.print_answers import welcome_user_new, answer_final
from brain_games.print_answers import answer_for_input
from brain_games.special_functions import find_gcd

# шаблон вопроса - для всех игр одинаковый
QUESTION_STR = "Question: {0}\nYour answer: "


def ask_progr():
    """ Игра арифметическая прогрессия, генерируется ряд чисел
    одно число заменяется двумя точками, игрок должен ввести
    правильный ответ
    Длина прогрессии, шаг, скрываемое число генерируются
    случайным образом
    возвращает два параметра - ответ игрока и правильный ответ"""
    pr_len = randint(5, 10)    # длина прогрессии
    pr_start = randint(1, 15)  # начальное число
    pr_step = randint(1, 10)   # шаг прогрессии
    i_missing = randint(1, pr_len)  # номер числа для пропуска
    count = 0
    ans_string = ""
    while count < pr_len:
        if count + 1 == i_missing:
            ans_string += ".. "
        else:
            ans_string += str(pr_start + pr_step * count) + " "
        count += 1
    answer = prompt.integer(QUESTION_STR.format(ans_string))
    return answer, pr_start + pr_step * (i_missing - 1)


def ask_calc():
    """ Игра Калькулятор. Генерирует случайные числа,
    случайную операцию, задает вопрос и получает ответ игрока.
    возвращает два параметра - ответ игрока и правильный ответ"""

    operations = (' + ', " - ", " * ")
    rn_fst = randint(1, 10)     # fist random number
    rn_snd = randint(1, 10)      # second random number
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

    rn_fst = randint(1, 20)     # fist random number
    rn_snd = randint(1, 30)      # second random number
    ans_string = str(rn_fst) + " " + str(rn_snd)
    user_answer = prompt.integer(QUESTION_STR.format(ans_string))
    correct_answer = find_gcd(rn_fst, rn_snd)
    return user_answer, correct_answer


def ask_even():
    """ Игра чет/нечет. Генерирует случайное число,
    задает вопрос и получает ответ игрока.
    возвращает два параметра - ответ игрока и правильный ответ"""

    random_number = randint(1, 100)
    answer = prompt.string(QUESTION_STR.format(str(random_number)))
    correct_answer = "yes" if random_number % 2 == 0 else "no"
    return answer, correct_answer


# цикл с определением победителя
# на входе game - строка с названием игры, возможные варианты
# 'calc'  - калькулятора
# 'even'  - чет/нечет
# 'gcd'   - наибольший общий делитель
# 'progr' - арифметическая прогрессия
# quest - первоначальный вопрос по заданию
# count   - опционально, количество попыток. По умолчанию 3


def is_winner(game, quest, count=3):
    """ входные параметры - имя игры, первоночальный вопрос,
    количество циклов
    возвращаемое - выиграл или нет игрок (bool"""
    # game - строка с названием игры, возможные варианты
    # 'calc'  - калькулятора
    # 'even'  - чет/нечет
    # 'gcd'   - наибольший общий делитель
    # 'progr' - арифметическая прогрессия
    print(quest)
    # словарь со ссылками на функции проверки для различных игр
    funсtions = {'even': ask_even, 'progr': ask_progr,
                 'calc': ask_calc, 'gcd': ask_gcd}
    while count > 0:
        user_answer, correct_answer = funсtions[game]()
        if user_answer == correct_answer:
            count -= 1
            answer_for_input(True)
        else:
            answer_for_input(False, str(user_answer), str(correct_answer))
            return False
    return True
