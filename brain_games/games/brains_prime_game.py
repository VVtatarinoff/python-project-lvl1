# Модуль содержит в себе запуск игры "простое ли число?"
# welcome_user_new - приветствие игрока и запрос его имени


from brain_games.print_answers import welcome_user_new
from brain_games.brains_engine import CODE_PRIME, exec_game


# запуск игры
def play_prime_game():
    user_name = welcome_user_new()
    exec_game(CODE_PRIME, user_name)
