import prompt


QUESTION_STR = "Question: {0}\nYour answer: "
WRONG_ANSWER_STRING = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
CORRECT_ANSWER = "Correct!"
LOST_ANS = "Let's try again,"
WIN_ANS = "Congratulations,"
ROUND_COUNT = 3        # количество циклов в игре


def exec_game(game_module):
    """ входные параметры - имя игры, имя игрока"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello,', user_name + '!')
    print(game_module.QST_STR)   # возвращается только строка с правилами
    is_winner = True
    count = ROUND_COUNT
    while count > 0 and is_winner:
        task, correct_answer = game_module.main()
        answer = prompt.string(QUESTION_STR.format(task))
        if answer == correct_answer:
            count -= 1
            print(CORRECT_ANSWER)
        else:
            print(WRONG_ANSWER_STRING.format(answer, correct_answer))
            is_winner = False
    print(WIN_ANS if is_winner else LOST_ANS, user_name + "!")
