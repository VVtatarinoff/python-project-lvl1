# Модуль содержит в себе программу игры "наибольший общий делитель (НОД)"
# генерируются два случайных числа, пользователь должен вычислить
# и вывести наибольший общий делитель этих чисел
# выигрыш при трех правильных ответах

# welcome_user_new - приветствие игрока и запрос его имени
# answer_final - финальная фраза, которая разная для выгрыша и проигрыша
# answer_for_input - промежуточная фраза на каждый ответ "правильно/направильно"


from brain_games.print_answers import welcome_user_new, answer_final
from brain_games.games.brains_engine import is_winner


# запуск игры
def play_gcd_game():
    user_name = welcome_user_new()
    quest = 'Find the greatest common divisor of given numbers.'
    answer_final(user_name, is_winner('gcd', quest))
