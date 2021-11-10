# Модуль содержит в себе программу игры "простое ли число?"
# генерируются случайное число, пользователь должен ответить
# является ли число простым
# выигрыш при трех правильных ответах

# welcome_user_new - приветствие игрока и запрос его имени
# answer_final - финальная фраза, которая разная для выгрыша и проигрыша
# answer_for_input - промежуточная фраза на каждый ответ "правильно/направильно"


from brain_games.print_answers import welcome_user_new, answer_final
from brain_games.games.brains_engine import is_winner


# запуск игры
def play_prime_game():
    user_name = welcome_user_new()
    quest = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    answer_final(user_name, is_winner('prime', quest))
