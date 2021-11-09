# Модуль содержит в себе программу игры "калькулятор"
# генерируются два случайных числа, и выбирается лучайно одна из
# операций "+ или - или *"
# игрок должен посчитать ответ и ввести его
# выигрыш при трех правильных ответах

# welcome_user_new - приветствие игрока и запрос его имени
# answer_final - финальная фраза, которая разная для выгрыша и проигрыша
# answer_for_input - промежуточная фраза на каждый ответ "правильно/направильно"


from brain_games.print_answers import welcome_user_new, answer_final
from brain_games.games.brains_engine import is_winner


# запуск игры
def play_calc_game():
    user_name = welcome_user_new()
    quest = 'What is the result of the expression?'
    answer_final(user_name, is_winner('calc', quest))
