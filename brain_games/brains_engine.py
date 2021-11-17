import prompt
from brain_games.games.game import play_game
from brain_games.print_answers import welcome_user_new

QUESTION_STR = "Question: {0}\nYour answer: "
WRONG_ANSWER_STRING = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
CORRECT_ANSWER = "Correct!"
LOST_ANS = "Let's try again,"
WIN_ANS = "Congratulations,"
ROUND_COUNT = 3        # количество циклов в игре


def exec_game(game_code):
    """ входные параметры - имя игры, имя игрока"""
    user_name = welcome_user_new()
    is_winner = True
    count = ROUND_COUNT
    while count > 0 and is_winner:
        rules_print, task, is_int, correct_answer = play_game(game_code)
        if count == ROUND_COUNT:
            print(rules_print)
        if is_int:
            answer = prompt.integer(QUESTION_STR.format(task))
        else:
            answer = prompt.string(QUESTION_STR.format(task))
        if answer == correct_answer:
            count -= 1
            print(CORRECT_ANSWER)
        else:
            print(WRONG_ANSWER_STRING.format(answer, correct_answer))
            is_winner = False
    print(WIN_ANS if is_winner else LOST_ANS, user_name + "!")
