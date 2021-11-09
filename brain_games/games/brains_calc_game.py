# Модуль содержит в себе программу игры "калькулятор"
# генерируются два случайных числа, и выбирается лучайно одна из
# операций "+ или - или *"
# игрок должен посчитать ответ и ввести его
# выигрыш при трех правильных ответах

# welcome_user_new - приветствие игрока и запрос его имени
# answer_final - финальная фраза, которая разная для выгрыша и проигрыша
# answer_for_input - промежуточная фраза на каждый ответ "правильно/направильно"


import prompt
from random import randint
from brain_games.print_answers import welcome_user_new, answer_final
from brain_games.print_answers import answer_for_input


# основной алгоритм игры
def is_winner():
    attempt_count = 3
    operations = ('+', "-", "*")
    print('What is the result of the expression?')
    while attempt_count > 0:
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
        if user_answer == correct_answer:
            attempt_count -= 1
            answer_for_input(True)
        else:
            answer_for_input(False, str(user_answer), str(correct_answer))
            return False
    return True


# запуск игры
def play_calc_game():
    user_name = welcome_user_new()
    answer_final(user_name, is_winner())
