from brain_games.games.brains_calc_game import ask_calc
from brain_games.games.brains_even_game import ask_even
from brain_games.games.brains_gcd_game import ask_gcd
from brain_games.games.brains_prime_game import ask_prime
from brain_games.games.brains_progr_game import ask_progr


CODE_EVEN = "even"
CODE_CALC = "calc"
CODE_GCD = "gcd"
CODE_PRIME = "prime"
CODE_PROGR = "progr"""


GAME_FUNCTIONS = {CODE_EVEN: ask_even, CODE_PROGR: ask_progr,
                  CODE_CALC: ask_calc, CODE_GCD: ask_gcd,
                  CODE_PRIME: ask_prime}

# возвращает
#   1 первоночальный вопрос
#   2 строка - задание
#   3 является ли ввод числом (TRUE), иначе - строка
#   4 правильный ответ


def play_game(game_code):
    return GAME_FUNCTIONS[game_code]()
