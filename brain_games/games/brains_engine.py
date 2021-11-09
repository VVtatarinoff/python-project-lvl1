import prompt
from random import randint
# from brain_games.print_answers import welcome_user_new, answer_final
from brain_games.print_answers import answer_for_input
from brain_games.special_functions import find_gcd, answer_even


def ask_calc():
    operations = ('+', "-", "*")
    rn_fst = randint(1, 10)     # fist random number
    rn_snd = randint(1, 10)      # second random number
    # as choice is limited we put it into two separated lists
    # first - type of operations
    # second - results of those operations in the same order
    correct_results = (rn_fst + rn_snd, rn_fst - rn_snd, rn_fst * rn_snd)
    r_count = randint(0, 2)     # trigger for type of operation
    ans_string = str(rn_fst) + " " + operations[r_count] + " " + str(rn_snd)
    ans_string = 'Question: ' + ans_string + '\nYour answer: '
    user_answer = prompt.integer(ans_string)
    correct_answer = correct_results[r_count]
    return user_answer, correct_answer


def ask_gcd():
    rn_fst = randint(1, 100)     # fist random number
    rn_snd = randint(1, 100)      # second random number
    ans_string = str(rn_fst) + " " + str(rn_snd)
    ans_string = 'Question: ' + ans_string + '\nYour answer: '
    user_answer = prompt.integer(ans_string)
    correct_answer = find_gcd(rn_fst, rn_snd)
    return user_answer, correct_answer


def ask_even():
    random_number = randint(1, 100)
    answer_string = 'Question: ' + str(random_number) + '\nYour answer: '
    answer = prompt.string(answer_string)
    correct_answer = answer_even(random_number)
    return answer, correct_answer

# цикл с определением победиля
# на входе game - строка с названием игры, возможные варианты
# 'calc'  - калькулятора
# 'even'  - чет/нечет
# 'gcd'   - наибольший общий делитель
# quest - первоначальный вопрос по заданию
# count   - опционально, количество попыток. По умолчанию 3


def is_winner(game, quest, count=3):
    print(quest)
    while count > 0:
        if game == 'calc':
            user_answer, correct_answer = ask_calc()
        elif game == 'gcd':
            user_answer, correct_answer = ask_gcd()
        elif game == 'even':
            user_answer, correct_answer = ask_even()
        else:
            return False
        if user_answer == correct_answer:
            count -= 1
            answer_for_input(True)
        else:
            answer_for_input(False, str(user_answer), str(correct_answer))
            return False
    return True
