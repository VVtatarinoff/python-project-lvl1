# Модуль содержит в себе программу игры "четное-нечетное"
# генерируются случайные числа, игрок должен ответить четное ли число
# если ввод не один из предложенных, то автоматически проигрыш
# выигрыш при трех правильных ответах

# welcome_user_new - приветствие игрока и запрос его имени
# answer_final - финальная фраза, которая разная для выгрыша и проигрыша
# answer_for_input - промежуточная фраза на каждый ответ "правильно/направильно"


import prompt
from random import randint
from brain_games.print_answers import welcome_user_new, answer_final
from brain_games.print_answers import answer_for_input


# определение правильного ответа, в зависимости от числа
def answer_even(number):
    if number % 2 == 0:
        return "yes"
    return "no"


# основной алгоритм игры
def is_winner():
    attempt_count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while attempt_count > 0:
        random_number = randint(1, 100)
        answer_string = 'Question: ' + str(random_number) + '\nYour answer: '
        answer = prompt.string(answer_string)
        correct_answer = answer_even(random_number)
        if answer == correct_answer:
            attempt_count -= 1
            answer_for_input(True)
        else:
            answer_for_input(False, answer, correct_answer)
            return False
    return True


# запуск игры
def play_even_game():
    user_name = welcome_user_new()
    answer_final(user_name, is_winner())
