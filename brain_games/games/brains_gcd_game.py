# Модуль содержит в себе запуск игры "НОД"
# welcome_user_new - приветствие игрока и запрос его имени


from brain_games.print_answers import welcome_user_new
from brain_games.brains_engine import CODE_GCD, exec_game


# запуск игры
def play_gcd_game():
    user_name = welcome_user_new()
    exec_game(CODE_GCD, user_name)
