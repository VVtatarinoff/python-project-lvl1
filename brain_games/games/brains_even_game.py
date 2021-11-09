# Модуль содержит в себе программу игры "четное-нечетное"
# генерируются случайные числа, игрок должен ответить четное ли число
# если ввод не один из предложенных, то автоматически проигрыш
# выигрыш при трех правильных ответах

# welcome_user_new - приветствие игрока и запрос его имени
# answer_final - финальная фраза, которая разная для выгрыша и проигрыша
# answer_for_input - промежуточная фраза на каждый ответ "правильно/направильно"


from brain_games.print_answers import welcome_user_new, answer_final
from brain_games.games.brains_engine import is_winner


# запуск игры
def play_even_game():
    user_name = welcome_user_new()
    quest = 'Answer "yes" if the number is even, otherwise answer "no".'
    answer_final(user_name, is_winner('even', quest))
